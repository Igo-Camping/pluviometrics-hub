"""Re-trace the three White logo variants using their alpha channel.

vtracer in binary mode treats white as background, so white-on-transparent
PNGs produce empty SVGs. We rasterise the alpha channel into a black
silhouette on white, trace that, then re-colour the black fill to white.
"""
from pathlib import Path
import re
import sys
import tempfile

from PIL import Image
import vtracer

# Logos are very high-resolution (>178MP); they're trusted local files.
Image.MAX_IMAGE_PIXELS = None

LOGO_DIR = Path(__file__).resolve().parent.parent / "Assets" / "Logos"

WHITE_LOGOS = [
    "AtmosWhite_PNG-01 (1).png",
    "PluviomWhite_PNG-01 (1).png",
    "PluviomShortWhite_PNG-01.png",
]

# Match black fills/strokes vtracer emits (it uses #xxxxxx, lower-case).
HEX_RE = re.compile(r'(fill|stroke)="#000000"')


def alpha_to_silhouette(src: Path, dst: Path) -> None:
    """Write a 1-bit-style PNG: opaque pixels become black, rest white."""
    img = Image.open(src).convert("RGBA")
    alpha = img.split()[-1]
    # Pixels with alpha > 32 are "ink"; everything else is background.
    silhouette = alpha.point(lambda v: 0 if v > 32 else 255).convert("L")
    silhouette.convert("RGB").save(dst, format="PNG")


def trace_and_recolor(src_png: Path, dst_svg: Path) -> None:
    with tempfile.TemporaryDirectory() as td:
        sil = Path(td) / "silhouette.png"
        alpha_to_silhouette(src_png, sil)
        vtracer.convert_image_to_svg_py(
            str(sil),
            str(dst_svg),
            colormode="binary",
            hierarchical="stacked",
            mode="spline",
            filter_speckle=4,
            corner_threshold=60,
            length_threshold=4.0,
            max_iterations=10,
            splice_threshold=45,
            path_precision=3,
        )
    text = dst_svg.read_text(encoding="utf-8")
    text = HEX_RE.sub(r'\1="#ffffff"', text)
    dst_svg.write_text(text, encoding="utf-8")


def main() -> int:
    fails: list[tuple[str, str]] = []
    for name in WHITE_LOGOS:
        src = LOGO_DIR / name
        dst = src.with_suffix(".svg")
        if not src.exists():
            fails.append((name, "missing source"))
            continue
        try:
            trace_and_recolor(src, dst)
            print(f"[white] {name} -> {dst.name} ({dst.stat().st_size/1024:.1f} KB)")
        except Exception as e:  # noqa: BLE001
            fails.append((name, repr(e)))
    if fails:
        for n, e in fails:
            print(f"FAIL {n}: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
