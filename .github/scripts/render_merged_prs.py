#!/usr/bin/env python3
"""Rewrite the aggregate open-source block of the profile README.

The query asks for no titles, numbers or URLs, and only counts are ever written out.
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
BAR = 14

PAGE = """
query($search: String!, $cursor: String) {
  search(query: $search, type: ISSUE, first: 100, after: $cursor) {
    issueCount
    pageInfo { hasNextPage endCursor }
    nodes {
      ... on PullRequest {
        mergedAt
        baseRepository {
          nameWithOwner
          stargazerCount
          primaryLanguage { name }
          owner { login }
        }
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
    """Return up to 500 matching nodes plus the server-side total count."""
    seen, pages, cursor, total = set(), [], None, 0
    for _ in range(5):
        page = gql(token, {"search": query, "cursor": cursor})
        total = page["issueCount"]
        for node in page["nodes"]:
            key = json.dumps(node, sort_keys=True)
            if key not in seen:
                seen.add(key)
                pages.append(node)
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    return pages, total


def months(seen: set[str], now: str) -> list[str]:
    if not seen:
        return []
    year, month = (int(part) for part in min(seen).split("-"))
    out = []
    while f"{year:04d}-{month:02d}" <= now:
        out.append(f"{year:04d}-{month:02d}")
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    return out[-MAX_MONTHS:]


def compact(number: int) -> str:
    return f"{number / 1000:.1f}k" if number >= 1000 else str(number)


def render(prs: list[dict], merged_total: int, open_total: int) -> str:
    if not prs:
        return "_Nothing merged upstream yet._"

    repos = {p["baseRepository"]["nameWithOwner"]: p["baseRepository"] for p in prs}
    reach = sum(repo["stargazerCount"] for repo in repos.values())
    owners = {repo["owner"]["login"] for repo in repos.values()}
    langs = Counter(
        (repo.get("primaryLanguage") or {}).get("name", "Other") for repo in repos.values()
    )
    per_month = Counter(stamp[:7] for stamp in (p["mergedAt"] for p in prs))
    first_month = min(per_month)
    now = datetime.now(timezone.utc).strftime("%Y-%m")

    out = [
        "| Merged upstream | Projects | Upstream reach | In review |",
        "| :---: | :---: | :---: | :---: |",
        f"| **{merged_total}** | **{len(repos)}** | **{compact(reach)} ★** | **{open_total}** |",
        f"| since {first_month} | {len(owners)} maintainers | combined stars | pending |",
        "",
        "```text",
    ]
    peak = max(per_month.values())
    for label in months(set(per_month), now):
        count = per_month.get(label, 0)
        width = max(1, round(count / peak * BAR)) if count else 0
        out.append(f"{label}  {'█' * width}{'░' * (BAR - width)}  {count}")
    out += ["```", "", "**Stack**  " + "  ·  ".join(
        f"{name} `{'█' * max(1, round(count / len(repos) * BAR))}` {count}/{len(repos)}"
        for name, count in langs.most_common(4)
    )]
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
    parser.add_argument(
        "--input",
        type=Path,
        help="JSON [nodes, merged total, open total] instead of calling the API.",
    )
    args = parser.parse_args()

    if args.input:
        prs, merged_total, open_total = json.loads(args.input.read_text(encoding="utf-8"))
    else:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not token:
            raise SystemExit("Set GH_TOKEN / GITHUB_TOKEN, or pass --input.")
        prs, merged_total = collect(token, f"author:{args.owner} is:pr is:merged")
        _, open_total = collect(token, f"author:{args.owner} is:pr is:open")
        prs = [p for p in prs if p.get("mergedAt")]

    body = render(prs, merged_total, open_total)

    readme = args.readme
    text = readme.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r"(.*?)" + re.escape(END), re.S)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Markers not found in {readme}")
    # The footnote timestamp changes every run, so compare on the data alone.
    if STAMP.sub("", match.group(1)).strip() == body.strip():
        print(f"{readme} already up to date ({merged_total} merged, {open_total} open)")
        return 0

    block = (
        f"{body}\n\n<sub>Refreshed "
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by "
        "[.github/workflows/refresh.yml](.github/workflows/refresh.yml). "
        "Aggregates only - individual pull requests are deliberately not listed.</sub>"
    )
    start, stop = match.span()
    readme.write_text(
        f"{text[:start]}{START}\n{block}\n{END}{text[stop:]}",
        encoding="utf-8",
        newline="\n",
    )
    print(f"{readme} refreshed ({merged_total} merged, {open_total} open)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
