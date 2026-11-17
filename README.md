# Vice City Theme Preservation

Permanent BetterDiscord and Vencord preservation of Discord's limited-time **Vice City** theme and **Home** button logo, with full [OldCord](https://github.com/milbits/oldcord/tree/main) compatibility.

## Features

- Full **Vice City** gradient and dark palette across chats, sidebars, settings, menus, and popouts (works permanently without Nitro).
- Custom **Vice City** Home button logo embedded offline directly inside the theme (no external CDN requests).
- Compatible with **[OldCord](https://github.com/milbits/oldcord/tree/main)** in any load order (fixes Settings/Menus colors, Activity & Active Now cards, notification badge outlines, and top bar overlay).
- Works across Ash, Dark, Onyx, and Light theme modes.

## Installation

### BetterDiscord
1. Download [`ViceCity-BetterDiscord.theme.css`](./ViceCity-BetterDiscord.theme.css).
2. Open Discord -> **User Settings** -> **BetterDiscord** -> **Themes** -> **Open Themes Folder**.
3. Place `ViceCity-BetterDiscord.theme.css` into the folder and enable **Vice City Theme Preservation**.

### Vencord / Vesktop
- **Online Themes** (recommended):
  Paste this link into **User Settings -> Vencord -> Themes -> Online Themes**:
  ```text
  https://raw.githubusercontent.com/t1murmat/Vice-City-Theme-Preservation/main/ViceCity-Vencord.theme.css
  ```
- **Local Themes**:
  Download [`ViceCity-Vencord.theme.css`](./ViceCity-Vencord.theme.css) and place it into **Open Themes Folder** (`%APPDATA%\Vencord\themes`).

## Build from Source

Requires Python 3.8+:

```bash
python src/build_theme.py
python src/verify_theme.py
```

## Disclaimer

This repository archives Discord's limited-time Rockstar Games Vice City theme and icon solely for personal preservation after the event ends. Original visual assets belong to Rockstar Games / Discord Inc.
