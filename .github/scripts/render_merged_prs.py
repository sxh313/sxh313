#!/usr/bin/env python3
"""Rewrite the generated blocks of the profile README.

Merged-PR block: badges over every project that merged a pull request and has at least
MIN_STARS (1,000) stars, then one row per FEATURED project carrying that project's own
repository description, then an ellipsis row for the remainder so the visible counts still
add up to the badges. The query selects no PR title, number or URL, so the page stays at
project-level counts only.

Activity block: contribution, commit and repository totals for the trailing ACTIVITY_DAYS, read
from the same graph the profile page draws.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://api.github.com/graphql"
START = "<!-- merged-prs:start -->"
END = "<!-- merged-prs:end -->"
ACTIVITY_START = "<!-- activity:start -->"
ACTIVITY_END = "<!-- activity:end -->"
MAX_PAGES = 5
MIN_STARS = 1000
DESC_MAX = 90
# Contribution window in days. The prose derives from this number, so the two cannot drift apart.
ACTIVITY_DAYS = 90

# The only projects named on the page. Names are matched exactly, so a transfer or rename
# silently drops the row rather than showing the wrong project; the merges it carried stay in
# the totals and move to the ellipsis row.
FEATURED = (
    "openclaw/openclaw",
    "bytedance/deer-flow",
    "agentscope-ai/agentscope",
    "QwenLM/qwen-code",
    "TencentCloud/Octop",
)

PAGE = """
query($search: String!, $cursor: String) {
  search(query: $search, type: ISSUE, first: 100, after: $cursor) {
    issueCount
    pageInfo { hasNextPage endCursor }
    nodes {
      ... on PullRequest {
        mergedAt
        baseRepository { nameWithOwner stargazerCount description primaryLanguage { name } }
      }
    }
  }
}
"""

ACTIVITY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar { totalContributions }
      totalCommitContributions
      totalRepositoryContributions
    }
  }
}
"""

STAMP = re.compile(r"; last change \d{4}-\d\d-\d\d \d\d:\d\d UTC")

SHIELDS = "https://img.shields.io/badge/"
# One colour for all three headline totals. Purple, GitHub's own accent: three different colours
# turned the totals row into a traffic light that competed with the language pills underneath it.
ACCENT = "8250DF"
LANG_STYLE = {
    "Python": ("3776AB", "python", "white"),
    "Rust": ("000000", "rust", "white"),
    "TypeScript": ("3178C6", "typescript", "white"),
    "JavaScript": ("F7DF1E", "javascript", "black"),
    "Go": ("00ADD8", "go", "white"),
    "C++": ("00599C", "cplusplus", "white"),
    "C": ("A8B9CC", "c", "black"),
    "Java": ("ED8B00", "openjdk", "white"),
    "Kotlin": ("7F52FF", "kotlin", "white"),
    "Swift": ("F05138", "swift", "white"),
    "Ruby": ("CC342D", "rubygems", "white"),
    "Shell": ("89E051", "gnu-bash", "black"),
    "HTML": ("E34F26", "html5", "white"),
    "Vue": ("4FC08D", "vuedotjs", "black"),
}
UNKNOWN_LANG = ("8B949E", "", "white")


def quote(text: str) -> str:
    return urllib.parse.quote(text, safe="").replace("%2D", "--")


def metric(label: str, value: str, color: str, logo: str) -> str:
    """A wide labelled badge, used for the centered totals row."""
    url = (
        f"{SHIELDS}{quote(label)}-{quote(value)}-{color}"
        f"?style=for-the-badge&logo={quote(logo)}&logoColor=white"
    )
    return f'<img src="{url}" alt="{value} {label.lower()}" />'


def pill(text: str) -> str:
    """A small brand-coloured tag, used for languages inside table cells."""
    color, logo, logo_color = LANG_STYLE.get(text, UNKNOWN_LANG)
    url = f"{SHIELDS}-{quote(text)}-{color}?style=flat-square"
    if logo:
        url += f"&logo={quote(logo)}&logoColor={logo_color}"
    return f"![{text}]({url})"




