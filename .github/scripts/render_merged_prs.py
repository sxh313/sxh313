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
                "latest": row["stamp"],
            },
        )
        entry["merged"] += 1
        entry["latest"] = max(entry["latest"], row["stamp"])

    langs = Counter(entry["lang"] for entry in projects.values())
    per_month = Counter(row["stamp"][:7] for row in rows)
    now = datetime.now(timezone.utc).strftime("%Y-%m")
    order = sorted(projects, key=lambda n: (-projects[n]["stars"], n))

    out = [
        "| Project | ★ | Language | Merged | Latest |",
        "| :-- | --: | :-- | --: | :-- |",
    ]
    for name in order:
        entry = projects[name]
        out.append(
            f"| [`{name}`](https://github.com/{name}) | {compact(entry['stars'])} "
            f"| {entry['lang']} | {entry['merged']} | {entry['latest'][:10]} |"
        )
    total_stars = sum(entry["stars"] for entry in projects.values())
    out.append(
        f"| **{len(projects)} projects** | **{compact(total_stars)}** | — "
        f"| **{merged_total}** | since {min(per_month)} |"
    )
    if len(rows) < merged_total:
        out.append("")
        out.append(f"<sub>Per-project counts cover the {len(rows)} most recent merges.</sub>")
    out += [
        "",
        "<details><summary>Cadence &amp; stack</summary>",
        "",
        "```text",
        *cadence(per_month, now),
        "```",
        "",
        "**Primary languages**  " + "  ·  ".join(
            f"{name} `{'█' * max(1, round(count / max(langs.values())) * BAR)}` {count}"
            for name, count in langs.most_common(5)
        ),
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
        f"Refreshed {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by "
        "[.github/workflows/refresh.yml](.github/workflows/refresh.yml).</sub>"
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
