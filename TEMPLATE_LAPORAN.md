# [REPORT] TEMPLATE LAPORAN UAS BIG DATA
## Supermarket Sales Analysis

**Mata Kuliah:** Big Data Science
**Dosen:** [Nama Dosen]
**Kelompok:** [Anggota 1 — NIM], [Anggota 2 — NIM], [Anggota 3 — NIM]

---

## Struktur Laporan (Max 20 Halaman)

### Halaman Cover (1 halaman)
- Logo Universitas (jika ada)
- Judul: "Analisis Data Penjualan Supermarket Menggunakan Tableau"
- Mata Kuliah: Big Data Science
- Nama Kelompok & NIM
- Dosen Pengampu
- Tahun Akademik

---

### Bab 1: Pendahuluan (2-3 halaman)

**1.1. Latar Belakang**
- Big Data dalam industri ritel
- Pentingnya analisis data transaksi untuk pengambilan keputusan
- Dataset Supermarket Sales sebagai studi kasus

**1.2. Rumusan Masalah**
- Faktor yang mempengaruhi penjualan dan kepuasan pelanggan di 3 cabang supermarket

**1.3. Pertanyaan Bisnis**
Primer: "Faktor-faktor apa yang paling mempengaruhi total penjualan dan tingkat kepuasan pelanggan di ketiga cabang supermarket?"
Sub: 5 sub-pertanyaan dari Tahap 1

**1.4. Tujuan**
- Menganalisis tren penjualan
- Mengidentifikasi produk unggulan
- Mengevaluasi program member
- Membangun dashboard interaktif

**1.5. Manfaat**
Bagi manajemen: insight operasional dan strategis

> **Isi detail:** Lihat `TAHAP1_Pemahaman_Masalah.md`
> - 5V Big Data (Volume, Velocity, Variety, Veracity, Value)
> - Data Lifecycle
> - Identifikasi Stakeholder

---

### Bab 2: Profil Dataset (2 halaman)

**2.1. Sumber Data**
- Platform: Kaggle — Supermarket Sales Dataset
- URL: https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales
- Format: CSV, 1.000 baris × 17 kolom

**2.2. Deskripsi Field**
Tabel 17 field dengan tipe data dan makna bisnis

**2.3. Statistik Dasar**
- Total revenue: $322,966.75
- Rentang waktu: 1 Jan – 9 Mar 2019
- 3 cabang, 6 kategori produk, 3 metode pembayaran
- 501 Member, 499 Normal

> **Isi detail:** Lihat `TAHAP2_Profiling_Persiapan_Data.md`

---

### Bab 3: Pembersihan Data (2 halaman)

**3.1. Pengecekan Missing Values**
- Hasil: 0 null values
- Screenshot: [Gambar 3.1]

**3.2. Pengecekan Duplikasi**
- Hasil: 0 duplikat (COUNT = COUNTD = 1.000)
- Screenshot: [Gambar 3.2]

**3.3. Pengecekan Inkonsistensi Format**
- Semua field kategorikal konsisten
- Screenshot: [Gambar 3.3]

**3.4. Pengecekan Outlier**
- Box Plot Total per City: tidak ada outlier ekstrem
- Screenshot: [Gambar 3.4]

**3.5. Konversi Tipe Data**
- Date: String → Date
- Time: String → Hour (Calculated Field)

**3.6. Calculated Fields**
- Daftar 7+ CF yang dibuat

> **Isi detail:** Lihat `TAHAP3_Pembersihan_Data.md`

---

### Bab 4: Analisis Data (5-6 halaman)

**4.1. Analisis Tren Waktu**
- Tren penjualan harian per cabang (Line Chart)
- Penjualan per hari dalam seminggu
- Jam sibuk (Peak hours analysis)
- [Gambar 4.1, 4.2, 4.3]

**4.2. Analisis Produk**
- Revenue per product line
- Gross income analysis
- Rating per product line
- Heatmap produk per cabang
- [Gambar 4.4, 4.5, 4.6, 4.7]