def gql(token: str, query: str, variables: dict) -> dict:
    body = json.dumps({"query": query, "variables": variables}).encode()
    request = urllib.request.Request(
        API,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-readme-refresh",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = json.load(response)
    if payload.get("errors"):
        raise SystemExit(f"GraphQL errors: {json.dumps(payload['errors'])}")
    return payload["data"]


def collect(token: str, query: str) -> tuple[list[dict], int]:
    """Return up to 500 {repo, mergedAt} records plus the server-side total count."""
    seen, rows, cursor, total = set(), [], None, 0
    for _ in range(MAX_PAGES):
        result = gql(token, PAGE, {"search": query, "cursor": cursor})["search"]
        total = result["issueCount"]
        for node in result["nodes"]:
            repo, stamp = node.get("baseRepository"), node.get("mergedAt")
            if not repo or not stamp or (repo["nameWithOwner"], stamp) in seen:
                continue
            seen.add((repo["nameWithOwner"], stamp))
            rows.append({"repo": repo, "stamp": stamp})
        if not result["pageInfo"]["hasNextPage"]:
            break
        cursor = result["pageInfo"]["endCursor"]
    return rows, total


def star_floor(rows: list[dict], minimum: int = MIN_STARS) -> tuple[list[dict], int]:
    """Drop merges in projects under `minimum` stars - they read as padding, not reach."""
    kept = [row for row in rows if row["repo"]["stargazerCount"] >= minimum]
    return kept, len(rows) - len(kept)


def compact(number: int) -> str:
    return f"{number / 1000:.1f}k" if number >= 1000 else str(number)


def tenths(number: int) -> int:
    """Star counts in units of 100 - the precision the page prints.

    Rounding each cell on its own makes the column disagree with the badge over it, so every
    star figure is cut at this granularity first and the badge is the sum of the cells.
    """
    return round(number / 100)


def stars(count_tenths: int) -> str:
    return f"{count_tenths / 10:.1f}k"


def clip(text: str, limit: int = DESC_MAX) -> str:
    """One tidy table cell out of whatever the maintainer wrote in the repo description."""
    flat = " ".join(text.split()).replace("|", "\\|")
    if len(flat) <= limit:
        return flat
    return flat[: limit + 1].rsplit(" ", 1)[0].rstrip(",;:") + " …"


def aggregate(rows: list[dict]) -> dict[str, dict]:
    projects: dict[str, dict] = {}
    for row in rows:
        repo = row["repo"]
        name = repo["nameWithOwner"]
        entry = projects.setdefault(
            name,
            {
                "stars": repo["stargazerCount"],
                "desc": repo.get("description") or "",
                "lang": (repo.get("primaryLanguage") or {}).get("name") or "-",
                "merged": 0,
            },
        )
        entry["merged"] += 1
    return projects


def avatar(name: str) -> str:
    """The project's own mark, served by GitHub's avatar CDN. Requested at 48px so the 24px
    figure stays crisp on a retina screen; the non-breaking space keeps icon and name together
    when the cell wraps."""
    owner = name.split("/", 1)[0]
    return f'<img src="https://github.com/{owner}.png?size=48" width="24" height="24" alt="" />&nbsp;'


def render(all_rows: list[dict], featured_rows: list[dict], merged_total: int) -> str:
    if not all_rows:
        return "_Nothing merged upstream yet._"

    projects = aggregate(all_rows)
    cells = {name: tenths(entry["stars"]) for name, entry in projects.items()}
    by_stars = lambda n: (-cells[n], n)
    total_star_cells = sum(cells.values())

    langs = {entry["lang"] for entry in projects.values()}
    # One language across every row is noise, so the column only appears once they differ.
    show_lang = len(langs) > 1

    head = ["| Project | ★ | Language | Merged |", "| :-- | --: | :-- | --: |"] if show_lang else [
        "| Project | ★ | Merged |", "| :-- | --: | --: |"
    ]
    out = [
        '<p align="center">',
        "  " + metric("Merged PRs", str(merged_total), ACCENT, "git"),
        "  " + metric("Projects", str(len(projects)), ACCENT, "box"),
        "  " + metric("Upstream stars", stars(total_star_cells), ACCENT, "github"),
        "</p>",
        "",
    ] + head
    for name in sorted(aggregate(featured_rows), key=by_stars):
        entry = projects[name]
        label = f"{avatar(name)}[`{name}`](https://github.com/{name})"
        if entry["desc"]:
            label += f"<br><sub>{clip(entry['desc'])}</sub>"
        row = f"| {label} | {stars(cells[name])} "
        if show_lang:
            lang = pill(entry["lang"]) if entry["lang"] != "-" else "—"
            row += f"| {lang} "
        out.append(row + f"| {entry['merged']} |")

    # The five rows above are a shortlist. GitHub strips style attributes, so no row can be hidden
    # on its own and <details> cannot wrap a <tr> - but it does survive inside a cell, measured on
    # the rendered page. Keeping the tail in that row's first cell means one table with one set of
    # column widths, and the row still carries the remainder's totals, so the page adds up to the
    # badges without anyone having to click.
    listed = aggregate(featured_rows)
    hidden = {name: projects[name] for name in projects if name not in listed}
    if hidden:
        rest = total_star_cells - sum(cells[name] for name in listed)
        items = "".join(
            f"<br>{avatar(name)}[`{name}`](https://github.com/{name})"
            f" &middot; {stars(cells[name])} &middot; {hidden[name]['merged']}"
            for name in sorted(hidden, key=by_stars)
        )
        note = f"<details><summary><sub>… and {len(hidden)} more</sub></summary>{items}</details>"
        row = f"| {note} | {stars(rest)} "
        row += "| — " if show_lang else ""
        out.append(row + f"| {merged_total - len(featured_rows)} |")

    if len(all_rows) < merged_total:
        out += ["", f"<sub>Per-project counts cover the {len(all_rows)} most recent merges.</sub>"]
    return "\n".join(out)


def render_activity(token: str, owner: str) -> str:
    """The three totals GitHub's own contribution graph already publishes."""
    now = datetime.now(timezone.utc)
    collection = gql(
        token,
        ACTIVITY,
        {
            "login": owner,
            "from": (now - timedelta(days=ACTIVITY_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
    )["user"]["contributionsCollection"]

    totals = [
        ("Contributions", collection["contributionCalendar"]["totalContributions"], ACCENT, "github"),
        ("Commits", collection["totalCommitContributions"], ACCENT, "git"),
        ("Repositories touched", collection["totalRepositoryContributions"], ACCENT, "box"),
    ]
    months = ACTIVITY_DAYS // 30
    out = [
        f"Rolling {months} month{'s' if months != 1 else ''}, "
        "counted by GitHub's own contribution graph.",
        "",
        '<p align="center">',
    ]
    out += [f"  {metric(label, compact(value), color, logo)}" for label, value, color, logo in totals]
    return "\n".join(out + ["</p>"])


def replace(text: str, start_tag: str, end_tag: str, body: str) -> tuple[str, bool]:
    """Swap one marked region. Reports whether the rendered data actually moved."""
    pattern = re.compile(re.escape(start_tag) + r"(.*?)" + re.escape(end_tag), re.S)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Marker {start_tag} not found")
    # The footnote timestamp changes every run, so compare both sides with it removed -
    # otherwise every run looks like a change and pushes a commit that only moves the clock.
    # It has to be the clock alone: an earlier pattern dropped the whole footnote, which made a
    # real wording change invisible and left it uncommitted.
    if STAMP.sub("", match.group(1)).strip() == STAMP.sub("", body).strip():
        return text, False
    start, stop = match.span()
    return f"{text[:start]}{start_tag}\n{body}\n{end_tag}{text[stop:]}", True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default=os.environ.get("PROFILE_OWNER", "sxh313"))
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path(os.environ.get("GITHUB_WORKSPACE", Path(__file__).resolve().parents[2]))
        / "README.md",
    )
    parser.add_argument("--input", type=Path, help="JSON [rows, total] instead of calling the API.")
    args = parser.parse_args()

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if args.input:
        rows, merged_total = json.loads(args.input.read_text(encoding="utf-8"))
    else:
        if not token:
            raise SystemExit("Set GH_TOKEN / GITHUB_TOKEN, or pass --input.")
        rows, merged_total = collect(token, f"author:{args.owner} is:pr is:merged")

    rows, hidden = star_floor(rows)
    merged_total -= hidden

    featured = [row for row in rows if row["repo"]["nameWithOwner"] in FEATURED]

    body = render(rows, featured, merged_total) + (
        f"\n\n<sub>Merges only, counted across every project with {MIN_STARS:,}+ stars. "
        "The table names the five above; the rest expand from the line below. "
        "Checked automatically by "
        "[.github/workflows/refresh.yml](.github/workflows/refresh.yml)"
        f"; last change {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}.</sub>"
    )

    readme = args.readme
    text = readme.read_text(encoding="utf-8")
    text, changed = replace(text, START, END, body)
    # Only CI may write the activity block: a personal token sees private repositories, so a
    # local run renders larger numbers than the runner does and the two would fight forever.
    if token and os.environ.get("GITHUB_ACTIONS") == "true":
        text, activity_changed = replace(
            text, ACTIVITY_START, ACTIVITY_END, render_activity(token, args.owner)
        )
        changed = changed or activity_changed

    if changed:
        readme.write_text(text, encoding="utf-8", newline="\n")
        print(f"{readme} refreshed ({merged_total} merged)")
    else:
        print(f"{readme} already up to date ({merged_total} merged)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
