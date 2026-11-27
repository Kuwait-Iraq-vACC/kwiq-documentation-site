"""Limit a page's table of contents with `toc_depth` in its front matter.

`toc_depth: 2` shows only h1 and h2 headings in that page's table of contents.
Headings and their permalinks stay on the page. Pages without `toc_depth` are
left alone.
"""


def _trim(items, depth):
    for item in items:
        item.children = [child for child in item.children if child.level <= depth]
        _trim(item.children, depth)


def on_page_context(context, page, config, nav):
    depth = page.meta.get("toc_depth")
    if isinstance(depth, int):
        _trim(page.toc.items, depth)
    return context
