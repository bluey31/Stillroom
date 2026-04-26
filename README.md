# Stillroom

A warm dark theme for Visual Studio Code. Natural dyes on warm ink — lichen, woad, madder, damson, eucalyptus, terracotta — calibrated for Python, MONAI, and the quieter side of the terminal.

## Install

**Development loop (recommended for trying it out)**

Clone this repo, open the folder in VS Code, press `F5`. A new Extension Development Host window opens with Stillroom available in the theme picker (`⌘K ⌘T`).

**Sideload**

Copy the folder into `~/.vscode/extensions/stillroom/`. If you had a previous version installed, delete `~/.vscode/extensions/extensions.json` before relaunching VS Code so the registry rescans. Pick Stillroom from `Code > Settings > Theme > Color Theme`.

**Package as `.vsix`**

```bash
npm install -g @vscode/vsce
vsce package
code --install-extension stillroom.vsix
```

## Variants

Currently a single variant. Future releases may ship under the family:

- `Stillroom · Steep` — current, dark.
- `Stillroom · Decant` — light (planned).
- `Stillroom · Mordant` — high-contrast (planned).

