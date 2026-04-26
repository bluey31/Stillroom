# Stillroom — Chrome theme

Chrome supports unpacked theme loading for personal use. No Chrome Web Store
submission required.

## Install (unpacked · developer mode)

1. Open Chrome → `chrome://extensions`
2. Toggle **Developer mode** on (top-right)
3. Click **Load unpacked**
4. Select this `chrome/` folder
5. Theme applies immediately

The theme sits in your extensions list alongside regular extensions.

## The banner warning

Chrome shows a banner on each launch: "Disable developer mode extensions".
Don't click disable — click the `×` to dismiss. For personal use this is
just noise; the theme isn't doing anything privileged (no JavaScript, no
permissions, just colors).

## Update / remove

- **Tweaking colors:** edit `manifest.json`, then in `chrome://extensions`
  click the circular-arrow (reload) icon on the Stillroom tile.
- **Removing:** click **Remove** on the Stillroom tile.

## Surface mapping

Chrome's theming surface is narrower than VS Code's — about a dozen
addressable elements — but covers the parts that sit in peripheral vision
all day (window frame, toolbar, tabs, address bar, new-tab page).

### Frame and toolbar (the shell)

| Surface                | Pigment   | Hex       |
| ---------------------- | --------- | --------- |
| frame (window chrome)  | crust     | `#12100f` |
| toolbar                | mantle    | `#1a1715` |

Crust/mantle one stop apart — same discipline as the Slack sidebar. Frame
sits darkest against the OS desktop; toolbar lifts slightly where the
buttons live.

### Tabs

| Surface                         | Pigment    | Hex       |
| ------------------------------- | ---------- | --------- |
| active tab text                 | text       | `#d4cec8` |
| inactive tab text               | subtext 0  | `#a89f9b` |
| unfocused-window inactive text  | ovly 1     | `#807b77` |

Three tiers. Active tab leads, inactive tabs recede one stop, background-
window tabs recede further. Same hierarchy VS Code uses for editor tabs.

### Address bar (omnibox) and buttons

| Surface              | Pigment   | Hex       |
| -------------------- | --------- | --------- |
| omnibox background   | surf 0    | `#332f2c` |
| omnibox text         | text      | `#d4cec8` |
| button background    | surf 0    | `#332f2c` |
| toolbar button icon  | linen     | `#d2ceb9` |

Omnibox lifts one stop above the toolbar to read as an input field rather
than part of the bar itself.

### New-tab page

| Surface          | Pigment   | Hex       |
| ---------------- | --------- | --------- |
| ntp background   | base      | `#211e1c` |
| ntp text         | text      | `#d4cec8` |
| ntp link         | woad      | `#7d95b3` |
| ntp header       | lichen    | `#bab886` |

Matches the VS Code editor background exactly — opening a new tab should
feel continuous with your editor, not like a different surface.

## Tab group colors

Chrome's tab group colors are **hardcoded in the browser binary** and not
exposed to the theme manifest. The eight swatches (grey, blue, red, yellow,
green, pink, purple, cyan, orange) cannot be replaced with our palette.

The best workaround is to map semantic roles to the closest Chrome swatch:

| Chrome swatch | Closest pigment | Suggested use             |
| ------------- | --------------- | ------------------------- |
| yellow        | lichen          | main work, active focus   |
| blue          | woad            | reference, reading, docs  |
| green         | eucalyptus      | done, shipped, healthy    |
| red           | madder          | urgent, blocked           |
| orange        | terracotta      | review, in-progress       |
| purple        | damson          | held in reserve           |
| grey          | ovly 1          | archive, neutral          |
| cyan          | —               | (avoid — no palette match) |

Right-click a group name → Edit group → pick swatch to reassign.

## Things Chrome doesn't let us theme

- Individual tab group colors (hardcoded in the browser binary)
- Individual bookmark icons (come from favicons)
- Extension icon backgrounds (owned by each extension)
- The "Developer mode" banner itself
- DevTools (use DevTools → Settings → Appearance → dark, separately)
- Web page contents (that's site/user-agent styling, not a theme)

## DevTools pairing

Chrome themes don't touch DevTools. For a matching inspector, open DevTools
(`⌘⌥I`), click the gear, Appearance → Theme → Dark.