**4.3. Analisis Pelanggan**
- Member vs Normal
- Analisis metode pembayaran
- Preferensi produk per segmen
- [Gambar 4.8, 4.9]

**4.4. Analisis Korelasi**
- Scatter plot: Total vs Rating (tidak ada korelasi)
- Scatter plot: Quantity vs Rating
- Rating per jam
- [Gambar 4.10, 4.11]

**4.5. Analisis Demografi**
- Gender distribution
- Payment by gender
- [Gambar 4.12]

> **Isi detail:** Lihat `TAHAP4_Analisis_Eksploratif.md`
> Setiap sub-bab harus mengandung: Nama visualisasi, Tujuan, Insight, Screenshot

---

### Bab 5: Dashboard Interaktif (2-3 halaman)

**5.1. Komponen Dashboard**
- 6 sheet utama
- 2 Quick Filter (City, Product line)
- 2 Filter Action
- 1+ Parameter (Top N Products)

**5.2. Layout Dashboard**
- [Gambar 5.1: Full Dashboard screenshot]

**5.3. Interaktivitas**
- Cara kerja filter
- Cara kerja parameter
- Cara kerja filter action

**5.4. Panduan Penggunaan**
- Cara memfilter per cabang
- Cara mengganti metrik
- Cara menggunakan Top N

> **Isi detail:** Lihat `TAHAP5_Dashboard_Interaktif.md`

---

### Bab 6: Kesimpulan dan Rekomendasi (2 halaman)

**6.1. Kesimpulan**
- Jawaban pertanyaan bisnis utama
- Temuan kunci (10 temuan dari analisis)

**6.2. Rekomendasi**
| Prioritas | Rekomendasi |
|:---------:|-------------|
| P1 [P1] | Optimasi jam operasional (tambah staf peak hour) |
| P1 [P1] | Tingkatkan program member (tiered membership) |
| P2 | Strategi produk per cabang |
| P2 | Investigasi rating Mandalay |
| P3 | Promosi Credit Card |

**6.3. Keterbatasan**
- Data 3 bulan
- Dataset sintetis
- Tidak ada data biaya operasional

**6.4. Saran Penelitian Lanjutan**
- Analisis year-over-year
- Segmentasi pelanggan lebih detail
- Analisis profitabilitas bersih

> **Isi detail:** Lihat `TAHAP6_Sintesis_Rekomendasi.md`

---

### Daftar Pustaka

1. Kaggle — Supermarket Sales Dataset. https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales
2. [Materi kuliah Big Data Science]
3. [Dokumentasi Tableau]

### Lampiran
- Screenshot tambahan
- Tabel data lengkap
- Daftar Calculated Fields

---

## Tips Penulisan Laporan

| Aspek | Tips |
|-------|------|
| **Maksimal 20 halaman** | Gunakan font 12pt, spacing 1.5, margin 3cm |
| **Screenshot berkualitas** | Crop dan beri border, jangan screenshot buram |
| **Setiap gambar punya caption** | Contoh: "Gambar 4.1: Tren Penjualan Harian per Cabang" |
| **Gunakan tabel** | Ringkas data dalam tabel, jangan paragraf panjang |
| **Bahasa** | Gunakan Bahasa Indonesia formal (atau Inggris sesuai instruksi dosen) |
| **Konsisten** | Format tabel, font, numbering harus konsisten |

---

## Format File Kumpul

| Luaran | Format | Nama File |
|--------|--------|-----------|
| Laporan | .docx atau .pdf | `Laporan_UAS_BigData_KelompokX.docx` |
| Dashboard | .twbx | `Supermarket_Sales_Dashboard.twbx` |
| Slide | .pptx atau .pdf | `Slide_UAS_BigData_KelompokX.pptx` |

---

**Deadline:** [Tanggal 9, pukul 23.59]
**Tempat Kumpul:** [Sesuai instruksi dosen — Google Drive / LMS / Email]
