<div align="center">
  <h1>RoadToUAS-BigDataScience</h1>
</div>

AI CLI workflow for a Big Data Science final project, built around a Tableau-based **Supermarket Sales Analysis** case study.

Repository ini berisi project UAS mata kuliah Big Data Science dengan pendekatan yang sedikit berbeda: bukan hanya membuat dashboard Tableau, tetapi juga membangun alur kerja yang bisa dibaca dan dieksekusi oleh AI CLI seperti Codex, OpenCode, Gemini CLI, Antigravity CLI, Kiro CLI, atau tool sejenis.

Konsepnya sederhana: AI CLI tidak hanya menerima prompt lepas seperti chatbot, tetapi membaca struktur project, dataset, skenario, spesifikasi dashboard, script validasi, dan dokumen laporan. Dengan begitu, AI bisa bekerja lebih kontekstual, konsisten, dan bisa membantu mempercepat pengerjaan UAS dari awal sampai output final.

---

## Apa yang Ditunjukkan Repo Ini

Project ini menunjukkan cara mengintegrasikan workflow data analysis dengan AI CLI secara lebih terstruktur:

- Dataset dan konteks bisnis dibuat eksplisit.
- AI CLI diberi `scenario.md` sebagai instruksi utama.
- Struktur data dijelaskan dalam `data_spec.yaml`.
- Rancangan dashboard dijelaskan dalam `dashboard_spec.json`.
- Validasi metrik dilakukan dengan Python.
- Laporan dan slide dapat digenerate sebagai draft awal.
- Tableau tetap dipakai untuk verifikasi visual dan export `.twbx`.

Pendekatannya bukan mengganti proses analisis, tetapi membuat prosesnya lebih cepat, terdokumentasi, dan bisa diulang.

---

## Ringkasan Project

| Item | Detail |
|---|---|
| Mata kuliah | Big Data Science |
| Studi kasus | Supermarket Sales Analysis |
| Dataset utama | `datasets/retail/supermarket_sales.csv` |
| Tools utama | Tableau Desktop, Python, AI CLI |
| Output akhir | `.twbx`, laporan `.docx/.pdf`, slide `.pptx/.pdf` |
| Dashboard | 6 sheet, 2 quick filter, 1 filter action, 1 parameter |
| Status data | Clean, 0 missing value, 0 duplicate |
| Persiapan wajib | Convert `Date` string ke Date dan ekstrak `Hour` dari `Time` |

---

## Dataset yang Dipilih

Dataset utama ada di:

```text
datasets/retail/supermarket_sales.csv
```

Karakteristik dataset:

- 1.000 baris transaksi.
- 17 kolom.
- Periode data: 1 Januari 2019 sampai 9 Maret 2019.
- 3 cabang: Yangon, Mandalay, Naypyitaw.
- 6 kategori produk.
- 3 metode pembayaran.
- 501 pelanggan Member dan 499 pelanggan Normal.

Kondisi data:

- Missing values: 0.
- Duplikasi `Invoice ID`: 0.
- Format kategorikal konsisten.
- Tidak ada outlier ekstrem yang perlu dibuang.
- `Date` awalnya perlu dipastikan sebagai Date di Tableau.
- `Time` dapat tetap string dan dipakai untuk membuat calculated field:

```text
Hour = INT(LEFT([Time], 2))
```

Informasi ini juga terdokumentasi di:

- `scenario.md`
- `data_spec.yaml`
- `laporan/TAHAP2_Profiling_Persiapan_Data.md`
- `laporan/TAHAP3_Pembersihan_Data.md`
- `PROJECT_AUDIT.md`

---

## Alur AI CLI

Kalau project ini dibuka di AI CLI, urutan file yang harus dibaca adalah:

1. `README.md`
   - Untuk memahami tujuan repository, struktur folder, output final, dan alur kerja umum.

2. `scenario.md`
   - Ini instruksi utama untuk AI CLI. Berisi business question, tahap 1-6, output yang harus dibuat, command, dan success criteria.

3. `data_spec.yaml`
   - Untuk memahami dataset, field, tipe data, calculated fields, validation rules, dan metrik yang sudah dihitung.

4. `dashboard_spec.json`
   - Untuk memahami rancangan dashboard Tableau: sheet, chart type, filter, action, parameter, layout, dan warna.

5. `PROJECT_AUDIT.md`
   - Untuk melihat status kelengkapan project, fungsi masing-masing file, risiko, dan checklist final.

6. File tahap laporan di folder `laporan/`
   - Untuk menyusun laporan akhir berdasarkan enam tahap wajib dari brief dosen.

7. Panduan pendukung
   - `PANDUAN_TABLEAU_LENGKAP.md`
   - `TABLEAU_WORKFLOW.md`
   - `SCREENSHOT_GUIDE.md`
   - `REPORT_READY.md`
   - `SLIDE_READY.md`

Prompt awal yang bisa diberikan ke AI CLI:

```text
Baca README.md terlebih dahulu, lalu baca scenario.md, data_spec.yaml,
dashboard_spec.json, dan PROJECT_AUDIT.md. Setelah itu jalankan pipeline
validasi dan bantu saya menyelesaikan output UAS Big Data Science sesuai
brief dosen.
```

---

## Struktur Repository

