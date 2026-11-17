import argparse
import base64
import os
import shutil
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/t1murmat/Vice-City-Theme-Preservation"


@dataclass(frozen=True)
class ThemeVariant:
    """Target theme output definition."""

    filename: str
    author: str
    description: str
    install_subdir: tuple[str, ...]
    extra_css: str = ""


VARIANTS: dict[str, ThemeVariant] = {
    "betterdiscord": ThemeVariant(
        filename="ViceCity-BetterDiscord.theme.css",
        author="Rockstar Games / Discord (Saved for BetterDiscord)",
        description=(
            "Permanent BetterDiscord preservation of Discord's limited-time Vice City "
            "client theme and app icon (home button logo), including OldCord compatibility."
        ),
        install_subdir=("BetterDiscord", "themes"),
    ),
    "vencord": ThemeVariant(
        filename="ViceCity-Vencord.theme.css",
        author="Rockstar Games / Discord (Saved for Vencord)",
        description=(
            "Permanent Vencord & Vesktop preservation of Discord's limited-time Vice City "
            "client theme and Home button icon, including OldCord compatibility."
        ),
        install_subdir=("Vencord", "themes"),
        extra_css=(
            "\n/* Vencord UI & Addon Cards */\n"
            ":is(html.theme-dark, html.theme-darker, html.theme-midnight, .theme-dark, .theme-darker, .theme-midnight):not(#_):not(.theme-light) :is(.vc-addon-card, .vc-card-base) {\n"
            "    background-color: var(--card-background-default);\n"
            "    border-color: var(--border-subtle);\n"
            "}\n"
        ),
    ),
}


def render_header(variant: ThemeVariant) -> str:
    """Format a BetterDiscord/Vencord-compatible JSDoc metadata block."""
    return (
        "/**\n"
        " * @name Vice City Theme Preservation\n"
        f" * @author {variant.author}\n"
        " * @version 1.0.0\n"
        f" * @description {variant.description}\n"
        f" * @source {REPO_URL}\n"
        f" * @website {REPO_URL}\n"
        " */"
    )


def install_to_appdata(src_path: Path, subdir: tuple[str, ...]) -> Path:
    """Copy a built theme file into %APPDATA%\\<subdir>\\<filename>."""
    appdata = os.environ.get("APPDATA")
    if not appdata:
        raise RuntimeError("APPDATA environment variable is not set.")
    dest_dir = Path(appdata).joinpath(*subdir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src_path.name
    shutil.copyfile(src_path, dest)
    print(f"Installed: {dest}")
    return dest


def build_themes(install_bd: bool = False, install_vencord: bool = False) -> dict[str, Path]:
    """Assemble BetterDiscord and Vencord theme files from shared source assets."""
    icon_b64 = base64.b64encode((ROOT / "assets" / "vice_city_icon.webp").read_bytes()).decode("ascii")
    tokens_css = (ROOT / "src" / "tokens.css").read_text(encoding="utf-8")
    template = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")

    outputs: dict[str, Path] = {}
    install_flags = {"betterdiscord": install_bd, "vencord": install_vencord}

    for key, variant in VARIANTS.items():
        css = (
            template.replace("__HEADER_BLOCK__", render_header(variant))
            .replace("__TOKENS_CSS__", tokens_css)
            .replace("__ICON_B64__", icon_b64)
        )
        if variant.extra_css:
            css = css.rstrip() + "\n" + variant.extra_css.strip("\n") + "\n"

        out_path = ROOT / variant.filename
        with out_path.open("w", encoding="utf-8", newline="\n") as f:
            f.write(css)
        print(f"Wrote: {out_path} ({out_path.stat().st_size} bytes)")
        outputs[key] = out_path

        if install_flags[key]:
            install_to_appdata(out_path, variant.install_subdir)

    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build ViceCity-BetterDiscord.theme.css and ViceCity-Vencord.theme.css."
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Also copy ViceCity-BetterDiscord.theme.css into %%APPDATA%%\\BetterDiscord\\themes.",
    )
    parser.add_argument(
        "--install-vencord",
        action="store_true",
        help="Also copy ViceCity-Vencord.theme.css into %%APPDATA%%\\Vencord\\themes.",
    )
    args = parser.parse_args()
    build_themes(install_bd=args.install, install_vencord=args.install_vencord)


if __name__ == "__main__":
    main()
