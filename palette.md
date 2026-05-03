# Stillroom — Palette Reference

Warm ink · natural dyes · calibrated for code.

---

## The hero · one pigment leads the UI

| Pigment | Hex       | Role                                                        |
| ------- | --------- | ----------------------------------------------------------- |
| ecru    | #c0b490 | UI accent — cursor, active borders, badges, find match, focus |

Parchment straw. Carries the "you are here" weight in the workbench: cursor, active tab indicator, focused panel border, search match, badge fills, progress, primary buttons. Warm-buff rather than yellow-olive — sits beside the warm ink base without competing.

**Usage rule:** ecru fills *and* highlights at UI scale. Use it wherever the eye should land first in chrome. Don't use it for syntax — it's tuned to be calm enough for fills, which makes it too quiet for per-token emphasis.

## The syntax lead · one pigment leads the code

| Pigment | Hex       | Role                                                  |
| ------- | --------- | ----------------------------------------------------- |
| lichen  | #c4bd6e | keywords (class, def, for, in, return) |

The dyer's garden pressed into yellow-green. Every keyword draws its pigment from this pot. If someone sees a single screenshot of Stillroom *code*, this is the color they'll remember.

**Usage rule:** lichen is a *scanning color*, not a fill color. Works as a highlight on small tokens where the eye arrives briefly and moves on. Does not work as a large persistent surface — its yellow-olive hue carries a "highlighter pen" connotation at fill scale, which is why ecru holds the UI accent role instead.

---

## Supporting dyes · active in syntax

These pigments appear in the VS Code syntax map and carry the semantic weight of the theme, alongside lichen (hero) and waxed linen (tinted neutral).

| Pigment    | Hex       | Role                                                                 |
| ---------- | --------- | -------------------------------------------------------------------- |
| petal      | #b89aac   | types, annotations, class references                               |
| woad       | #7d95b3   | functions, methods, dict/object keys, links                        |
| glaze      | #8ba5aa   | decorators, f-string braces, magic methods, structural annotations |
| eucalyptus | #9ec48f   | strings, docstrings, regex                                         |
| ember      | #c29070   | numbers, booleans, `None`, `null`, escape sequences                |
| madder     | #c8716a   | errors, exceptions, TODO/FIXME, H1                                 |
| buff       | #cec4af   | import module names — yellow companion to woad                     |

## Supporting dyes · documented, held in reserve

These pigments are defined, named, and available for future surfaces (Chrome tab groups, Slack variants, Linear accents, extended language packs) but do not appear in the current VS Code syntax map. Restraint is deliberate — active syntax is sized at six accents plus lichen plus waxed linen, not fourteen.

| Pigment    | Hex       | Hue  | Register                                                    |
| ---------- | --------- | ---- | ----------------------------------------------------------- |
| frost      | #c8d0d8   | 215° | off-white, cool-blue tint                                 |
| chalk      | #cad2c5   | 125° | off-white, cool-green tint                                |
| verdigris  | #8ab3ad   | 175° | oxidised copper, teal                                     |
| pewter     | #8da8a4   | 190° | old tin, storm lantern glass                              |
| slate      | #9ba8c2   | 225° | weathered slate roof, dusty blue                          |
| damson     | #b4a5dc   | 255° | original plum-lavender, cooler than the current type lane |
| terracotta | #d08a6e   | 20°  | fired clay, brighter rust-orange                          |
| fig        | #a07a92   | 320° | ripe fig flesh, dusty plum between damson and petal       |
| clay       | #dba39c   | 20°  | warm pink-peach, original syntax dye for `self`/`cls`     |

## The tinted neutral · off the ramp

| Pigment     | Hex       | Role                              |
| ----------- | --------- | --------------------------------- |
| linen       | #c8c1a5   | variables, parameters, properties |

Not on the neutral ramp — deliberately tinted warm, with a beeswax cast rather than plain off-white, so identifiers carry a quiet material warmth without drifting into highlight color.

---

## Neutral ramp · warm ink H345°

