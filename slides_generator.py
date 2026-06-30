#!/usr/bin/env python3
"""
Generate a presentation draft from the prepared slide content.

The output is Markdown with slide separators. It can be copied into PowerPoint,
Google Slides, Canva, or converted with Pandoc when available.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "SLIDE_READY.md"
OUTPUT = ROOT / "luaran" / "Slide_UAS_BigData_Supermarket_Sales.md"


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"Missing required file: {SOURCE}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    content = SOURCE.read_text(encoding="utf-8").strip()

    header = "\n".join(
        [
            "# Slide Presentasi UAS Big Data Science",
            "## Supermarket Sales Analysis",
            "",
            "**Anggota Kelompok:** [Nama 1 - NIM], [Nama 2 - NIM], [Nama 3 - NIM]",
            "**Tools:** Tableau Desktop",
            "",
            "---",
            "",
            "Catatan: file ini adalah draft konten presentasi maksimal 15 slide. "
            "Masukkan screenshot dashboard final dan rapikan visual di PowerPoint/Canva.",
            "",
            "---",
            "",
        ]
    )

    OUTPUT.write_text(header + content + "\n", encoding="utf-8")
    print(f"[OK] Slide draft generated: {OUTPUT}")


if __name__ == "__main__":
    main()
