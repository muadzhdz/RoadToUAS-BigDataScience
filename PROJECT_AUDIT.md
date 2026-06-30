# Audit Proyek UAS Big Data Science
## Supermarket Sales Analysis

Dokumen ini menjelaskan fungsi setiap file di root repository, status kelengkapannya, hubungan antar file, dan pekerjaan final yang masih harus dilakukan sebelum dikumpulkan.

---

## 1. Kesimpulan Audit

Status umum: hampir lengkap untuk kebutuhan pengerjaan UAS, tetapi belum bisa disebut final 100% sampai dashboard dibuka dan diverifikasi langsung di Tableau Desktop.

Yang sudah kuat:
- Dataset sesuai brief: minimal 1.000 baris, punya dimensi waktu, kategorikal, dan numerik.
- Tahap 1 sampai Tahap 6 sudah terdokumentasi.
- Validasi data dengan Python sudah berhasil.
- Scenario AI CLI sudah tersedia.
- Draft laporan dan slide sudah bisa digenerate otomatis ke folder `luaran/`.
- Draft `.twb` XML sudah bisa digenerate tanpa error dan XML-nya well-formed.

Yang masih perlu verifikasi manual:
- File `.twb` hasil generator harus dibuka di Tableau Desktop untuk memastikan kompatibilitas Tableau, karena `.twb` Tableau punya struktur internal yang spesifik.
- File final `.twbx` tetap harus diekspor dari Tableau Desktop.
- Screenshot dashboard dan preprocessing harus diambil manual dari Tableau.
- Nama anggota, NIM, kelas, dan detail pengumpulan harus diisi.

---

## 2. Struktur Folder dan Fungsi

### Root Project

| File | Fungsi | Status |
|---|---|---|
| `scenario.md` | Instruksi utama untuk AI CLI. Menjelaskan objective, dataset, tahap 1-6, output, command, dan success criteria. | Lengkap, sudah dirapikan |
| `data_spec.yaml` | Metadata terstruktur untuk dataset: field, tipe data, calculated fields, validation rules, dan precomputed metrics. | Lengkap |
| `dashboard_spec.json` | Spesifikasi dashboard: sheet, chart type, quick filter, filter action, parameter, layout, dan styling. | Lengkap |
| `twb_generator.py` | Membuat draft XML `.twb` berdasarkan `data_spec.yaml` dan `dashboard_spec.json`. | Berjalan, perlu verifikasi Tableau |
| `report_generator.py` | Menggabungkan file Tahap 1-6 menjadi draft laporan Markdown di `luaran/`. | Berjalan |
| `slides_generator.py` | Membuat draft slide Markdown dari `SLIDE_READY.md` ke `luaran/`. | Berjalan |
| `run_all.py` | Menjalankan pipeline lokal: validasi, generate `.twb`, generate laporan, generate slide. | Berjalan |
| `PROJECT_AUDIT.md` | Dokumen audit ini. | Lengkap |

### Panduan dan Template

| File | Fungsi | Status |
|---|---|---|
| `PANDUAN_TABLEAU_LENGKAP.md` | Panduan pengerjaan Tableau dari import data sampai export `.twbx`. | Lengkap |
| `TABLEAU_WORKFLOW.md` | Workflow Tableau yang lebih granular, cocok dipakai saat praktik step-by-step. | Lengkap |
| `SCREENSHOT_GUIDE.md` | Daftar screenshot yang harus diambil, nama file, caption, dan lokasi di laporan. | Lengkap |
| `REPORT_READY.md` | Konten laporan siap pakai, bisa menjadi bahan utama Word/PDF. | Lengkap |
| `SLIDE_READY.md` | Konten presentasi 15 slide dengan catatan presenter. | Lengkap |
| `TEMPLATE_LAPORAN.md` | Struktur laporan maksimal 20 halaman. | Lengkap |
| `TEMPLATE_SLIDE.md` | Struktur slide maksimal 15 slide. | Lengkap |
| `PYTHON_SCRIPT.md` | Dokumentasi script validasi data dan cara menjalankannya. | Lengkap |

### Folder `laporan/`

