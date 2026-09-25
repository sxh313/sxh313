#!/usr/bin/env python3
"""Rewrite the generated merged-PR block of the profile README.

Badges over every project that merged a pull request and has at least MIN_STARS (1,000) stars,
then one row per FEATURED project - name, what the project is, language, stars, merges - then
an ellipsis row for the remainder so every visible column adds up to the badges. The query
selects no PR title, number or URL, so the page stays at project-level counts only.

Nothing on this page duplicates what GitHub already draws next to it: the contribution totals
are deliberately not repeated here, because the profile's own graph header says the same
number one section later.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com/graphql"
START = "<!-- merged-prs:start -->"
END = "<!-- merged-prs:end -->"
MAX_PAGES = 5
MIN_STARS = 1000
DESC_MAX = 90

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

STAMP = re.compile(r"\n*<sub>.*</sub>\s*\Z")

SHIELDS = "https://img.shields.io/badge/"
# One badge style and exactly two colours for the whole page. Brand-coloured language pills and
# a different colour per metric made the block look like three dashboards stacked on each other.
LABEL_COLOR = "24292F"
ACCENT = "8250DF"


def quote(text: str) -> str:
    return urllib.parse.quote(text, safe="").replace("%2D", "--")


def metric(label: str, value: str) -> str:
    url = (
        f"{SHIELDS}{quote(label)}-{quote(value)}-{ACCENT}"
        f"?style=flat-square&labelColor={LABEL_COLOR}"
    )
    return f'<img src="{url}" alt="{value} {label.lower()}" />'


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


def render(all_rows: list[dict], featured_rows: list[dict], merged_total: int) -> str:
    if not all_rows:
        return "_Nothing merged upstream yet._"

    projects = aggregate(all_rows)
    cells = {name: tenths(entry["stars"]) for name, entry in projects.items()}
    by_stars = lambda n: (-cells[n], n)
    total_star_cells = sum(cells.values())

    out = [
        '<p align="center">',
        "  " + metric("Merged PRs", str(merged_total)),
        "  " + metric("Projects", str(len(projects))),
        "  " + metric("Upstream stars", stars(total_star_cells)),
        "</p>",
        "",
        "| Project | What it is | Language | ★ | Merged |",
        "| :-- | :-- | :-- | --: | --: |",
    ]
    for name in sorted(aggregate(featured_rows), key=by_stars):
        entry = projects[name]
        lang = entry["lang"] if entry["lang"] != "-" else "—"
        out.append(
            f"| [`{name}`](https://github.com/{name}) | {clip(entry['desc'])} "
            f"| {lang} | {stars(cells[name])} | {entry['merged']} |"
        )

    # The listed rows are a shortlist, so the remainder gets its own row: every column then
    # adds up to the badge above it, and nothing on the page over-claims.
    listed = aggregate(featured_rows)
    hidden_projects = len(projects) - len(listed)
    if hidden_projects > 0:
        rest = total_star_cells - sum(cells[name] for name in listed)
        out.append(
            f"| _… {hidden_projects} more_ | | | {stars(rest)} "
            f"| {merged_total - len(featured_rows)} |"
        )

    if len(all_rows) < merged_total:
        out += ["", f"<sub>Per-project counts cover the {len(all_rows)} most recent merges.</sub>"]
    return "\n".join(out)


def replace(text: str, start_tag: str, end_tag: str, body: str) -> tuple[str, bool]:
    """Swap one marked region. Reports whether the rendered data actually moved."""
    pattern = re.compile(re.escape(start_tag) + r"(.*?)" + re.escape(end_tag), re.S)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Marker {start_tag} not found")
    # The footnote timestamp changes every run, so compare both sides with it removed -
    # otherwise every run looks like a change and pushes a commit that only moves the clock.
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
        f"\n\n<sub>Merges only, in projects with {MIN_STARS:,}+ stars. Refreshed by "
        "[.github/workflows/refresh.yml](.github/workflows/refresh.yml)"
        f" &middot; {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</sub>"
    )

    readme = args.readme
    text = readme.read_text(encoding="utf-8")
    text, changed = replace(text, START, END, body)

    if changed:
        readme.write_text(text, encoding="utf-8", newline="\n")
        print(f"{readme} refreshed ({merged_total} merged)")
    else:
        print(f"{readme} already up to date ({merged_total} merged)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