Twelve stops from crust to text. All sit on the same warm-red-brown axis (H345° LCH, chroma ~1.8). Reads as "walnut, espresso, sepia ink" rather than blue-black or neutral charcoal.

| Stop      | Hex       | Role                                          |
| --------- | --------- | --------------------------------------------- |
| crust     | #12100f | darkest — sidebar, status bar, title bar      |
| mantle    | #1a1715 | slightly raised — panel, terminal, suggest widget |
| base      | #211e1c | editor background                             |
| surf 0    | #332f2c | borders, dividers                             |
| surf 1    | #46413d | hover state, active selection                 |
| surf 2    | #595450 | stronger surfaces, line numbers (active)      |
| ovly 0    | #6d6864 | comments                                      |
| ovly 1    | #807b77 | operators, punctuation, bracket dim           |
| ovly 2    | #948f8b | `self`, `cls`, `this` · muted identifiers     |
| subtxt 0  | #a89f9b | (reserved / muted identifiers)                |
| subtxt 1  | #bcb4b0 | secondary text, inactive tabs                 |
| text      | #d4cec8 | primary foreground                            |

---

## Surface usage rules

Cross-tool conventions to keep the palette coherent as it expands to new surfaces:

- **ecru** — UI accent. Persistent fills allowed (badges, active borders, progress, focused indicators). The "you are here" pigment in chrome.
- **lichen** — syntax keywords; per-token emphasis only. Never persistent fills.
- **woad** — function/method emphasis in syntax; persistent *selected* states in cool-leaning app UI where a tinted accent reads better than a neutral one.
- **madder** — persistent *urgent* states: errors, exceptions, unread mention badges, TODO/FIXME, destructive action confirmations.
- **eucalyptus** — persistent *healthy* states: strings, online presence, successful tests, git added.
- **glaze** — decorators and structural annotations (f-string braces, magic methods). Steps back, never leads.
- **petal** — types, class references, annotations. Quiet semantic register.
- **ember** — literal values (numbers, booleans, None) and their UI equivalents (tags, counts).
- **buff** — context lines, import module names. Yellow companion to woad — sits beside it without competing.

**On accents in cross-tool surfaces:** the "right" accent color is app-dependent, not palette-universal. Slack's active-pill wants high-contrast text/white over the dark base — a tinted accent like woad muddles against the warm-ink ramp. Linear's accent wants lichen. Chrome tab groups can only approximate via Chrome's fixed swatches. Each surface deserves its own evaluation; avoid forcing one accent to do the job across all contexts.

---

## The base undertone · warm ink

`#211e1c` decomposes to R=33, G=30, B=28 — a strictly descending RGB signature. That's the fingerprint of walnut, espresso, and sepia ink. Distinctly *not* a blue-black (Dracula, Tokyo Night, One Dark live there) and *not* a neutral charcoal (GitHub Dark).

The warmth is subtle by design. Against a bright monitor in a bright room it can read as "just dark." It earns its character in the conditions where code actually gets written — low ambient light, long sessions, eyes adapted.

---

## Variant namespace

Currently a single variant. Future releases may ship as a family, named after stages of the dyer's process:

- **Stillroom · Steep** — current, dark.
- **Stillroom · Decant** — light (planned).
- **Stillroom · Mordant** — high-contrast (planned).

Until a second variant ships, the current release is just *Stillroom* with no suffix.

---

## Cross-tool deployments

| Surface         | File                                  | Notes                                      |
| --------------- | ------------------------------------- | ------------------------------------------ |
| VS Code         | `themes/stillroom-color-theme.json`   | Primary surface. Full workbench + syntax.  |
| Zed             | `zed/themes/stillroom.json`           | Tree-sitter syntax map + workbench colors. |
| Ghostty         | `ghostty/stillroom`                   | ANSI 0–15 palette + cursor/selection.      |
| Slack (sidebar) | `slack.txt`                           | 8-slot custom theme string.                |
| Linear          | `linear.md`                           | Accent + background only.                  |
| Chrome          | `chrome/manifest.json`                | Frame, tabs, toolbar, omnibox, new tab.    |

---
