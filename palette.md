# Stillroom — Palette Reference

Warm ink · natural dyes · calibrated for code.

---

## The hero · one pigment leads

| Pigment | Hex       | Role                          |
| ------- | --------- | ----------------------------- |
| lichen  | #c4bd6e | keywords (class, def, for, in, return) |

The dyer's garden pressed into yellow-green. Every keyword draws its pigment from this pot. If someone sees a single screenshot of Stillroom, this is the color they'll remember.

**Usage rule:** lichen is a *scanning color*, not a fill color. Works as a highlight on small tokens where the eye arrives briefly and moves on. Does not work as a large persistent surface — its yellow-olive hue carries a "highlighter pen" connotation at fill scale.

---

## Supporting dyes · active in syntax

These six pigments appear in the VS Code syntax map and carry the semantic weight of the theme, alongside lichen (hero) and waxed linen (tinted neutral).

| Pigment          | Hex       | Role                                                |
| ---------------- | --------- | --------------------------------------------------- |
| clay             | #d4a894 | decorators, imports, f-string braces, `self`, `cls` |
| petal            | #a897a6 | types, annotations, class references                |
| woad             | #7d95b3 | 215° | older indigo-blue, cooler than the current callable blue |
| eucalyptus       | #a8c49a | strings, docstrings, regex                          |
| ember            | #c29070 | numbers, booleans, `None`, `null`, `undefined`       |
| madder           | #c8716a | errors, exceptions, warnings                        |

## Supporting dyes · documented, held in reserve

These pigments are defined, named, and available for future surfaces (Chrome tab groups, Slack variants, Linear accents, extended language packs) but do not appear in the current VS Code syntax map. Restraint is deliberate — active syntax is sized at six accents plus lichen plus waxed linen, not fourteen.

| Pigment   | Hex       | Hue  | Register                            |
| --------- | --------- | ---- | ----------------------------------- |
| frost     | #c8d0d8 | 215° | off-white, cool-blue tint           |
| chalk     | #cad2c5 | 125° | off-white, cool-green tint          |
| verdigris | #8ab3ad | 175° | oxidised copper, teal               |
| pewter    | #8da8a4 | 190° | old tin, storm lantern glass        |
| glaze     | #8ba5aa | ---- | light blue glaze                    |
| slate     | #9ba8c2 | 225° | weathered slate roof, dusty blue    |
| ecru      | #c0b490 | 48°  | parchment straw, warm buff          |
| damson    | #b4a5dc | 255° | original plum-lavender, cooler than the current type lane |
| terracotta| #d08a6e | 20°  | fired clay, brighter rust-orange    |

## The tinted neutral · off the ramp

| Pigment     | Hex       | Role                              |
| ----------- | --------- | --------------------------------- |
| waxed linen | #c8c1a5 | variables, parameters, properties |

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
| ovly 2    | #948f8b | (reserved / tertiary text)                    |
| subtxt 0  | #a89f9b | `self`, `cls`, `this` · muted identifiers     |
| subtxt 1  | #bcb4b0 | secondary text, inactive tabs                 |
| text      | #d4cec8 | primary foreground                            |

---

## Surface usage rules

Cross-tool conventions to keep the palette coherent as it expands to new surfaces:

- **lichen** — ephemeral highlights, per-token emphasis only. Never persistent fills.
- **woad** — persistent *selected* states in apps with cool-leaning UI (Linear accent, Slack active pill). First choice for "you are here" when one must be picked, but not universal — some apps want a warmer selection color.
- **madder** — persistent *urgent* states (errors, unread mention badges, destructive action confirmations).
- **eucalyptus** — persistent *healthy* states (strings, online presence, successful tests, git added).
- **damson** — rare/semantic markers (decorators, f-string interp, renamed git files). Held in reserve.
- **terracotta** — literal values (numbers, booleans, None) and their UI equivalents (tags, counts).
- **clay** — types and structural annotations. Steps back, never leads.

**On accents in cross-tool surfaces:** the "right" accent color is app-dependent, not palette-universal. Slack's active-pill wants woad. Linear's accent wants clay. Chrome tab groups can only approximate via Chrome's fixed swatches. Each surface deserves its own evaluation; avoid forcing one accent to do the job across all contexts.

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
| Ghostty         | `ghostty/stillroom`                   | ANSI 0–15 palette + cursor/selection.      |
| Slack (sidebar) | `slack.txt`                           | 8-slot custom theme string.                |
| Linear          | `linear.md`                           | Accent + background only.                  |
| Chrome          | `chrome/manifest.json`                | Frame, tabs, toolbar, omnibox, new tab.    |

---
