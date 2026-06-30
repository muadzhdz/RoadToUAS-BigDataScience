# Tahap 6: Sintesis Insight dan Rekomendasi
## Supermarket Sales Analysis — Tableau

---

## 1. Jawaban Pertanyaan Bisnis Utama

> **Pertanyaan:**
> *"Faktor-faktor apa yang paling mempengaruhi total penjualan dan tingkat kepuasan pelanggan di ketiga cabang supermarket, dan bagaimana strategi yang dapat diterapkan untuk meningkatkan pendapatan serta loyalitas pelanggan?"*

### 1.1. Faktor yang Mempengaruhi Total Penjualan

Berdasarkan analisis data 1.000 transaksi dari 3 cabang, berikut faktor-faktor utama:

| Faktor | Dampak | Bukti Data |
|--------|--------|------------|
| **[CITY] Lokasi Cabang** | SIGNIFIKAN | Naypyitaw unggul 4.1% dalam total revenue ($110,568) vs Yangon ($106,200) dan Mandalay ($106,197) meski memiliki transaksi paling sedikit |
| **[TIME] Waktu Transaksi** | SIGNIFIKAN | Jam 19:00 menyumbang 11.3% transaksi — tertinggi sepanjang hari. Revenue per jam di 19:00 = $39,699 |
| **[OUTPUT] Kategori Produk** | MODERAT | 5 dari 6 kategori memiliki kontribusi hampir identik (~$54K). Food & Beverages unggul tipis ($56K) |
| **[CUSTOMER] Tipe Pelanggan** | MODERAT | Member menghabiskan $9.67 lebih banyak per transaksi (+3%) dibanding Normal |
| **[PAYMENT] Metode Bayar** | RENDAH | Perbedaan revenue antar metode minimal. Cash/Ewallet dominan ~34.5% |

### 1.2. Faktor yang Mempengaruhi Kepuasan Pelanggan

| Faktor | Dampak | Detail |
|--------|:------:|--------|
| **Kategori Produk** | [OK] Ada | Food & Beverages rating tertinggi (7.11), Home & Lifestyle terendah (6.84) |
| **Lokasi Cabang** | [OK] Ada | Naypyitaw rating 7.07, Mandalay terendah 6.82 |
| **Nilai Transaksi** | [NO] Tidak | Scatter plot menunjukkan tidak ada korelasi antara Total dan Rating |
| **Jumlah Item** | [NO] Tidak | Quantity juga tidak berkorelasi dengan Rating |
| **Metode Bayar** | [NO] Minimal | Selisih rating antar metode hanya 0.05 poin |
| **Tipe Pelanggan** | [NO] Minimal | Member rating 6.94, Normal 7.01 — selisih tidak signifikan |

**Kesimpulan Utama:**
Kepuasan pelanggan **tidak dipengaruhi** oleh nilai transaksi atau jumlah item. Faktor yang lebih berpengaruh adalah **kategori produk** (terutama F&B) dan **lokasi cabang** (Naypyitaw unggul). Ini mengindikasikan bahwa kualitas layanan dan produk lebih penting daripada nominal belanja.

---

## 2. Jawaban Sub-Pertanyaan Analitik

### Q1: Tren Penjualan Harian & Mingguan

**Jawaban:**
Tren penjualan harian menunjukkan fluktuasi normal dengan puncak di sekitar akhir pekan. Revenue tertinggi dalam satu hari terjadi pada **3/9/2019 ($7,474)** dan terendah pada **2/13/2019 ($934)**. Ketiga cabang menunjukkan pola yang relatif paralel — artinya faktor eksternal (seperti hari libur atau cuaca) mempengaruhi semua cabang secara seragam.

### Q2: Kategori Produk & Kontribusi

**Jawaban:**
Food & Beverages adalah kontributor terbesar ($56,144 — 17.38%) dengan rating tertinggi (7.11). Namun, distribusi revenue cukup merata antar kategori — ini menandakan strategi diversifikasi produk telah berjalan baik. Setiap cabang memiliki kekuatan berbeda: Naypyitaw dominan di F&B, Yangon dominan di Home & Lifestyle.

