import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TARGETS = (
    ROOT / "ViceCity-BetterDiscord.theme.css",
    ROOT / "ViceCity-Vencord.theme.css",
)


def verify(css_path: Path) -> None:
    """Validate CSS delimiter balance, embedded WebP icon, and theme metadata."""
    css = css_path.read_text(encoding="utf-8")

    stripped = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    stripped_no_url = re.sub(r'url\("data:[^"]+"\)', 'url("")', stripped)

    opens = stripped_no_url.count("{")
    closes = stripped_no_url.count("}")
    parens_o = stripped_no_url.count("(")
    parens_c = stripped_no_url.count(")")

    print(f"File: {css_path} ({len(css)} chars)")
    print(f"Braces: {{={opens}, }}={closes} (match={opens == closes})")
    print(f"Parens: (={parens_o}, )={parens_c} (match={parens_o == parens_c})")
    assert opens == closes, f"Brace mismatch: {opens} != {closes}"
    assert parens_o == parens_c, f"Paren mismatch: {parens_o} != {parens_c}"

    m = re.search(r'url\("data:image/webp;base64,([^"]+)"\)', css)
    assert m, "Missing embedded WebP data URI!"
    raw_webp = base64.b64decode(m.group(1))
    print("Decoded WebP bytes:", len(raw_webp), "header:", raw_webp[:12])
    assert raw_webp[:4] == b"RIFF" and raw_webp[8:12] == b"WEBP", "Invalid WebP header!"

    assert ".custom-theme-background" not in stripped_no_url, "Leftover .custom-theme-background selector!"
    assert css.startswith("/**\n * @name Vice City Theme Preservation\n"), "Unexpected JSDoc header!"
    assert " * @website https://github.com/t1murmat/Vice-City-Theme-Preservation\n" in css, "Missing @website metadata!"

    print("All syntax & asset checks PASSED!")


def main() -> None:
    targets = [Path(arg) for arg in sys.argv[1:]] if len(sys.argv) > 1 else list(DEFAULT_TARGETS)
    for target in targets:
        verify(target)


if __name__ == "__main__":
    main()