| File | Fungsi | Status |
|---|---|---|
| `TAHAP1_Pemahaman_Masalah.md` | Domain, stakeholder, business question, sub-question, 5V, dan data lifecycle. | Lengkap |
| `TAHAP2_Profiling_Persiapan_Data.md` | Profil dataset, field, tipe data, dan persiapan Tableau. | Lengkap, sudah konsisten Tableau |
| `TAHAP3_Pembersihan_Data.md` | Dokumentasi cleaning: missing value, duplikasi, inkonsistensi, outlier, tipe data. | Lengkap |
| `TAHAP4_Analisis_Eksploratif.md` | EDA, analisis tren, produk, pelanggan, pembayaran, korelasi, dan insight. | Lengkap |
| `TAHAP5_Dashboard_Interaktif.md` | Spesifikasi dashboard, quick filter, filter action, parameter, layout, dan export. | Lengkap |
| `TAHAP6_Sintesis_Rekomendasi.md` | Jawaban business question, rekomendasi, keterbatasan, dan pertanyaan lanjutan. | Lengkap |

### Folder `datasets/`

| File/Folder | Fungsi | Status |
|---|---|---|
| `datasets/retail/supermarket_sales.csv` | Dataset utama proyek. | Valid |
| `datasets/SUMBER_DATASET.md` | Catatan sumber dataset dari beberapa domain. | Lengkap |
| `datasets/agriculture/coffee.csv` | Dataset alternatif domain agriculture. | Pendukung |
| `datasets/environment/beijing_pm25.csv` | Dataset alternatif domain environment. | Pendukung |
| `datasets/finance/stock_data.csv` | Dataset alternatif domain finance. | Pendukung |
| `datasets/health/healthcare_dataset.csv` | Dataset alternatif domain health. | Pendukung |
| `datasets/health/life_expectancy.csv` | Dataset alternatif domain health. | Pendukung |

### Folder `scripts/`

| File | Fungsi | Status |
|---|---|---|
| `scripts/validate_data.py` | Validasi dan analisis statistik lengkap. Menghasilkan output terminal dan `validation_report.txt`. | Berjalan |
| `scripts/validation_verify.py` | Validasi ringkas untuk membuktikan metrik utama cocok dengan precomputed metrics. | Berjalan |
| `scripts/validation_report.txt` | Output dari `validate_data.py`. | Ada setelah script dijalankan |

### Folder `luaran/`

| File | Fungsi | Status |
|---|---|---|
| `Supermarket_Sales_Dashboard.twb` | Draft XML Tableau Workbook. | Ada, well-formed XML, perlu dibuka di Tableau |
| `Laporan_UAS_BigData_Supermarket_Sales.md` | Draft laporan gabungan Tahap 1-6. | Ada |
| `Slide_UAS_BigData_Supermarket_Sales.md` | Draft konten slide. | Ada |
| `Supermarket_Sales_Dashboard.twbx` | File final packaged workbook. | Belum ada, harus export dari Tableau |

---

## 3. Hubungan Antar File

Alur kerja yang disarankan:

```text
datasets/retail/supermarket_sales.csv
  -> scripts/validation_verify.py
  -> data_spec.yaml
  -> dashboard_spec.json
  -> twb_generator.py
  -> luaran/Supermarket_Sales_Dashboard.twb
  -> Tableau Desktop
  -> luaran/Supermarket_Sales_Dashboard.twbx
```

Alur laporan:

```text
laporan/TAHAP1 sampai TAHAP6
  -> report_generator.py
  -> luaran/Laporan_UAS_BigData_Supermarket_Sales.md
  -> Word/LibreOffice/Pandoc
  -> PDF/DOCX final
```

Alur slide:

```text
SLIDE_READY.md
  -> slides_generator.py
  -> luaran/Slide_UAS_BigData_Supermarket_Sales.md
  -> PowerPoint/Canva/Google Slides
  -> PPTX/PDF final
```

Alur screenshot:

```text
Tableau Desktop
  -> SCREENSHOT_GUIDE.md
  -> masukkan gambar ke laporan dan slide
```

---

## 4. Checklist Final Sebelum Pengumpulan