### Q3: Member vs Normal & Metode Bayar

**Jawaban:**
Member memberikan kontribusi lebih tinggi (+3% per transaksi) namun dengan rating sedikit lebih rendah. Program member sudah efektif tetapi belum optimal. Cash dan Ewallet adalah metode pembayaran paling dominan.

### Q4: Korelasi Rating dengan Variabel Lain

**Jawaban:**
Tidak ada korelasi linear antara rating dengan Total (R² mendekati 0) maupun Quantity. Ini adalah temuan penting — menunjukkan bahwa pelanggan tidak menilai berdasarkan nilai transaksi.

### Q5: Preferensi Metode Bayar per Segmen

**Jawaban:**
Cash dan Ewallet sama-sama populer di semua segmen. Credit card sedikit kurang digunakan. Tidak ada perbedaan signifikan preferensi pembayaran antara Member dan Normal.

---

## 3. Rekomendasi Strategis

### Rekomendasi 1: Optimasi Jam Operasional (Prioritas Tinggi)

**Temuan:** Jam 19:00 adalah peak hour dengan 113 transaksi dan revenue $39,699.
**Rekomendasi:**
- Tambahkan **2 kasir tambahan** pada shift 18:30-20:00 di semua cabang
- Pastikan stok produk populer (F&B) terisi penuh menjelang jam 18:00
- Terapkan **"Happy Hour Promo"** di jam sepi (17:00-18:00) untuk meratakan distribusi transaksi
- **Target:** Meningkatkan revenue jam sepi sebesar 15%

### Rekomendasi 2: Tingkatkan Program Member (Prioritas Tinggi)

**Temuan:** Member spend $9.67 lebih banyak (+3%) dan ada 501 member dari 1.000 transaksi.
**Rekomendasi:**
- **Tiered Membership:** Buat level Silver/Gold/Platinum berdasarkan frekuensi belanja
- **Member-only promo:** Diskon khusus untuk kategori dengan rating rendah (Home & Lifestyle) untuk meningkatkan kepuasan
- **Referral program:** Member yang mereferensikan pelanggan normal mendapat poin reward
- **Target:** Meningkatkan rasio member dari 50.1% menjadi 60% dan avg spend member menjadi +5%

### Rekomendasi 3: Strategi Produk per Cabang (Prioritas Sedang)

**Temuan:** Setiap cabang memiliki preferensi produk yang berbeda.
**Rekomendasi:**
- **Naypyitaw:** Fokus stok dan promosi Food & Beverages serta Fashion accessories — perluas variasi produk di kategori ini
- **Yangon:** Tingkatkan display dan promosi Home & Lifestyle dan Sports & Travel — pertimbangkan kolaborasi dengan brand lokal
- **Mandalay:** Optimasi Health & Beauty dan Sports & Travel — rating Mandalay terendah (6.82), perlu perbaikan layanan
- **Target:** Meningkatkan revenue per cabang sebesar 5% melalui penyesuaian stok

### Rekomendasi 4: Investigasi Rating Mandalay (Prioritas Sedang)

**Temuan:** Mandalay memiliki rating terendah (6.82) dibanding Naypyitaw (7.07) dan Yangon (7.03).
**Rekomendasi:**
- Lakukan survei kepuasan pelanggan khusus untuk cabang Mandalay
- Evaluasi kualitas layanan staf dan kebersihan toko
- Bandingkan jam operasional dan tata letak toko dengan cabang lain
- **Target:** Meningkatkan rating Mandalay ke 7.0 dalam 3 bulan

### Rekomendasi 5: Promosi Credit Card (Prioritas Rendah)

**Temuan:** Credit card digunakan paling sedikit (31.1% transaksi) namun pembeli CC memberi rating tertinggi (7.00).
**Rekomendasi:**
- Tawarkan diskon 2% untuk pembayaran Credit Card
- Kerja sama dengan bank untuk promo cicilan 0%
- **Target:** Meningkatkan penggunaan CC ke 35%

