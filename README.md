# DUQ — prototype

Interactive prototype of the DUQ prediction market.

- Live: https://nshanh.github.io/DUQ/
- Current version: v151

## Files

| file | what it is |
| --- | --- |
| `index.html` | the published prototype: one self-contained page, the token sheet inlined. GitHub Pages serves it. |
| `src/duq-copy.html` | the source — the prototype as the Claude artifact «DUQ test · копия» holds it. A page fragment (no doctype or body of its own) that links `tokens.css`. |
| `src/tokens.css` | the DUQ Design System tokens, generated from the design-system artifact (Figma «DUQ Design System v2»). Not edited by hand. |
| `build.py` | builds `index.html` from `src/`: inlines the tokens and writes the document shell around the fragment. |

## Updating

1. Put the new `duq-copy.html` (and `tokens.css`, if the tokens changed) into `src/`.
2. Run `python3 build.py`.
3. Commit `src/` and `index.html` together and push; Pages rebuilds in about a minute.
