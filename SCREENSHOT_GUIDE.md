# [SCREENSHOT] PANDUAN SCREENSHOT — Supermarket Sales Analysis
## 13 Screenshot Wajib untuk Laporan

---

### Cara Mengambil Screenshot yang Baik

| Aturan | Keterangan |
|--------|-----------|
| **Resolusi** | Minimal 1280×720 (jangan zoom in berlebihan) |
| **Format** | PNG (kualitas terbaik) |
| **Nama File** | `GambarX.Y_Filename.png` — lihat tabel di bawah |
| **Crop** | Hanya area relevan, jangan include taskbar Windows |
| **Border** | Bisa tambah border tipis (opsional) |
| **Tool** | Gunakan Snipping Tool / Windows+Shift+S |

---

## SCREENSHOT PER TAHAP

### TAHAP 3: Pembersihan Data (4 screenshot)

#### Screenshot 3.1 — Cek Missing Values
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar3.1_MissingValues.png` |
| **Tampilkan** | Data Source di Tableau dengan semua kolom — tunjukkan 1.000 baris lengkap |
| **Cara Ambil** | Buka tab **Data Source** → pastikan semua data terisi → screenshot seluruh tabel |
| **Caption Laporan** | *Gambar 3.1: Pengecekan missing values menunjukkan seluruh 1.000 baris memiliki data lengkap* |
| **Lokasi di Laporan** | Bab 3 sub-bab 3.1 |

#### Screenshot 3.2 — Cek Duplikasi
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar3.2_Duplicates.png` |
| **Tampilkan** | COUNT(Invoice ID) = 1000 dan COUNTD(Invoice ID) = 1000 |
| **Cara Ambil** | Worksheet → drag Invoice ID ke Rows 2x → Count & Count Distinct → screenshot labelnya |
| **Caption Laporan** | *Gambar 3.2: Pengecekan duplikasi — COUNT dan COUNTD sama-sama 1.000, tidak ada data duplikat* |
| **Lokasi di Laporan** | Bab 3 sub-bab 3.2 |

#### Screenshot 3.3 — Inkonsistensi Format
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar3.3_FormatCheck.png` |
| **Tampilkan** | Data Source dengan kolom City/Product line/Payment yang sudah di-sort ascending |
| **Cara Ambil** | Data Source → klik header City → Sort Ascending → screenshot kolom City + 2-3 kolom lain |
| **Caption Laporan** | *Gambar 3.3: Pengecekan inkonsistensi format pada field kategorikal — semua nilai konsisten* |
| **Lokasi di Laporan** | Bab 3 sub-bab 3.3 |

#### Screenshot 3.4 — Box Plot Outlier
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar3.4_BoxPlot.png` |
| **Tampilkan** | Box Plot Total per City (3 box plot berdampingan) |
| **Cara Ambil** | Worksheet → Total ke Columns, City ke Rows → Distribution Band → Box Plot → screenshot |
| **Caption Laporan** | *Gambar 3.4: Box Plot Total per cabang — tidak terdapat outlier ekstrem di ketiga cabang* |
| **Lokasi di Laporan** | Bab 3 sub-bab 3.4 |

---

### TAHAP 4: Analisis Eksploratif (5 screenshot)

#### Screenshot 4.1 — Revenue Trend
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar4.1_RevenueTrend.png` |
| **Tampilkan** | Line chart tren penjualan harian — 3 garis warna per cabang |
| **Caption Laporan** | *Gambar 4.1: Tren penjualan harian per cabang — Naypyitaw (hijau) konsisten di atas* |
| **Lokasi di Laporan** | Bab 4 sub-bab 4.1 |

#### Screenshot 4.2 — Product Performance
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar4.2_ProductPerformance.png` |
| **Tampilkan** | Bar chart revenue per product line (horizontal, stacked by City) |
| **Caption Laporan** | *Gambar 4.2: Total pendapatan per kategori produk — Food & Beverages menjadi kontributor terbesar* |
| **Lokasi di Laporan** | Bab 4 sub-bab 4.2 |