---

## 4. Matriks Prioritas Rekomendasi

| # | Rekomendasi | Dampak | Usaha | Prioritas |
|:-:|------------|:------:|:----:|:---------:|
| 1 | Optimasi jam operasional | [PRIMER] Tinggi | [GREEN] Rendah | **P1** [P1] |
| 2 | Tingkatkan program member | [PRIMER] Tinggi | [SEKUNDER] Sedang | **P1** [P1] |
| 3 | Strategi produk per cabang | [SEKUNDER] Sedang | [SEKUNDER] Sedang | **P2** |
| 4 | Investigasi rating Mandalay | [SEKUNDER] Sedang | [GREEN] Rendah | **P2** |
| 5 | Promosi Credit Card | [GREEN] Rendah | [GREEN] Rendah | **P3** |

---

## 5. Keterbatasan Analisis

| # | Keterbatasan | Dampak | Mitigasi |
|:-:|-------------|:------:|----------|
| 1 | **Data hanya 3 bulan** | Tidak bisa mendeteksi pola musiman tahunan | Gunakan sebagai baseline untuk monitoring ke depan |
| 2 | **Dataset sintetis** | Pola data mungkin tidak mencerminkan realitas sempurna | Validasi temuan dengan data tambahan jika tersedia |
| 3 | **Tidak ada data biaya operasional** | Tidak bisa menghitung profitabilitas bersih per cabang | Fokus pada revenue dan gross income |
| 4 | **Tidak ada demografi detail (usia, pekerjaan)** | Segmentasi pelanggan terbatas pada Member/Normal | Pertimbangkan survei tambahan |
| 5 | **Rating subjektif** | Rating 7 dari pelanggan A bisa berbeda artinya dengan pelanggan B | Analisis berdasarkan tren, bukan nilai absolut |
| 6 | **Tidak ada data kompetitor** | Tidak bisa membandingkan performa dengan pasar | Tambahkan data kompetitor jika ada |

---

## 6. Pertanyaan Lanjutan untuk Penelitian Mendatang

1. Bagaimana tren penjualan year-over-year? Apakah ada pertumbuhan?
2. Apakah ada pengaruh musiman (hari raya, liburan sekolah) terhadap pola belanja?
3. Bagaimana profitabilitas bersih setelah memperhitungkan biaya sewa, gaji, dan utilitas per cabang?
4. Apakah ada segmentasi pelanggan yang lebih granular (berdasarkan frekuensi, kategori favorit)?
5. Bagaimana pengaruh promosi diskon terhadap volume penjualan dan loyalitas pelanggan?
6. Apakah ada perbedaan pola belanja antara pelanggan pagi (10:00-12:00) vs malam (18:00-20:00)?

---

## 7. Ringkasan Eksekutif

**Supermarket Sales Analysis** menganalisis 1.000 transaksi dari 3 cabang supermarket (Yangon, Mandalay, Naypyitaw) selama Jan-Mar 2019.

**Temuan Kunci:**
- Total revenue: **$322,966.75** dengan Naypyitaw sebagai cabang dengan performa terbaik ($110,568)
- Jam 19:00 adalah **peak hour** dengan kontribusi revenue tertinggi
- **Food & Beverages** adalah kategori paling populer dan paling memuaskan
- **Program Member** sudah efektif (+3% spend) tetapi belum optimal
- **Kepuasan pelanggan** tidak dipengaruhi oleh nilai transaksi — kualitas layanan dan produk lebih penting

**Rekomendasi Utama:**
1. [P1] **Optimasi jam operasional** — tambah staf di peak hour, promo di jam sepi
2. [P1] **Tingkatkan program member** — tiered membership, referral program
3. **Strategi produk per cabang** — sesuaikan stok dengan preferensi lokal
4. **Investigasi rating Mandalay** — cari akar masalah kepuasan terendah
5. **Promosi Credit Card** — insentif untuk meningkatkan penggunaan

---

*Dokumen ini menjadi dasar untuk pembuatan **Laporan Tertulis** dan **Slide Presentasi**.*
