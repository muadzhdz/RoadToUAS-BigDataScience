#!/usr/bin/env python3
"""
Generate a consolidated report draft from the existing UAS stage files.

The output is Markdown so it can be reviewed, edited, and converted to DOCX/PDF
with Pandoc or copied into Word/LibreOffice.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "luaran" / "Laporan_UAS_BigData_Supermarket_Sales.md"

STAGE_FILES = [
    ROOT / "laporan" / "TAHAP1_Pemahaman_Masalah.md",
    ROOT / "laporan" / "TAHAP2_Profiling_Persiapan_Data.md",
    ROOT / "laporan" / "TAHAP3_Pembersihan_Data.md",
    ROOT / "laporan" / "TAHAP4_Analisis_Eksploratif.md",
    ROOT / "laporan" / "TAHAP5_Dashboard_Interaktif.md",
    ROOT / "laporan" / "TAHAP6_Sintesis_Rekomendasi.md",
]


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8").strip()


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    parts = [
        "# Laporan UAS Big Data Science",
        "## Analisis Data Penjualan Supermarket Menggunakan Tableau",
        "",
        "**Anggota Kelompok:** Mu'adz Hudzaifah (24903460014), Alhaq Sabilil Izati (24903460012), Arfan Ghifari",
        "**Dosen:** Nur Choiriyati",
        "**Dataset:** Supermarket Sales",
        "**Tools:** Tableau Desktop, Python",
        "",
        "---",
        "",
        "## Catatan Penyusunan",
        "",
        "Dokumen ini adalah draft gabungan dari seluruh tahap. Sebelum dikumpulkan, "
        "masukkan screenshot Tableau sesuai SCREENSHOT_GUIDE.md, isi nama anggota, "
        "rapikan nomor gambar, dan pastikan total halaman maksimal 20 halaman.",
        "",
        "---",
    ]

    for stage_file in STAGE_FILES:
        parts.extend(["", read_text(stage_file), "", "---"])

    parts.extend(
        [
            "",
            "## Lampiran",
            "",
            "- Screenshot preprocessing dan dashboard.",
            "- File Tableau Packaged Workbook (.twbx).",
            "- Dataset mentah supermarket_sales.csv.",
            "- Output validasi scripts/validation_report.txt.",
            "",
        ]
    )

    OUTPUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"[OK] Report draft generated: {OUTPUT}")


if __name__ == "__main__":
    main()
