# Proyek Analisis Data Penjualan Supermarket — UAS Big Data Science

Proyek ini menganalisis data transaksi penjualan supermarket sebanyak 1.000 baris dan 17 kolom menggunakan **Tableau Desktop** dan **Python**. Seluruh alur kerja — mulai dari validasi data, pembuatan workbook Tableau, hingga penyusunan draft laporan dan presentasi — diotomatisasi melalui skrip Python yang terstruktur dalam repositori ini.

### Identitas Kelompok

- Mu'adz Hudzaifah (24903460014)
- Alhaq Sabilil Izati (24903460012)
- Arfan Ghifari (24903460016)
- Dosen Pengampu: Nur Choiriyati, S.Kom., M.T.

---

### Struktur Direktori

| Folder / File | Fungsi |
|---|---|
| **Scripts/** | Skrip Python untuk otomatisasi pipeline analisis |
| **markdown/** | Spesifikasi teknis, panduan Tableau, draft konten laporan & slide |
| **stage_drafts/** | Draft laporan per tahap (Tahap 1–6) sesuai format penilaian |
| **dataset/** | Dataset mentah `supermarket_sales.csv` dan dokumentasi sumber |
| **output_drafts/** | Hasil generate pipeline (.twb, laporan markdown, slide markdown) |
| **run_all.py** | Entry point untuk menjalankan seluruh pipeline |

#### Scripts/

| Skrip | Kegunaan |
|---|---|
| **validation_verify.py** | Validasi statistik dataset (row count, missing values, duplicates, city metrics, product lines, dll.) |
| **twb_generator.py** | Generator XML workbook Tableau (.twb) berdasarkan spesifikasi JSON/YAML |
| **report_generator.py** | Menggabungkan draft tiap tahap menjadi satu dokumen laporan markdown |
| **slides_generator.py** | Menggabungkan draft konten presentasi menjadi satu file slide markdown |
| build_with_boxplot.py | *(opsional, Windows-only)* Injeksi calculated fields & box plot ke .twb |
| final_audit.py | *(opsional, Windows-only)* Audit internal struktur workbook Tableau |

#### markdown/

| Berkas | Kegunaan |
|---|---|
| **scenario.md** | Panduan pertanyaan bisnis dan alur pengerjaan Tahap 1–6 |
| **dashboard_spec.json** | Definisi layout, sheet, parameter, dan filter action dashboard |
| **data_spec.yaml** | Spesifikasi field dataset dan calculated fields |
| **PANDUAN_TABLEAU_LENGKAP.md** / **TABLEAU_WORKFLOW.md** | Dokumentasi langkah teknis Tableau |
| **REPORT_READY.md** / **SLIDE_READY.md** | Konten akhir laporan dan slide presentasi |
| **TEMPLATE_LAPORAN.md** / **TEMPLATE_SLIDE.md** | Kerangka laporan dan slide UAS |
| **SCREENSHOT_GUIDE.md** | Panduan screenshot untuk laporan |
| **PROJECT_AUDIT.md** / **PYTHON_SCRIPT.md** | Catatan audit proyek dan referensi teknis |

---

### Pipeline

Pipeline otomatis menjalankan: validasi data → generate workbook Tableau → kompilasi laporan → kompilasi slide.

```bash
pip install pyyaml
python run_all.py
```

> **Catatan:** Di Linux, gunakan `python3 run_all.py`.

Output akan tersimpan di folder **output_drafts/**:
- `Supermarket_Sales_Dashboard.twb` — workbook Tableau
- `Laporan_UAS_BigData_Supermarket_Sales.md` — draft laporan
- `Slide_UAS_BigData_Supermarket_Sales.md` — draft slide presentasi
