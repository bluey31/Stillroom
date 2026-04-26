# Stillroom

A warm dark theme for Visual Studio Code. Natural dyes on warm ink — lichen, woad, madder, damson, eucalyptus, terracotta — calibrated for Python, MONAI, and the quieter side of the terminal.

## Install

**Development loop (recommended for trying it out)**

Clone this repo, open the folder in VS Code, press `F5`. A new Extension Development Host window opens with Stillroom available in the theme picker (`⌘K ⌘T`).

**Sideload**

Copy the folder into `~/.vscode/extensions/stillroom-1.0.4/` (or `%USERPROFILE%\.vscode\extensions\stillroom-1.0.4\` on Windows). If you had a previous version installed, delete `~/.vscode/extensions/extensions.json` before relaunching VS Code so the registry rescans. Pick Stillroom from `Code > Settings > Theme > Color Theme`.

**Package as `.vsix`**

```bash
npm install -g @vscode/vsce
vsce package
code --install-extension stillroom-1.0.4.vsix
```

## Palette

Six accents active in syntax, plus lichen and linen:

| Pigment      | Hex       | Role                             |
| ------------ | --------- | -------------------------------- |
| lichen ★     | `#bab886` | keywords (hero)                  |
| clay         | `#c9a99d` | types, annotations               |
| woad         | `#7d95b3` | functions, methods               |
| eucalyptus   | `#9bb596` | strings                          |
| terracotta   | `#d08a6e` | numbers, booleans, None          |
| madder       | `#c8716a` | errors, exceptions               |
| damson       | `#b4a5dc` | decorators, f-string interp      |
| linen        | `#d2ceb9` | variables, identifiers           |

Plus five documented-but-reserved pigments (frost, chalk, verdigris, slate, ember) available for non-syntax surfaces. See `palette.md` for the full 14-pigment reference.

The neutral ramp sits on warm ink (~H345°, chroma ~1.8). Base `#211e1c`. Operators, brackets, and punctuation are pulled into the neutral ramp so the dyed tokens carry the file.

## Philosophy

- **One hero, not seven.** Lichen leads. The others support.
- **Dyed, not painted.** Every accent traces to a natural pigment — woad (*Isatis tinctoria*), madder (*Rubia tinctorum*), lichen, damson (the plum, historically used for muted purple dye), eucalyptus, terracotta clay, clay.
- **Quiet scaffolding.** Operators, brackets, commas, and dots sit in the neutral ramp so they never fight the identifiers.
- **`self` as particle.** Treated as a grammatical marker, not a variable — pulled one ramp stop into subtext.
- **Types-heavy code stays readable.** Calibrated against PyTorch and MONAI internals, where 60% of the file can be type annotations.
- **Markdown headings as rainbow.** H1–H6 step through the six supporting accents (madder → terracotta → lichen → eucalyptus → woad → damson), giving documents a visible structure even at a squint.
- **No italics anywhere.** Emphasis comes through color and weight, never slant.

## Recommended companions

- **Editor font:** Berkeley Mono, JetBrains Mono, Commit Mono, or Fira Code.
- **Language server:** Pylance — the theme is calibrated around its semantic tokens (`selfParameter`, `magicFunction`, `*.decorator`).
- **Semantic highlighting:** on (default). If off, the theme still works via TextMate scopes.
- **Bracket pair colorization:** optional. The theme provides graduated grays rather than rainbow colors, preserving the operator-calm discipline.

## Variants

Currently a single variant. Future releases may ship under the family:

- `Stillroom · Steep` — current, dark.
- `Stillroom · Decant` — light (planned).
- `Stillroom · Mordant` — high-contrast (planned).

## License

MIT.
