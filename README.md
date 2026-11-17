# Vice City Theme Preservation

Permanent BetterDiscord and Vencord preservation of Discord's limited-time **Vice City (`HEXAGON`)** client theme and custom app icon (Home button logo), including full **OldCord** compatibility fixes.

## Features

- **Full Vice City (`HEXAGON`) Palette & Gradients**: Preserves the 4-stop gradient (`#4645ff` -> `#af01f3` -> `#ff6698` -> `#f89a03`) and OKLAB color-mix surface, text, border, input, menu, modal, and button tokens permanently without requiring Discord's temporary `.custom-theme-background` flag or Nitro.
- **Offline Embedded Home Icon**: Embeds the limited-time Vice City Home button icon (`assets/vice_city_icon.webp`) directly as an inline base64 WebP data URI so it works offline without relying on external CDN links or triggering CSP blocks.
- **Settings, Context Menus & Modals Parity**: Preserves the deep indigo-navy surface palette (`--primary-600..800` / `--background-surface-*` / `.disable-adaptive-theme`) across **Ash** (`.theme-dark`), **Dark** (`.theme-darker`), **Onyx** (`.theme-midnight`), Light mode fallback (`.theme-light`), and High Contrast mode.
- **OldCord (`OldCord.theme.css`) Compatibility**:
  - Works in any theme load order (OldCord loaded before or after Vice City).
  - Keeps User Settings, Context Menus, and Popouts in Vice City's navy palette instead of OldCord's default gray `.theme-darker` / `.theme-midnight` overrides.
  - Applies Vice City gradients to Member List **Activity** cards (`.container_g7esM5` and `.popoutContentWrapper_R0WNX5`), **Active Now** column and cards (`.nowPlayingColumn_zrUwGA`, `.container_GNEh_C`, `.wrapper_o3hXTo`, `.section_o3hXTo`, `.emptyCard_-7KzVR`), Vencord **BetterFolders** sidebars (`.vc-betterFolders-sidebar`), and forum controls/open threads (`.sortDropdown_BkGrJJ`, `.tagsButton_BkGrJJ`, `.isOpen_SOY5H6`, `.isOpen_x1LvFB`).
  - Removes the 5px dark border and halo around red unread notification badges (`.lowerBadge_hqZPsU`, `.upperBadge_hqZPsU`) on servers, folders, and unread DM friend avatars.
  - Keeps OldCord's `.systemBar_3zSH5d` overlay transparent in Settings so it never covers the top-left `DISCORD` wordmark or paints an extra strip across the top of the window.

## Installation

### BetterDiscord
1. Download [`ViceCity.theme.css`](./ViceCity.theme.css).
2. Open Discord -> **User Settings** -> **BetterDiscord** -> **Themes** -> **Open Themes Folder** (`%APPDATA%\BetterDiscord\themes` on Windows).
3. Move `ViceCity.theme.css` into your Themes folder and enable **Vice City Theme Preservation**.

### Vencord / Vesktop
Choose **any** of the three Vencord methods:

- **Option A — Online Themes (auto-loaded from GitHub)**:
  1. Open Discord -> **User Settings** -> **Vencord** -> **Themes** -> **Online Themes**.
  2. Paste this direct link on a new line:
     ```text
     https://raw.githubusercontent.com/t1murmat/Vice-City-Theme-Preservation/main/ViceCity-Vencord.theme.css
     ```
- **Option B — Local Themes**:
  1. Download [`ViceCity-Vencord.theme.css`](./ViceCity-Vencord.theme.css).
  2. Open **User Settings** -> **Vencord** -> **Themes** -> **Open Themes Folder** (`%APPDATA%\Vencord\themes` on Windows), or click **Upload Theme**.
  3. Place `ViceCity-Vencord.theme.css` there and enable **Vice City Theme Preservation**.
- **Option C — QuickCSS**:
  Paste the single import line into **Vencord -> QuickCSS** (works alongside OldCord):
  ```css
  @import url("https://raw.githubusercontent.com/t1murmat/Vice-City-Theme-Preservation/main/ViceCity-Vencord.theme.css");
  ```

## Repository Structure

```text
Vice-City-Theme-Preservation/
├── ViceCity.theme.css          # BetterDiscord theme (single self-contained CSS file)
├── ViceCity-Vencord.theme.css  # Vencord / Vesktop theme (with Vencord card & BetterFolders rules)
├── assets/
│   └── vice_city_icon.webp     # Embedded Home button icon (8,472 bytes WebP)
├── src/
│   ├── build_theme.py          # Assembles both BetterDiscord & Vencord variants from shared sources
│   ├── styles.css              # Core Vice City variables, component overrides & OldCord compatibility rules
│   ├── tokens.css              # Extracted OKLAB color-mix tokens, legacy aliases & Light/Profile rules
│   └── verify_theme.py         # Verifies CSS delimiter balance, embedded WebP integrity & metadata headers
└── README.md
```

## Building & Verifying from Source

Requires Python 3.8+ (no external packages needed):

```bash
# Rebuild ./ViceCity.theme.css and ./ViceCity-Vencord.theme.css
python src/build_theme.py

# Also install into BetterDiscord and/or Vencord local themes folders (Windows)
python src/build_theme.py --install
python src/build_theme.py --install-vencord

# Verify brace/parenthesis balance, embedded WebP icon & header metadata for both files
python src/verify_theme.py
```

## Disclaimer

This repository archives Discord's promotional Rockstar Games / Vice City (`HEXAGON`) color theme and app icon asset solely for personal BetterDiscord and Vencord preservation after the limited-time event expires. All original visual assets belong to Rockstar Games / Discord Inc.
