#!/usr/bin/env python3
"""Build index.html — the published prototype — from the sources in src/.

src/duq-copy.html is the prototype as the Claude artifact «DUQ test · копия» holds it: a page fragment that links
src/tokens.css. index.html is that fragment made self-contained: the token sheet inlined, and the document shell
(doctype, head, body) written around it, with <body> opened before the scripts that need document.body.

    python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC, CSS, OUT = ROOT / 'src/duq-copy.html', ROOT / 'src/tokens.css', ROOT / 'index.html'

s = SRC.read_text(encoding='utf-8')
css = CSS.read_text(encoding='utf-8')

# 1. the token sheet goes inline in place of its link
LINK = '<link rel="stylesheet" href="tokens.css">'
assert s.count(LINK) == 1, 'expected one link to tokens.css'
s = s.replace(LINK, '<style>\n' + css + '\n</style>')

# 2. the fragment starts with its own charset; the shell below carries it instead
FIRST = '<meta charset="utf-8">\n'
assert s.startswith(FIRST), 'expected the fragment to open with <meta charset="utf-8">'
s = s[len(FIRST):]

# 3. <body> opens before the scripts that read document.body
MARK = "<script>window.addEventListener('error'"
assert s.count(MARK) == 1, 'expected one error-handler script'
s = s.replace(MARK, '</head>\n<body>\n' + MARK, 1)

doc = ('<!doctype html>\n<html lang="en">\n<head>\n'
       '<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       + s.rstrip() + '\n</body>\n</html>\n')
OUT.write_text(doc, encoding='utf-8')
print(f'{OUT.name}: {OUT.stat().st_size:,} bytes')
