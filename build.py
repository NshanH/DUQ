#!/usr/bin/env python3
"""Build the published pages from the sources in src/.

src/duq-copy.html is the prototype as the Claude artifact «DUQ test · копия» holds it: a page fragment that links
src/tokens.css. Each page is that fragment made self-contained: the token sheet inlined, and the document shell
(doctype, head, body) written around it, with <body> opened before the scripts that need document.body.

    index.html       the prototype
    flow/index.html  the same prototype with the landing background swapped for the Flow Field test
                     (src/flow-addon.html appended; the Claude artifact «DUQ Flow Field» holds the same page)

    python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC, CSS = ROOT / 'src/duq-copy.html', ROOT / 'src/tokens.css'
FLOW = ROOT / 'src/flow-addon.html'


def page(s: str, css: str) -> str:
    # 1. the token sheet goes inline in place of its link
    link = '<link rel="stylesheet" href="tokens.css">'
    assert s.count(link) == 1, 'expected one link to tokens.css'
    s = s.replace(link, '<style>\n' + css + '\n</style>')
    # 2. the fragment starts with its own charset; the shell below carries it instead
    first = '<meta charset="utf-8">\n'
    assert s.startswith(first), 'expected the fragment to open with <meta charset="utf-8">'
    s = s[len(first):]
    # 3. <body> opens before the scripts that read document.body
    mark = "<script>window.addEventListener('error'"
    assert s.count(mark) == 1, 'expected one error-handler script'
    s = s.replace(mark, '</head>\n<body>\n' + mark, 1)
    return ('<!doctype html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + s.rstrip() + '\n</body>\n</html>\n')


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
    print(f'{path.relative_to(ROOT)}: {path.stat().st_size:,} bytes')


src = SRC.read_text(encoding='utf-8')
css = CSS.read_text(encoding='utf-8')
write(ROOT / 'index.html', page(src, css))

# the Flow Field test: its own title, the add-on after the prototype's last script
title = '<title>DUQ test · копия</title>'
assert src.count(title) == 1, 'expected the prototype title once'
flow = src.replace(title, '<title>DUQ Flow Field</title>', 1).rstrip() + '\n' + FLOW.read_text(encoding='utf-8')
write(ROOT / 'flow/index.html', page(flow, css))