```text
.
├── README.md
├── scenario.md
├── PROJECT_AUDIT.md
├── data_spec.yaml
├── dashboard_spec.json
├── run_all.py
├── twb_generator.py
├── report_generator.py
├── slides_generator.py
├── datasets/
│   ├── SUMBER_DATASET.md
│   ├── retail/
│   │   └── supermarket_sales.csv
│   ├── agriculture/
│   ├── environment/
│   ├── finance/
│   └── health/
├── laporan/
│   ├── TAHAP1_Pemahaman_Masalah.md
│   ├── TAHAP2_Profiling_Persiapan_Data.md
│   ├── TAHAP3_Pembersihan_Data.md
│   ├── TAHAP4_Analisis_Eksploratif.md
│   ├── TAHAP5_Dashboard_Interaktif.md
│   └── TAHAP6_Sintesis_Rekomendasi.md
├── scripts/
│   ├── validate_data.py
│   └── validation_verify.py
├── luaran/
│   ├── Supermarket_Sales_Dashboard.twb
│   ├── Laporan_UAS_BigData_Supermarket_Sales.md
│   └── Slide_UAS_BigData_Supermarket_Sales.md
├── PANDUAN_TABLEAU_LENGKAP.md
├── TABLEAU_WORKFLOW.md
├── SCREENSHOT_GUIDE.md
├── REPORT_READY.md
├── SLIDE_READY.md
├── TEMPLATE_LAPORAN.md
├── TEMPLATE_SLIDE.md
└── PYTHON_SCRIPT.md
```

---

## Cara Menjalankan Pipeline

Pastikan posisi terminal ada di root repository:

```bash
cd path/to/repository
```

Jalankan semua proses utama:

```bash
python3 run_all.py
```

Command ini akan menjalankan:

1. Validasi metrik dataset.
2. Generate draft Tableau workbook `.twb`.
3. Generate draft laporan Markdown.
4. Generate draft slide Markdown.

Output akan muncul di folder:

```text
luaran/
```

---

## Output yang Dihasilkan

| Output | File | Status |
|---|---|---|
| Draft Tableau Workbook | `luaran/Supermarket_Sales_Dashboard.twb` | Generated |
| Tableau Packaged Workbook | `luaran/Supermarket_Sales_Dashboard.twbx` | Harus export manual dari Tableau |
| Draft laporan | `luaran/Laporan_UAS_BigData_Supermarket_Sales.md` | Generated |
| Draft slide | `luaran/Slide_UAS_BigData_Supermarket_Sales.md` | Generated |
| Validasi data | `scripts/validation_report.txt` | Generated setelah `validate_data.py` |

Catatan penting: file `.twb` adalah draft XML workbook. File `.twbx` final tetap harus dibuat lewat Tableau Desktop dengan menu **Export Packaged Workbook**, karena `.twbx` adalah format package milik Tableau.

---

## Alur Manual di Tableau

Setelah pipeline dijalankan:

1. Buka Tableau Desktop.
2. Buka file:

```text
luaran/Supermarket_Sales_Dashboard.twb
```

3. Verifikasi koneksi dataset.
4. Pastikan calculated fields, sheet, filter, action, dan parameter sesuai.
5. Rapikan visual dashboard jika perlu.
6. Ambil screenshot sesuai `SCREENSHOT_GUIDE.md`.
7. Export sebagai:

```text
luaran/Supermarket_Sales_Dashboard.twbx
```

---

## Tahapan Sesuai Brief UAS

| Tahap | File Utama | Isi |
|---|---|---|
| Tahap 1 | `laporan/TAHAP1_Pemahaman_Masalah.md` | Domain, stakeholder, business question, 5V, lifecycle |
| Tahap 2 | `laporan/TAHAP2_Profiling_Persiapan_Data.md` | Profil dataset, field, tipe data, persiapan Tableau |
| Tahap 3 | `laporan/TAHAP3_Pembersihan_Data.md` | Missing value, duplikasi, inkonsistensi, outlier |
| Tahap 4 | `laporan/TAHAP4_Analisis_Eksploratif.md` | EDA, tren, produk, pelanggan, korelasi |
| Tahap 5 | `laporan/TAHAP5_Dashboard_Interaktif.md` | Dashboard, quick filter, filter action, parameter |
| Tahap 6 | `laporan/TAHAP6_Sintesis_Rekomendasi.md` | Insight, rekomendasi, limitasi, future questions |

---

## Insight Utama

Beberapa hasil analisis yang sudah divalidasi:

| Insight | Nilai |
|---|---|
| Total revenue | `$322,966.75` |
| Average rating | `6.97 / 10` |
| Cabang revenue tertinggi | Naypyitaw, `$110,568.71` |
| AOV tertinggi | Naypyitaw, `$337.10` |
| Produk revenue tertinggi | Food and beverages, `$56,144.84` |
| Peak hour | 19:00, 113 transaksi |
| Member AOV | `$327.79` |
| Normal AOV | `$318.12` |

---

## Catatan Filosofi Project

Project ini dibuat karena workflow AI modern tidak harus berhenti di chatbot. AI CLI bisa membaca struktur folder, memahami file, menjalankan validasi, memperbaiki dokumen, membuat output, dan menjaga konteks teknis project. Untuk tugas yang punya banyak tahapan seperti UAS Big Data, pendekatan ini bisa menghemat waktu, mengurangi pekerjaan berulang, dan membuat pengerjaan lebih konsisten.

Tujuan akhirnya bukan menggantikan pemahaman manusia, tapi mempercepat kerja yang repetitif supaya energi bisa dipakai untuk hal yang lebih penting: memahami insight, menjelaskan keputusan, dan menyampaikan rekomendasi berbasis data.
