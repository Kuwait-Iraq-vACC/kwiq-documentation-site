"""Order same-day procedure updates by reference number.

The blog plugin sorts posts by date only, and keeps the order in which posts
are found for posts on the same date. Posts are handed to it already ordered
by reference, which then decides the order within a day: Procedure Changes
(PRC) before Procedure NOTAMs (PRN), highest number first, then prefix A to Z.
Post file names match their references, e.g. prc-okkk-26-005.md.
"""

import os
import re

from material.plugins.blog.plugin import BlogPlugin

REFERENCE = re.compile(r"^(prc|prn)-([a-z]+)-(\d+)-(\d+)$")


def _reference_key(post):
    name = os.path.splitext(os.path.basename(post.file.src_path))[0]
    match = REFERENCE.match(name.lower())
    if not match:
        return (2, 0, 0, name)
    kind, prefix, year, number = match.groups()
    return (0 if kind == "prc" else 1, -int(year), -int(number), prefix)


def _sorted_posts(resolve_posts):
    def wrapper(self, files, config):
        return sorted(resolve_posts(self, files, config), key=_reference_key)

    wrapper.wrapped = True
    return wrapper


# Guard against wrapping twice when mkdocs serve reloads the hook
if not getattr(BlogPlugin._resolve_posts, "wrapped", False):
    BlogPlugin._resolve_posts = _sorted_posts(BlogPlugin._resolve_posts)
