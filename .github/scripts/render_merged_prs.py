#!/usr/bin/env python3
"""Rewrite the merged-PR block of the profile README.

One row per project that merged a pull request. The query selects no title, number or URL,
so an individual pull request is never named or linked.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com/graphql"
START = "<!-- merged-prs:start -->"
END = "<!-- merged-prs:end -->"
MAX_MONTHS = 12
MAX_PAGES = 5
BAR = 12

PAGE = """
query($search: String!, $cursor: String) {
  search(query: $search, type: ISSUE, first: 100, after: $cursor) {
    issueCount
    pageInfo { hasNextPage endCursor }
    nodes {
      ... on PullRequest {
        mergedAt
        baseRepository { nameWithOwner stargazerCount primaryLanguage { name } }
      }
    }
  }
}
"""

STAMP = re.compile(r"\n*<sub>.*</sub>\s*\Z")

SHIELDS = "https://img.shields.io/badge/"
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




def gql(token: str, variables: dict) -> dict:
    body = json.dumps({"query": PAGE, "variables": variables}).encode()
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
    return payload["data"]["search"]


def collect(token: str, query: str) -> tuple[list[dict], int]:
    """Return up to 500 {repo, mergedAt} records plus the server-side total count."""
    seen, rows, cursor, total = set(), [], None, 0
    for _ in range(MAX_PAGES):
        result = gql(token, {"search": query, "cursor": cursor})
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


def compact(number: int) -> str:
    return f"{number / 1000:.1f}k" if number >= 1000 else str(number)


def cadence(per_month: Counter, now: str) -> list[str]:
    if not per_month:
        return []
    year, month = (int(part) for part in min(per_month).split("-"))
    span = []
    while f"{year:04d}-{month:02d}" <= now:
        span.append(f"{year:04d}-{month:02d}")
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    peak = max(per_month.values())
    out = []
    for label in span[-MAX_MONTHS:]:
        count = per_month.get(label, 0)
        width = max(1, round(count / peak * BAR)) if count else 0
        out.append(f"{label}  {'█' * width}{'░' * (BAR - width)}  {count}")
    return out


def render(rows: list[dict], merged_total: int) -> str:
    if not rows:
        return "_Nothing merged upstream yet._"

    projects: dict[str, dict] = {}
    for row in rows:
        repo = row["repo"]
        name = repo["nameWithOwner"]
        entry = projects.setdefault(
            name,
            {
                "stars": repo["stargazerCount"],
                "lang": (repo.get("primaryLanguage") or {}).get("name") or "-",
                "merged": 0,
            },
        )
        entry["merged"] += 1

    per_month = Counter(row["stamp"][:7] for row in rows)
    now = datetime.now(timezone.utc).strftime("%Y-%m")
    order = sorted(projects, key=lambda n: (-projects[n]["stars"], n))
    total_stars = sum(entry["stars"] for entry in projects.values())

    out = [
        '<p align="center">',
        "  " + metric("Merged PRs", str(merged_total), "8250DF", "git"),
        "  " + metric("Projects", str(len(projects)), "0969DA", "box"),
        "  " + metric("GitHub stars", compact(total_stars), "BF8700", "github"),
        "</p>",
        "",
        "| Project | ★ | Language | Merged |",
        "| :-- | --: | :-- | --: |",
    ]
    for name in order:
        entry = projects[name]
        lang = pill(entry["lang"]) if entry["lang"] != "-" else "—"
        out.append(
            f"| [`{name}`](https://github.com/{name}) | {compact(entry['stars'])} "
            f"| {lang} | {entry['merged']} |"
        )
    if len(rows) < merged_total:
        out += ["", f"<sub>Per-project counts cover the {len(rows)} most recent merges.</sub>"]
    out += [
        "",
        "<details><summary>Merged per month</summary>",
        "",
        "```text",
        *cadence(per_month, now),
        "```",
        "",
        "</details>",
    ]
    return "\n".join(out)


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

    if args.input:
        rows, merged_total = json.loads(args.input.read_text(encoding="utf-8"))
    else:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not token:
            raise SystemExit("Set GH_TOKEN / GITHUB_TOKEN, or pass --input.")
        rows, merged_total = collect(token, f"author:{args.owner} is:pr is:merged")

    body = render(rows, merged_total)

    readme = args.readme
    text = readme.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r"(.*?)" + re.escape(END), re.S)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Markers not found in {readme}")
    # The footnote timestamp changes every run, so compare on the data alone.
    if STAMP.sub("", match.group(1)).strip() == body.strip():
        print(f"{readme} already up to date ({merged_total} merged)")
        return 0

    block = (
        f"{body}\n\n<sub>Merges only, per project - no individual pull request is listed. "
        f"Checked automatically by "
        "[.github/workflows/refresh.yml](.github/workflows/refresh.yml)"
        f"; last change {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}.</sub>"
    )
    start, stop = match.span()
    readme.write_text(
        f"{text[:start]}{START}\n{block}\n{END}{text[stop:]}",
        encoding="utf-8",
        newline="\n",
    )
    print(f"{readme} refreshed ({merged_total} merged)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
