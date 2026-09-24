#!/usr/bin/env python3
"""Compare the profile's pinned items with the projects worth pinning.

Target is your own non-fork repository first, then the strongest merged-into projects above the
README's star floor. GitHub has no API for pins (six items, repositories and gists
combined, edited only in the browser), so this prints the order to apply rather than applying it.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_merged_prs import collect, star_floor  # noqa: E402

API = "https://api.github.com/graphql"
SLOTS = 6
# A grid of nothing but other people's repos hides what you build yourself.
OWN_SLOTS = 1

PINS = """
query($login: String!) {
  user(login: $login) {
    pinnedItems(first: 6) {
      nodes { __typename ... on Repository { nameWithOwner } }
    }
  }
}
"""

OWN = """
query($login: String!) {
  user(login: $login) {
    repositories(
      first: 20, ownerAffiliations: OWNER, isFork: false,
      orderBy: {field: STARGAZERS, direction: DESC}
    ) {
      nodes { nameWithOwner stargazerCount pushedAt }
    }
  }
}
"""


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default=os.environ.get("PROFILE_OWNER", "sxh313"))
    parser.add_argument("--output", type=Path, help="Write the plan here.")
    args = parser.parse_args()

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("Set GH_TOKEN / GITHUB_TOKEN.")

    rows, _ = collect(token, f"author:{args.owner} is:pr is:merged")
    # Same floor as the README, so a pin never points at a project the table hides.
    rows, _ = star_floor(rows)
    stars: dict[str, int] = {}
    merges: Counter = Counter()
    for row in rows:
        name = row["repo"]["nameWithOwner"]
        stars.setdefault(name, row["repo"]["stargazerCount"])
        merges[name] += 1
    merged_order = sorted(stars, key=lambda n: (-stars[n], n))

    own = gql(token, OWN, {"login": args.owner})["user"]["repositories"]["nodes"]
    own.sort(key=lambda n: n["pushedAt"] or "", reverse=True)
    own.sort(key=lambda n: -n["stargazerCount"])
    own_order = [n["nameWithOwner"] for n in own if n["nameWithOwner"] not in stars]

    nodes = gql(token, PINS, {"login": args.owner})["user"]["pinnedItems"]["nodes"]
    current = [n["nameWithOwner"] for n in nodes if n and n["__typename"] == "Repository"]
    gists = sum(1 for n in nodes if n and n["__typename"] != "Repository")

    # Own work leads the grid: the merged projects prove reach, this proves authorship.
    target = own_order[:OWN_SLOTS] + merged_order[:SLOTS - OWN_SLOTS]
    if len(target) < SLOTS:
        # Personal picks keep their place; a gist costs a slot, so count it.
        room = SLOTS - gists
        for name in current:
            if len(target) >= room:
                break
            if name not in target:
                target.append(name)
        target = target[:room]

    to_add = [n for n in target if n not in current]
    to_drop = [n for n in current if n not in target]

    lines = [f"Pin these {len(target)}, in this order:"]
    for pos, name in enumerate(target, 1):
        tag = f"merged x{merges[name]}" if name in merges else "personal"
        lines.append(f"  {pos}. {name:<34} {tag}")
    if to_add:
        lines.append("Add:    " + ", ".join(to_add))
    if to_drop:
        lines.append("Remove: " + ", ".join(to_drop))
    if gists:
        lines.append(f"{gists} gist(s) pinned, so {SLOTS - gists} repository slots remain.")
    if not to_add and not to_drop:
        lines.insert(1, "Already in sync.")

    plan = "\n".join(lines)
    print(plan)
    if to_add or to_drop:
        # A log line GitHub renders as an annotation on the run page.
        print(f"::warning::profile pins drift: add [{', '.join(to_add)}] remove [{', '.join(to_drop)}]")
    if args.output:
        args.output.write_text(plan + "\n", encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