#### Screenshot 4.3 — Rating Analysis
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar4.3_RatingAnalysis.png` |
| **Tampilkan** | Bar chart AVG(Rating) per product line dengan reference line di 6.97 |
| **Caption Laporan** | *Gambar 4.3: Rata-rata rating per kategori produk — Food & Beverages mendapat rating tertinggi (7.11)* |
| **Lokasi di Laporan** | Bab 4 sub-bab 4.2 |

#### Screenshot 4.4 — Hourly Activity
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar4.4_HourlyActivity.png` |
| **Tampilkan** | Bar chart jumlah transaksi per jam — tunjukkan peak di jam 19:00 |
| **Caption Laporan** | *Gambar 4.4: Distribusi transaksi per jam — puncak aktivitas terjadi pada jam 19:00 dengan 113 transaksi* |
| **Lokasi di Laporan** | Bab 4 sub-bab 4.1 |

#### Screenshot 4.5 — Heatmap Produk per Cabang
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar4.5_HeatmapProduk.png` |
| **Tampilkan** | Heatmap (City × Product line) dengan warna berdasarkan SUM(Total) |
| **Caption Laporan** | *Gambar 4.5: Heatmap preferensi produk per cabang — Naypyitaw dominan di Food & Beverages, Yangon di Home & Lifestyle* |
| **Lokasi di Laporan** | Bab 4 sub-bab 4.2 |

---

### TAHAP 5: Dashboard (3 screenshot)

#### Screenshot 5.1 — Full Dashboard
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar5.1_FullDashboard.png` |
| **Tampilkan** | Dashboard lengkap — semua sheet, filter, parameter dalam satu layar |
| **Cara Ambil** | Dashboard view → pastikan semua elemen terlihat → **Dashboard → Copy Image** |
| **Caption Laporan** | *Gambar 5.1: Dashboard interaktif Supermarket Sales Analysis — terdiri dari 6 sheet visualisasi dengan Quick Filter dan Parameter* |
| **Lokasi di Laporan** | Bab 5 sub-bab 5.2 — LAYAR PENUH (usahakan 1 halaman) |

#### Screenshot 5.2 — Dashboard Saat Difilter
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar5.2_DashboardFiltered.png` |
| **Tampilkan** | Dashboard setelah difilter — pilih "Naypyitaw" di Quick Filter City |
| **Cara Ambil** | Filter City → Naypyitaw → screenshot |
| **Caption Laporan** | *Gambar 5.2: Dashboard setelah difilter untuk cabang Naypyitaw — semua sheet menampilkan data Naypyitaw secara spesifik* |
| **Lokasi di Laporan** | Bab 5 sub-bab 5.3 |

#### Screenshot 5.3 — Filter Action Config
| Item | Detail |
|------|--------|
| **Nama File** | `Gambar5.3_FilterAction.png` |
| **Tampilkan** | Dialog konfigurasi Filter Action (Dashboard → Actions) |
| **Cara Ambil** | Dashboard → Actions → klik "Filter by City" → screenshot dialog |
| **Caption Laporan** | *Gambar 5.3: Konfigurasi Filter Action — klik cabang di Revenue Trend akan memfilter seluruh sheet* |
| **Lokasi di Laporan** | Bab 5 sub-bab 5.3 atau Lampiran |

---

### TAHAP 5: Calculated Fields (1 screenshot)

#### Screenshot CF — Daftar Calculated Fields
| Item | Detail |
|------|--------|
| **Nama File** | `GambarCF_CalculatedFields.png` |
| **Tampilkan** | Panel Data di Tableau — tunjukkan semua Calculated Fields yang sudah dibuat |
| **Cara Ambil** | Panel Data (kiri) → klik dropdown Dimensions/Measures → scroll sampai semua CF terlihat |
| **Caption Laporan** | *Gambar 4.6: Daftar Calculated Fields yang dibuat untuk memperkaya analisis* |
| **Lokasi di Laporan** | Bab 4 sub-bab 4.5 (atau sisipkan di bagian Analisis) |

---

## RINGKASAN 13 SCREENSHOT

| # | Nama File | Dari | Untuk Bab | Halaman |
|:-:|-----------|:----:|:---------:|:-------:|
| 1 | `Gambar3.1_MissingValues.png` | TAHAP 3 | Bab 3 sub 3.1 | ~hal 6 |
| 2 | `Gambar3.2_Duplicates.png` | TAHAP 3 | Bab 3 sub 3.2 | ~hal 7 |
| 3 | `Gambar3.3_FormatCheck.png` | TAHAP 3 | Bab 3 sub 3.3 | ~hal 7 |
| 4 | `Gambar3.4_BoxPlot.png` | TAHAP 3 | Bab 3 sub 3.4 | ~hal 8 |
| 5 | `Gambar4.1_RevenueTrend.png` | TAHAP 4 | Bab 4 sub 4.1 | ~hal 9 |
| 6 | `Gambar4.2_ProductPerformance.png` | TAHAP 4 | Bab 4 sub 4.2 | ~hal 10 |
| 7 | `Gambar4.3_RatingAnalysis.png` | TAHAP 4 | Bab 4 sub 4.2 | ~hal 11 |
| 8 | `Gambar4.4_HourlyActivity.png` | TAHAP 4 | Bab 4 sub 4.1 | ~hal 11 |
| 9 | `Gambar4.5_HeatmapProduk.png` | TAHAP 4 | Bab 4 sub 4.2 | ~hal 12 |
| 10 | `GambarCF_CalculatedFields.png` | TAHAP 4 | Bab 4 sub 4.5 | ~hal 13 |
| 11 | `Gambar5.1_FullDashboard.png` | TAHAP 5 | Bab 5 sub 5.2 | ~hal 15 (full) |
| 12 | `Gambar5.2_DashboardFiltered.png` | TAHAP 5 | Bab 5 sub 5.3 | ~hal 16 |
| 13 | `Gambar5.3_FilterAction.png` | TAHAP 5 | Bab 5 sub 5.3 | ~hal 16 |

---

## TEMPLATE CAPTION SIAP PAKAI

Copy-paste caption ini ke laporan:

```
**Gambar 3.1:** Pengecekan missing values — seluruh 1.000 baris memiliki data lengkap.