| Item | Status Sekarang | Tindakan Final |
|---|---|---|
| Dataset valid | Selesai | Tidak perlu perubahan |
| Tahap 1-6 | Selesai | Review bahasa dan masukkan screenshot |
| Validasi Python | Selesai | Lampirkan output jika perlu |
| Draft `.twb` | Selesai | Buka di Tableau, perbaiki manual jika ada incompatibility |
| File `.twbx` | Belum final | Export dari Tableau Desktop sebagai Packaged Workbook |
| Laporan final | Draft tersedia | Copy ke Word/LibreOffice, insert screenshot, export PDF |
| Slide final | Draft tersedia | Buat visual slide, masukkan screenshot dashboard, export PPTX/PDF |
| Nama/NIM anggota | Placeholder | Isi data kelompok |
| Screenshot preprocessing | Belum ada | Ambil sesuai `SCREENSHOT_GUIDE.md` |
| Screenshot dashboard | Belum ada | Ambil dari dashboard Tableau final |

---

## 5. Penilaian Kelengkapan terhadap Brief Dosen

| Komponen Brief | Bukti File | Status |
|---|---|---|
| Pemahaman masalah dan konteks | `laporan/TAHAP1_Pemahaman_Masalah.md` | Terpenuhi |
| Profiling dan persiapan data | `laporan/TAHAP2_Profiling_Persiapan_Data.md` | Terpenuhi |
| Pembersihan data terdokumentasi | `laporan/TAHAP3_Pembersihan_Data.md`, `SCREENSHOT_GUIDE.md` | Terpenuhi, butuh screenshot aktual |
| Analisis eksploratif dan mendalam | `laporan/TAHAP4_Analisis_Eksploratif.md` | Terpenuhi |
| Minimal 3 calculated fields | `data_spec.yaml`, `PANDUAN_TABLEAU_LENGKAP.md` | Terpenuhi, ada 7 |
| Dashboard minimal 4 sheet | `dashboard_spec.json`, `TAHAP5_Dashboard_Interaktif.md` | Terpenuhi, ada 6 sheet |
| Minimal 2 quick filter | `dashboard_spec.json` | Terpenuhi |
| Minimal 1 filter action | `dashboard_spec.json` | Terpenuhi |
| Minimal 1 parameter | `dashboard_spec.json` | Terpenuhi |
| Sintesis dan rekomendasi | `laporan/TAHAP6_Sintesis_Rekomendasi.md` | Terpenuhi |
| Laporan maksimal 20 halaman | `luaran/Laporan_UAS_BigData_Supermarket_Sales.md` | Draft tersedia, perlu layout final |
| Slide maksimal 15 | `luaran/Slide_UAS_BigData_Supermarket_Sales.md` | Draft tersedia |
| File Tableau `.twbx` | `luaran/Supermarket_Sales_Dashboard.twb` | Draft `.twb` ada, `.twbx` belum diexport |

---

## 6. Risiko Teknis dan Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| `.twb` generator tidak 100% kompatibel dengan Tableau | Tableau bisa gagal membuka draft XML | Gunakan `dashboard_spec.json` sebagai blueprint dan bangun dashboard manual jika perlu |
| Screenshot belum ada | Nilai preprocessing/dashboard bisa turun | Ambil semua screenshot sesuai `SCREENSHOT_GUIDE.md` |
| Laporan terlalu panjang | Melanggar batas 20 halaman | Ringkas bagian panduan teknis ke lampiran |
| Slide terlalu padat | Presentasi kurang efektif | Pakai maksimal 15 slide, satu pesan utama per slide |
| Nama/NIM belum diisi | Administrasi tidak lengkap | Isi di semua template sebelum export |

---

## 7. Command yang Sudah Teruji

```bash
cd path/to/repository
python3 run_all.py
```

Hasil command:
- Validasi data berhasil.
- Draft `.twb` berhasil dibuat.
- Draft laporan berhasil dibuat.
- Draft slide berhasil dibuat.

---

## 8. Rekomendasi Final

Urutan kerja paling efektif:

1. Jalankan `python3 run_all.py`.
2. Buka `luaran/Supermarket_Sales_Dashboard.twb` di Tableau.
3. Jika Tableau tidak membuka file dengan sempurna, gunakan `dashboard_spec.json` dan `PANDUAN_TABLEAU_LENGKAP.md` untuk membuat dashboard manual.
4. Export dashboard final sebagai `luaran/Supermarket_Sales_Dashboard.twbx`.
5. Ambil screenshot sesuai `SCREENSHOT_GUIDE.md`.
6. Masukkan screenshot ke laporan dan slide.
7. Isi nama/NIM anggota.
8. Export laporan ke PDF/DOCX dan slide ke PPTX/PDF.
9. Kumpulkan satu folder final sesuai format dosen.
