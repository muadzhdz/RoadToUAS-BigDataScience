# Tahap 1: Pemahaman Masalah dan Konteks Dataset
## Supermarket Sales Analysis

---

## 1. Domain dan Konteks Dataset

**Domain:** Bisnis Ritel / Supermarket

Dataset ini merepresentasikan data transaksi penjualan dari sebuah perusahaan supermarket fiksi yang memiliki **3 cabang** di **3 kota besar**:
- **Cabang A** — Yangon
- **Cabang B** — Mandalay  
- **Cabang C** — Naypyitaw

Data mencakup **1.000 transaksi** selama periode **1 Januari 2019 – 9 Maret 2019** (3 bulan). Setiap transaksi mencatat informasi pelanggan, produk yang dibeli, metode pembayaran, nilai transaksi, serta rating kepuasan pelanggan.

Perusahaan supermarket ini melayani **6 kategori produk**:
1. Electronic accessories
2. Fashion accessories
3. Food and beverages
4. Health and beauty
5. Home and lifestyle
6. Sports and travel

---

## 2. Identifikasi Pemangku Kepentingan (Stakeholder)

| Stakeholder | Peran | Kepentingan |
|-------------|-------|-------------|
| **Manajer Regional** | Mengawasi kinerja 3 cabang | Ingin tahu cabang mana yang berkinerja terbaik dan faktor pendorongnya |
| **Manajer Cabang** | Mengelola operasional harian | Butuh insight pola penjualan per produk dan jam sibuk untuk mengatur stok & shift |
| **Tim Marketing** | Menyusun strategi promosi & loyalitas | Ingin tahu efektivitas program member vs non-member, serta produk apa yang perlu dipromosikan |
| **Tim Keuangan** | Mengelola pendapatan & pajak | Memerlukan analisis pendapatan kotor, margin, dan tren biaya |

---

## 3. Pertanyaan Bisnis Utama

> **"Faktor-faktor apa yang paling mempengaruhi total penjualan dan tingkat kepuasan pelanggan di ketiga cabang supermarket, dan bagaimana strategi yang dapat diterapkan untuk meningkatkan pendapatan serta loyalitas pelanggan?"**

---

## 4. Sub-Pertanyaan Analitik (Minimal 3)

| # | Sub-Pertanyaan | Tujuan Analisis |
|---|----------------|-----------------|
| 1 | **Bagaimana tren penjualan harian dan mingguan di setiap cabang selama periode Jan-Mar 2019? Apakah ada pola musiman atau hari tertentu yang menunjukkan lonjakan penjualan?** | Identifikasi pola waktu untuk optimasi stok & jadwal karyawan |
| 2 | **Kategori produk apa yang paling berkontribusi terhadap total pendapatan dan memiliki margin keuntungan tertinggi? Apakah ada perbedaan preferensi produk antar cabang?** | Optimasi inventaris dan strategi promosi per cabang |
| 3 | **Bagaimana pengaruh tipe pelanggan (Member vs Normal) dan metode pembayaran terhadap nilai transaksi dan rating kepuasan?** | Evaluasi program loyalitas dan preferred payment method |
| 4 | **Apakah terdapat korelasi antara rating kepuasan dengan nilai transaksi, jumlah item, atau waktu transaksi?** | Identifikasi faktor yang mendorong kepuasan pelanggan |
| 5 | **Metode pembayaran apa yang paling dominan digunakan oleh tiap segmen pelanggan dan bagaimana pengaruhnya terhadap frekuensi pembelian?** | Insight untuk strategi partnership payment & promosi |

---

## 5. Relevansi dengan Konsep Big Data (5V)

| V | Penjelasan | Relevansi Dataset |
|---|------------|-------------------|
| **Volume** | Jumlah data yang besar | **1.000 baris transaksi** — skala kecil namun cukup representatif untuk analisis retail skala menengah |
| **Velocity** | Kecepatan data masuk | Data transaksi bersifat harian dengan timestamp per transaksi, mencerminkan aliran data real-time pada sistem POS |
| **Variety** | Keragaman tipe data | Dataset memiliki **17 kolom** dengan tipe data beragam: numerik (Total, Quantity, Rating), kategorikal (Branch, Product line, Payment), temporal (Date, Time), dan tekstual (Invoice ID) |
| **Veracity** | Kualitas & akurasi data | Data bersih tanpa missing value, namun merupakan data sintetis sehingga memiliki konsistensi tinggi — preprocessing tetap perlu didokumentasikan |
| **Value** | Nilai bisnis yang dapat diekstrak | Analisis dapat menghasilkan **rekomendasi strategis**: optimasi stok produk, evaluasi program member, strategi pricing per cabang, dan peningkatan kepuasan pelanggan |

---

## 6. Posisi Dataset dalam Data Lifecycle

```
[Sumber Data] ──> [Pengumpulan] ──> [Penyimpanan] ──> [Analisis] ──> [Presentasi]
                      (POS System)     (CSV File)      (Tableau)        (Dashboard)
                           │                 │
                           ▼                 ▼
                     Transaksi harian     Dataset siap
                     di 3 cabang          pakai (clean)
```

**Penjelasan:**
1. **Sumber Data:** Sistem POS (Point of Sale) di 3 cabang supermarket mencatat setiap transaksi secara real-time
2. **Pengumpulan:** Data dikumpulkan dari sistem POS selama periode 3 bulan (Jan-Mar 2019)
3. **Penyimpanan:** Data diekspor ke format CSV — kita menerima data pada tahap ini sebagai file flat
4. **Analisis:** Dataset akan diolah menggunakan Tableau untuk profiling, cleaning, eksplorasi, visualisasi, dan dashboard interaktif
5. **Presentasi:** Hasil analisis disajikan dalam bentuk dashboard interaktif yang dapat digunakan oleh pengambil keputusan

Dataset yang kita gunakan sudah berada pada tahap **penyimpanan (storage)**, dan kita akan memprosesnya melalui tahap **analisis** hingga **presentasi** sesuai dengan alur kerja data analyst.

---

## Ringkasan Dataset

| Metrik | Nilai |
|--------|-------|
| Total Baris | 1.000 transaksi |
| Total Kolom | 17 field |
| Rentang Waktu | 1 Jan 2019 – 9 Mar 2019 |
| Total Pendapatan | **$322,966.75** |
| Rata-rata Rating | **6.97 / 10** |
| Cabang | 3 (Yangon, Naypyitaw, Mandalay) |
| Kategori Produk | 6 (Electronic accessories, Fashion accessories, Food & beverages, Health & beauty, Home & lifestyle, Sports & travel) |
| Metode Pembayaran | 3 (Cash, Ewallet, Credit card) |
| Tipe Pelanggan | Member (50.1%), Normal (49.9%) |
| Rata-rata Gross Income per Transaksi | $15.38 |
| Sumber Data | Kaggle — Supermarket Sales Dataset |

---

*Lanjut ke **Tahap 2: Profiling dan Persiapan Data** setelah dokumen ini disetujui.*
