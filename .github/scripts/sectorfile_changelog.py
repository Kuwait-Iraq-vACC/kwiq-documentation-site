#!/usr/bin/env python3
"""Build the sector file changelog pages for the docs site from GitHub Releases.

One page per FIR (see "out" in REPOS), one entry per release, newest first.

Release notes layout:
  ## Highlights          controller-facing summary, always shown first
  ## AIRAC changes       navigation data changes
  ## Non AIRAC changes   software and content changes, grouped by ### component

Standard library only.
"""
import json
import os
import re
import urllib.request

REPOS = {
    "okac": {
        "repo": "Kuwait-Iraq-vACC/OKAC-Sectorfile",
        "name": "OKAC",
        "fir": "Kuwait FIR",
        "download": "https://files.aero-nav.com/OKAC",
        "out": "docs/Kuwait FIR/Sector File Changelog.md",
    },
    "orbb": {
        "repo": "Kuwait-Iraq-vACC/ORBB-Sectorfile",
        "name": "ORBB",
        "fir": "Baghdad FIR",
        "download": "https://files.aero-nav.com/ORBB",
        "out": "docs/Baghdad FIR/Sector File Changelog.md",
    },
}
TOKEN = os.environ.get("GITHUB_TOKEN", "")
INCLUDE_PRERELEASES = os.environ.get("INCLUDE_PRERELEASES", "false").lower() == "true"
SECTION_ORDER = ["highlights", "airac changes", "non airac changes"]

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
STRIP_LINES = re.compile(r"^\s*\**full changelog\**\s*:", re.I)
PR_CREDIT = re.compile(r"\s+by @[\w-]+(?:\[bot\])? in (https://github\.com/\S+/pull/(\d+))")
BARE_URL = re.compile(r"(?<![(<\"\w/])(https?://[^\s)<>\]]+)")
MD_LINK = re.compile(r"(?<!!)\[([^\]]*)\]\((\S+?)(?:\s+\"[^\"]*\")?\)(?!\{)")
DROP_SECTIONS = {"new contributors"}


def fetch_releases(repo):
    releases, page = [], 1
    while True:
        req = urllib.request.Request(
            f"https://api.github.com/repos/{repo}/releases?per_page=100&page={page}",
            headers={"Accept": "application/vnd.github+json", "User-Agent": "kwiq-changelog"},
        )
        if TOKEN:
            req.add_header("Authorization", f"Bearer {TOKEN}")
        with urllib.request.urlopen(req) as resp:
            batch = json.load(resp)
        if not batch:
            return releases
        releases.extend(batch)
        page += 1


def split_sections(body):
    """Split release notes into (top-level heading level, [(title, lines)]).

    Older releases that don't use the template still show up: text before the first
    heading becomes a "Changes" section, and GitHub's auto-generated credits are tidied.
    """
    lines = []
    for line in (body or "").replace("\r", "").split("\n"):
        if STRIP_LINES.match(line):
            continue
        lines.append(PR_CREDIT.sub(lambda m: f" ([#{m.group(2)}]({m.group(1)}))", line))
    top = min((len(m.group(1)) for m in map(HEADING.match, lines) if m), default=1)
    current = ("Changes", [])
    sections = [current]
    for line in lines:
        m = HEADING.match(line)
        if m and len(m.group(1)) == top:
            current = (m.group(2).strip(), [])
            sections.append(current)
        else:
            current[1].append(line)
    sections = [
        (t, b) for t, b in sections
        if t.lower() not in DROP_SECTIONS and (t != "Changes" or "\n".join(b).strip())
    ]
    return top, sections


def nest(lines, from_level, to_level):
    """Shift headings so that from_level becomes to_level."""
    out = []
    for line in lines:
        m = HEADING.match(line)
        if m:
            line = f"{'#' * max(1, min(6, len(m.group(1)) - from_level + to_level))} {m.group(2)}"
        out.append(line)
    return "\n".join(out).strip()


def new_tab_links(text):
    """Turn bare URLs into links, and make every link open in a new tab (needs attr_list)."""
    text = BARE_URL.sub(lambda m: f"[{m.group(1)}]({m.group(1)})", text)
    return MD_LINK.sub(lambda m: f'[{m.group(1)}]({m.group(2)} "Opens in new tab"){{target="_blank"}}', text)


def order_key(title):
    t = title.lower()
    return SECTION_ORDER.index(t) if t in SECTION_ORDER else len(SECTION_ORDER)


def release_title(rel):
    return (rel.get("name") or rel["tag_name"]).strip()


def render(cfg, releases):
    repo = cfg["repo"]
    title = f"{cfg['name']} Sector File Changelog"
    if releases:
        title += f" ({releases[0]['tag_name']})"
    lines = [
        "---",
        f"title: {title}",
        "---",
        "",
        f"# {title}",
        "",
        f"Every change to the {cfg['name']} sector file for the {cfg['fir']}, newest first. "
        "Each release starts with its highlights: the changes that matter to controllers. "
        f"Download the latest package from [AeroNav]({cfg['download']}), and report bugs or "
        f"request features on [GitHub](https://github.com/{repo}/issues).",
        "",
    ]
    if not releases:
        lines += ["No releases yet.", ""]
    for i, rel in enumerate(releases):
        tag = rel["tag_name"]
        lines += [f"## {release_title(rel)}", ""]
        top, sections = split_sections(rel.get("body"))
        names = [t.lower() for t, _ in sections]
        if "highlights" not in names:
            sections.insert(0, ("Highlights", ["No major changes."]))
        sections.sort(key=lambda s: order_key(s[0]))
        for title, body in sections:
            lines += [f"### {title}", "", nest(body, top + 1, 4) or "NIL", ""]
        previous = releases[i + 1]["tag_name"] if i + 1 < len(releases) else None
        files = f"https://github.com/{repo}/compare/{previous}...{tag}" if previous else rel["html_url"]
        lines += [f"[Files updated]({files}) · [Release]({rel['html_url']})", ""]
        if i + 1 < len(releases):
            lines += ["---", ""]
    return new_tab_links("\n".join(lines).rstrip() + "\n")


def main():
    for cfg in REPOS.values():
        releases = [
            r for r in fetch_releases(cfg["repo"])
            if not r.get("draft") and (INCLUDE_PRERELEASES or not r.get("prerelease"))
        ]
        releases.sort(key=lambda r: r.get("published_at") or "", reverse=True)
        path = cfg["out"]
        content = render(cfg, releases)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if content == old:
            print(f"Unchanged {path}")
            continue
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Updated {path}")


if __name__ == "__main__":
    main()
