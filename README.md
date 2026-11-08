# DUQ — prototype

Interactive prototype of the DUQ prediction market.

- Live: https://nshanh.github.io/DUQ/
- Current version: v187 — no left side menu at any width; the signed-in hero is a row of three — where the crowd goes on the banner's market (a gauge and the last hour's bets), the banner, a head-to-head as a photo duel (the match photo cut on a diagonal into the teams' colours) taking the prototype's three head-to-heads in turn, both with the market cards' 24 px padding — with this week's markets running by under it on chips in the market cards' own ground; the hero's cards have a slightly brighter edge in the dark theme; every card, the hero carousel included, in the look of Liquid Glass Medium (plain CSS); market cards on Figma Home / Market card's spacing; market cards and market rows with a plain 28 px radius, the hero carousel's cards a plain 38 px; the hero carousel's shadow fades out inside its stage; in the light theme the cards' shadow and dark edge a little softer (about a quarter off); the dark theme graphite with a touch of blue: the page #07090f, the cards #121621 at 85 %; the dark landing with a soft blue light behind the headline; the category row stays pinned right under the top bar, both on a frosted ground; an open market's body on Figma Outcome Body (20 on every side); the charts carry the duq wordmark at 6 % (Figma Event Chart)
- Test page, the landing background as KokonutUI Flow Field: https://nshanh.github.io/DUQ/flow/

## Files

| file | what it is |
| --- | --- |
| `index.html` | the published prototype: one self-contained page, the token sheet inlined. GitHub Pages serves it. |
| `src/duq-copy.html` | the source — the prototype as the Claude artifact «DUQ test · копия» holds it. A page fragment (no doctype or body of its own) that links `tokens.css`. |
| `src/tokens.css` | the DUQ Design System tokens, generated from the design-system artifact (Figma «DUQ Design System v2»). Not edited by hand. |
| `flow/index.html` | the Flow Field test: the same prototype with the landing background swapped for a port of the KokonutUI «Flow Field» (colours from the tokens; a Tune panel compares it with the current background). |
| `src/flow-addon.html` | the Flow Field port and its Tune panel, appended to the prototype for `flow/index.html`. |
| `build.py` | builds `index.html` and `flow/index.html` from `src/`: inlines the tokens and writes the document shell around the fragment. |

## Updating

1. Put the new `duq-copy.html` (and `tokens.css`, if the tokens changed) into `src/`.
2. Run `python3 build.py`.
3. Commit `src/`, `index.html` and `flow/index.html` together and push; Pages rebuilds in about a minute.