**Gambar 3.2:** Pengecekan duplikasi — COUNT dan COUNTD(Invoice ID) sama-sama 1.000, tidak ada duplikasi.

**Gambar 3.3:** Pengecekan inkonsistensi format pada field kategorikal — semua nilai konsisten tanpa variasi ejaan.

**Gambar 3.4:** Box Plot distribusi Total per cabang — tidak terdapat outlier ekstrem.

**Gambar 4.1:** Tren penjualan harian per cabang (Jan-Mar 2019).

**Gambar 4.2:** Total pendapatan per kategori produk.

**Gambar 4.3:** Rata-rata rating per kategori produk.

**Gambar 4.4:** Distribusi transaksi per jam — puncak aktivitas di jam 19:00.

**Gambar 4.5:** Heatmap preferensi produk per cabang.

**Gambar 4.6:** Daftar Calculated Fields yang digunakan dalam analisis.

**Gambar 5.1:** Dashboard interaktif Supermarket Sales — tampilan penuh.

**Gambar 5.2:** Dashboard setelah difilter untuk cabang tertentu.

**Gambar 5.3:** Konfigurasi Filter Action di Tableau.
```

---

## FOLDER STRUCTURE UNTUK SCREENSHOT

```
./
└── screenshots/              ← BUAT FOLDER INI
    ├── tahap3/
    │   ├── Gambar3.1_MissingValues.png
    │   ├── Gambar3.2_Duplicates.png
    │   ├── Gambar3.3_FormatCheck.png
    │   └── Gambar3.4_BoxPlot.png
    ├── tahap4/
    │   ├── Gambar4.1_RevenueTrend.png
    │   ├── Gambar4.2_ProductPerformance.png
    │   ├── Gambar4.3_RatingAnalysis.png
    │   ├── Gambar4.4_HourlyActivity.png
    │   ├── Gambar4.5_HeatmapProduk.png
    │   └── GambarCF_CalculatedFields.png
    └── tahap5/
        ├── Gambar5.1_FullDashboard.png
        ├── Gambar5.2_DashboardFiltered.png
        └── Gambar5.3_FilterAction.png
```

**Buat foldernya:**
```bash
mkdir -p screenshots/{tahap3,tahap4,tahap5}
```
