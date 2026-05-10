"""Batch-vectorize logos in Assets/Logos/ to SVG using vtracer.

Single-color (Black/White variants + uppercase originals) -> binary trace.
Color logos (Logo_*.png) -> multi-color trace, ~8 colors.
"""
from pathlib import Path
import sys
import vtracer

LOGO_DIR = Path(__file__).resolve().parent.parent / "Assets" / "Logos"

# Files where the logo is a single solid colour on a transparent/white background.
SINGLE_COLOR = [
    "AtmosBlack_PNG-01.png",
    "AtmosWhite_PNG-01 (1).png",
    "PluviomBlack_PNG-01.png",
    "PluviomWhite_PNG-01 (1).png",
    "PluviomShortBlack_PNG-01.png",
    "PluviomShortWhite_PNG-01.png",
    "ATMOS.png",
    "PLUVIOMETRICS.png",
    "STORMGAUGE.png",
]

# Full-colour brand logos.
COLOR = [
    "Logo_Atmos.png",
    "Logo_Pluviometrics.png",
    "Logo_Stormgauge.png",
]


def trace_binary(src: Path, dst: Path) -> None:
    vtracer.convert_image_to_svg_py(
        str(src),
        str(dst),
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


def trace_color(src: Path, dst: Path) -> None:
    vtracer.convert_image_to_svg_py(
        str(src),
        str(dst),
        colormode="color",
        hierarchical="stacked",
        mode="spline",
        filter_speckle=4,
        color_precision=6,        # ~6 bits/channel quantization, ~8 effective layers
        layer_difference=16,
        corner_threshold=60,
        length_threshold=4.0,
        max_iterations=10,
        splice_threshold=45,
        path_precision=3,
    )


def main() -> int:
    failures: list[tuple[str, str]] = []
    successes: list[tuple[str, int, int]] = []

    for name in SINGLE_COLOR:
        src = LOGO_DIR / name
        dst = src.with_suffix(".svg")
        if not src.exists():
            failures.append((name, "missing source"))
            continue
        try:
            trace_binary(src, dst)
            successes.append((dst.name, src.stat().st_size, dst.stat().st_size))
            print(f"[binary] {name} -> {dst.name}")
        except Exception as e:  # noqa: BLE001
            failures.append((name, repr(e)))

    for name in COLOR:
        src = LOGO_DIR / name
        dst = src.with_suffix(".svg")
        if not src.exists():
            failures.append((name, "missing source"))
            continue
        try:
            trace_color(src, dst)
            successes.append((dst.name, src.stat().st_size, dst.stat().st_size))
            print(f"[color]  {name} -> {dst.name}")
        except Exception as e:  # noqa: BLE001
            failures.append((name, repr(e)))

    print("\nResults:")
    print(f"  {'file':<40} {'png (KB)':>10} {'svg (KB)':>10}")
    for name, png, svg in successes:
        print(f"  {name:<40} {png/1024:>10.1f} {svg/1024:>10.1f}")
    if failures:
        print("\nFailures:")
        for n, e in failures:
            print(f"  {n}: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
