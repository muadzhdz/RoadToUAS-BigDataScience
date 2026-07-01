# [REPORT] LAPORAN UAS BIG DATA SCIENCE — READY TO COPY
## Analisis Data Penjualan Supermarket Menggunakan Tableau

---

> **CARA PAKAI:** File ini berisi konten paragraf **lengkap** untuk laporan. Tinggal:
> 1. Ganti `[Nama]` / `[NIM]` dengan data lo
> 2. Insert screenshot sesuai `SCREENSHOT_GUIDE.md`
> 3. Copy ke Word, atur formatting (font 12, spasi 1.5, margin 3)
> 4. Export ke PDF

---

### HALAMAN COVER

```
┌─────────────────────────────────────────────┐
│                                             │
│         [LOGO UNIVERSITAS]                  │
│                                             │
│          LAPORAN UAS                        │
│          BIG DATA SCIENCE                   │
│                                             │
│   ANALISIS DATA PENJUALAN SUPERMARKET       │
│   MENGGUNAKAN TABLEAU                       │
│                                             │
│  Disusun oleh:                              │
│  [Nama Anggota 1] — [NIM]                  │
│  [Nama Anggota 2] — [NIM]                  │
│  [Nama Anggota 3] — [NIM]                  │
│                                             │
│  Dosen Pengampu:                            │
│  [Nama Dosen]                               │
│                                             │
│  PROGRAM STUDI [PRODI]                      │
│  [NAMA UNIVERSITAS]                         │
│  TAHUN AKADEMIK [TA]                        │
│                                             │
└─────────────────────────────────────────────┘
```

---

### BAB 1: PENDAHULUAN

#### 1.1. Latar Belakang

Perkembangan teknologi informasi telah menghasilkan data dalam jumlah besar (Big Data) di berbagai sektor industri, termasuk ritel. Supermarket sebagai salah satu pelaku bisnis ritel menghasilkan ribuan data transaksi setiap harinya. Data-data ini menyimpan potensi insight berharga yang dapat digunakan untuk pengambilan keputusan strategis, seperti pengelolaan stok, penjadwalan karyawan, evaluasi program loyalitas, hingga strategi pemasaran.

Namun, data mentah tidak memiliki nilai tanpa melalui proses analisis yang sistematis. Di sinilah peran Data Science dan tools visualisasi data seperti Tableau menjadi krusial. Dengan Tableau, data transaksi dapat divisualisasikan, dianalisis trennya, dan disajikan dalam bentuk dashboard interaktif yang mudah dipahami oleh para pemangku kepentingan.

Penelitian ini menggunakan dataset **Supermarket Sales** yang diperoleh dari platform Kaggle. Dataset ini mencatat 1.000 transaksi dari tiga cabang supermarket di tiga kota (Yangon, Mandalay, Naypyitaw) selama periode 1 Januari hingga 9 Maret 2019. Dengan 17 kolom informasi yang mencakup data transaksi, produk, pelanggan, dan rating kepuasan, dataset ini memberikan gambaran yang cukup komprehensif untuk menganalisis faktor-faktor yang mempengaruhi penjualan dan kepuasan pelanggan.

**Relevansi dengan Konsep Big Data (5V):**

| V | Penjelasan | Implementasi pada Dataset |
|---|-----------|--------------------------|
| **Volume** | Jumlah data yang besar | Dataset berisi 1.000 baris transaksi — skala yang cukup untuk analisis retail skala menengah |
| **Velocity** | Kecepatan data masuk | Data transaksi tercatat dengan timestamp per transaksi (Date + Time), mencerminkan aliran data dari sistem POS |
| **Variety** | Keragaman tipe data | 17 kolom dengan tipe data beragam: numerik (Total, Quantity, Rating), kategorikal (Branch, Product line, Payment), temporal (Date, Time), dan tekstual (Invoice ID) |
| **Veracity** | Kualitas dan akurasi | Dataset bersih tanpa missing value, namun merupakan data sintetis sehingga preprocessing tetap perlu didokumentasikan secara transparan |
| **Value** | Nilai bisnis yang dapat diekstrak | Analisis menghasilkan rekomendasi strategis: optimasi stok produk, evaluasi program member, dan peningkatan kepuasan pelanggan |

#### 1.2. Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian ini adalah:

*"Faktor-faktor apa yang paling mempengaruhi total penjualan dan tingkat kepuasan pelanggan di ketiga cabang supermarket, dan bagaimana strategi yang dapat diterapkan untuk meningkatkan pendapatan serta loyalitas pelanggan?"*

#### 1.3. Pertanyaan Bisnis

Untuk menjawab rumusan masalah di atas, dirumuskan pertanyaan bisnis utama dan lima sub-pertanyaan analitik:

**Pertanyaan Bisnis Utama:**
Faktor-faktor apa yang paling mempengaruhi total penjualan dan tingkat kepuasan pelanggan di ketiga cabang supermarket, dan bagaimana strategi yang dapat diterapkan untuk meningkatkan pendapatan serta loyalitas pelanggan?

**Sub-Pertanyaan Analitik:**
1. Bagaimana tren penjualan harian dan mingguan di setiap cabang selama periode Jan-Mar 2019? Apakah ada pola musiman atau hari tertentu yang menunjukkan lonjakan penjualan?
2. Kategori produk apa yang paling berkontribusi terhadap total pendapatan dan memiliki margin keuntungan tertinggi? Apakah ada perbedaan preferensi produk antar cabang?
3. Bagaimana pengaruh tipe pelanggan (Member vs Normal) dan metode pembayaran terhadap nilai transaksi dan rating kepuasan?
4. Apakah terdapat korelasi antara rating kepuasan dengan nilai transaksi, jumlah item, atau waktu transaksi?
5. Metode pembayaran apa yang paling dominan digunakan oleh tiap segmen pelanggan dan bagaimana pengaruhnya terhadap frekuensi pembelian?

#### 1.4. Tujuan Penelitian

Tujuan dari penelitian ini adalah:
1. Menganalisis tren penjualan harian dan mingguan di setiap cabang supermarket
2. Mengidentifikasi kategori produk yang paling berkontribusi terhadap pendapatan
3. Mengevaluasi efektivitas program member dan preferensi metode pembayaran
4. Mengukur korelasi antara rating kepuasan dengan variabel transaksi
5. Membangun dashboard interaktif menggunakan Tableau untuk monitoring kinerja
6. Menyusun rekomendasi strategis berdasarkan temuan analisis

#### 1.5. Manfaat Penelitian

**Bagi Manajemen Supermarket:**
- Mendapatkan insight tentang pola penjualan per cabang, per produk, dan per waktu
- Dasar pengambilan keputusan untuk optimasi stok, jadwal karyawan, dan promosi

**Bagi Tim Marketing:**
- Evaluasi efektivitas program member
- Identifikasi produk yang perlu dipromosikan atau ditingkatkan kualitasnya

**Bagi Tim Keuangan:**
- Analisis pendapatan kotor dan margin per kategori produk
- Informasi preferensi metode pembayaran untuk strategi partnership

#### 1.6. Sumber Data dan Posisi dalam Data Lifecycle

Dataset yang digunakan adalah **Supermarket Sales Dataset** yang diunduh dari platform Kaggle.

**Data Lifecycle:**

```
[Sumber: Sistem POS] → [Pengumpulan] → [Penyimpanan: CSV] → [Analisis: Tableau] → [Presentasi: Dashboard]
```

Dataset berada pada tahap penyimpanan (storage) ketika diterima, dan akan diproses melalui tahap analisis hingga presentasi menggunakan Tableau.

**Identifikasi Stakeholder:**

| Stakeholder | Peran | Kepentingan |
|-------------|-------|-------------|
| Manajer Regional | Mengawasi kinerja 3 cabang | Ingin tahu cabang dengan performa terbaik |
| Manajer Cabang | Mengelola operasional harian | Butuh insight pola penjualan untuk stok & shift |
| Tim Marketing | Strategi promosi & loyalitas | Efektivitas program member vs non-member |
| Tim Keuangan | Mengelola pendapatan & pajak | Analisis pendapatan kotor dan margin |

---

### BAB 2: PROFIL DATASET DAN PERSIAPAN DATA

#### 2.1. Sumber Data

Dataset **Supermarket Sales** diperoleh dari platform Kaggle. Dataset ini merupakan data transaksi penjualan dari sebuah perusahaan supermarket fiksi yang memiliki 3 cabang di 3 kota besar di Myanmar.

| Metrik | Nilai |
|--------|-------|
| Platform | Kaggle |
| URL | https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales |
| Format | CSV |
| Jumlah Baris | 1.000 transaksi |
| Jumlah Kolom | 17 field |
| Ukuran File | ~30 KB |

#### 2.2. Deskripsi Dataset

Dataset ini mencatat transaksi penjualan selama 3 bulan (1 Januari – 9 Maret 2019) dari tiga cabang supermarket:

| # | Nama Field | Tipe Data | Deskripsi |
|---|------------|-----------|-----------|
| 1 | Invoice ID | String | Nomor unik setiap transaksi |
| 2 | Branch | String | Kode cabang (A, B, C) |
| 3 | City | String | Kota cabang (Yangon, Mandalay, Naypyitaw) |
| 4 | Customer type | String | Tipe pelanggan (Member/Normal) |
| 5 | Gender | String | Jenis kelamin (Male/Female) |
| 6 | Product line | String | Kategori produk (6 kategori) |
| 7 | Unit price | Number | Harga satuan produk ($10.08–$99.96) |
| 8 | Quantity | Number | Jumlah unit yang dibeli (1–10) |
| 9 | Tax 5% | Number | Pajak 5% dari total transaksi |
| 10 | Total | Number | Total nilai transaksi ($10.68–$1,042.65) |
| 11 | Date | Date (konversi) | Tanggal transaksi (M/D/YYYY) |
| 12 | Time | Time (konversi) | Waktu transaksi (HH:MM) |
| 13 | Payment | String | Metode pembayaran (Cash/Ewallet/Credit card) |
| 14 | cogs | Number | Harga pokok penjualan |
| 15 | gross margin percentage | Number | Persentase margin kotor (~4.76%) |
| 16 | gross income | Number | Pendapatan kotor |
| 17 | Rating | Number | Rating kepuasan (4.0–10.0) |

#### 2.3. Statistik Dasar Dataset

| Metrik | Nilai |
|--------|-------|
| Total Baris | 1.000 transaksi |
| Rentang Waktu | 1 Januari – 9 Maret 2019 (89 hari) |
| Rentang Jam Operasional | 10:00 – 20:59 |
| Total Pendapatan (Revenue) | $322,966.75 |
| Total HPP (COGS) | $307,587.38 |
| Total Gross Income | $15,379.37 |
| Rata-rata Transaksi | $322.97 |
| Rata-rata Rating | 6.97/10 |
| Rata-rata Unit per Transaksi | 5.51 unit |
| Jumlah Cabang | 3 (Yangon, Mandalay, Naypyitaw) |
| Jumlah Kategori Produk | 6 |
| Metode Pembayaran | 3 (Cash, Ewallet, Credit card) |
| Tipe Pelanggan | Member (50.1%), Normal (49.9%) |

#### 2.4. Verifikasi Tipe Data

Sebelum analisis, dilakukan verifikasi tipe data pada setiap field. Ditemukan bahwa field `Date` dan `Time` masih bertipe String (Text) pada file CSV asli. Kedua field ini perlu dikonversi:

- **Date:** String `M/D/YYYY` → Date — dilakukan langsung di Tableau melalui fitur Change Data Type
- **Time:** String `HH:MM` → dibuat Calculated Field `Hour` untuk ekstraksi jam transaksi

Seluruh field lainnya sudah memiliki tipe data yang sesuai dan tidak memerlukan perubahan.

---

### BAB 3: PEMBERSIHAN DATA

#### 3.1. Pengecekan Missing Values

Langkah pertama dalam pembersihan data adalah memastikan tidak ada data yang hilang (missing values) pada seluruh 17 kolom. Proses pengecekan dilakukan di Tableau dengan cara mendrag seluruh field ke worksheet dan memverifikasi jumlah baris.

*[Insert Gambar 3.1: Screenshot pengecekan missing values]*

**Hasil:** Tidak ditemukan missing values pada seluruh 1.000 baris data. Setiap kolom memiliki 1.000 nilai yang valid. Dataset ini sudah bersih dari sisi kelengkapan data.

#### 3.2. Pengecekan Duplikasi

Pengecekan duplikasi dilakukan dengan membandingkan nilai COUNT (jumlah total) dan COUNTD (jumlah unik) pada kolom Invoice ID.

*[Insert Gambar 3.2: Screenshot pengecekan duplikasi]*

**Hasil:** COUNT(Invoice ID) = 1.000 dan COUNTD(Invoice ID) = 1.000. Tidak ada selisih, yang berarti tidak terdapat data duplikat. Setiap Invoice ID merepresentasikan transaksi yang unik.

#### 3.3. Pengecekan Inkonsistensi Format

Pengecekan dilakukan pada seluruh field kategorikal untuk memastikan konsistensi penulisan.

*[Insert Gambar 3.3: Screenshot pengecekan format kategorikal]*

| Field | Nilai Unik | Konsisten? |
|-------|-----------|:----------:|
| City | Yangon, Mandalay, Naypyitaw | [OK] |
| Branch | A, B, C | [OK] |
| Customer type | Member, Normal | [OK] |
| Gender | Male, Female | [OK] |
| Product line | 6 kategori (capitalized) | [OK] |
| Payment | Cash, Ewallet, Credit card | [OK] |

**Hasil:** Seluruh field kategorikal memiliki format yang konsisten tanpa variasi ejaan.

#### 3.4. Pengecekan Outlier

Outlier dideteksi menggunakan Box Plot (metode IQR) di Tableau. Analisis dilakukan pada field `Total` yang dikelompokkan per cabang, dan `Rating` per kategori produk.

*[Insert Gambar 3.4: Screenshot Box Plot Total per City]*

| Field | Range | Outlier? |
|-------|-------|:--------:|
| Total | $10.68 – $1,042.65 | Tidak ada outlier ekstrem |
| Unit price | $10.08 – $99.96 | Tidak ada outlier |
| Quantity | 1 – 10 unit | Tidak ada outlier |
| Rating | 4.0 – 10.0 | Tidak ada outlier |
| gross income | $0.51 – $49.65 | Tidak ada outlier |

**Hasil:** Tidak ditemukan outlier ekstrem pada seluruh field numerik. Distribusi data relatif normal.

#### 3.5. Tindak Lanjut Pembersihan

Berdasarkan hasil pengecekan di atas, dapat disimpulkan bahwa dataset **Supermarket Sales** sudah dalam kondisi sangat bersih. Tidak ada tindakan pembersihan substansial yang diperlukan. Langkah yang dilakukan hanyalah:

1. **Konversi tipe data Date** dari String ke Date
2. **Konversi tipe data Time** — pembuatan Calculated Field `Hour`
3. **Pembuatan field turunan** untuk memperkaya analisis (Day of Week, Month, Revenue per Unit, dll.)

---

### BAB 4: ANALISIS DATA

#### 4.1. Analisis Tren Waktu

**4.1.1. Tren Penjualan Harian per Cabang**

Visualisasi tren penjualan harian menggunakan Line Chart menunjukkan fluktuasi penjualan di ketiga cabang selama periode Januari hingga Maret 2019.

*[Insert Gambar 4.1: Line Chart Revenue Trend per Cabang]*

Analisis menunjukkan:
- **Naypyitaw** mencatat total revenue tertinggi sebesar **$110,568.71** meskipun memiliki jumlah transaksi paling sedikit (328 transaksi). Ini mengindikasikan bahwa nilai rata-rata transaksi (Average Order Value) di Naypyitaw lebih tinggi dibanding cabang lain.
- **Yangon** mencatat **$106,200.37** dari 340 transaksi — volume transaksi tertinggi namun revenue lebih rendah dari Naypyitaw.
- **Mandalay** mencatat **$106,197.67** dari 332 transaksi — hampir identik dengan Yangon dalam total revenue.

| Metrik | Yangon | Mandalay | Naypyitaw |
|--------|:------:|:--------:|:---------:|
| Total Revenue | $106,200.37 | $106,197.67 | $110,568.71 |
| Jumlah Transaksi | 340 | 332 | 328 |
| Rata-rata Transaksi | $312.35 | $319.87 | **$337.10** |

**4.1.2. Jam Sibuk (Peak Hours)**

Analisis distribusi transaksi per jam mengungkapkan pola aktivitas belanja yang menarik.

*[Insert Gambar 4.4: Bar Chart Hourly Activity]*

| Jam | Jumlah Transaksi | Total Revenue | % dari Total |
|:---:|:----------------:|:------------:|:-----------:|
| 10:00 | 101 | $31,421 | 9.7% |
| 11:00 | 90 | $30,377 | 9.4% |
| 12:00 | 89 | $26,066 | 8.1% |
| 13:00 | 103 | $34,723 | 10.7% |
| 14:00 | 83 | $30,828 | 9.5% |
| 15:00 | 102 | $31,180 | 9.6% |
| 16:00 | 77 | $25,226 | 7.8% |
| 17:00 | 74 | $24,445 | 7.6% |
| 18:00 | 93 | $26,030 | 8.1% |
| **19:00** | **113** | **$39,699** | **12.3%** |
| 20:00 | 75 | $22,970 | 7.1% |

**Insight Utama:** Jam **19:00 (7-8 PM)** adalah puncak aktivitas belanja dengan 113 transaksi dan revenue $39,699.51 — menyumbang 12.3% dari total revenue harian. Sebaliknya, jam 17:00 dan 20:00 cenderung sepi. Pola ini sangat penting untuk penjadwalan staf dan strategi promosi.

#### 4.2. Analisis Produk

**4.2.1. Revenue per Kategori Produk**

*[Insert Gambar 4.2: Bar Chart Product Performance]*

| Product Line | Total Revenue | % Kontribusi | Gross Income |
|-------------|:------------:|:------------:|:------------:|
| Food and beverages | $56,144.84 | 17.38% | $2,673.56 |
| Sports and travel | $55,122.83 | 17.07% | $2,624.90 |
| Electronic accessories | $54,337.53 | 16.82% | $2,587.50 |
| Fashion accessories | $54,305.89 | 16.81% | $2,585.99 |
| Home and lifestyle | $53,861.91 | 16.68% | $2,564.85 |
| Health and beauty | $49,193.74 | 15.23% | $2,342.56 |
| **Total** | **$322,966.74** | **100%** | **$15,379.37** |

**Insight:** Kontribusi revenue relatif merata antar kategori (15-17%). **Food & Beverages** unggul tipis sebagai kategori terlaris. **Health & Beauty** menempati posisi terendah. Semua kategori memiliki margin kotor yang seragam (~4.76%).

**4.2.2. Rating per Kategori Produk**

*[Insert Gambar 4.3: Bar Chart Rating per Product Line]*

| Product Line | Average Rating | Ranking |
|-------------|:------------:|:-------:|
| Food and beverages | 7.11 | [1] |
| Fashion accessories | 7.03 | [2] |
| Health and beauty | 7.00 | [3] |
| Sports and travel | 6.92 | 4 |
| Electronic accessories | 6.92 | 5 |
| Home and lifestyle | 6.84 | 6 |

**Insight:** **Food & Beverages** tidak hanya unggul dari sisi revenue, tetapi juga mendapat rating kepuasan tertinggi (7.11). **Home & Lifestyle** memiliki rating terendah (6.84) — perlu evaluasi kualitas atau variasi produk di kategori ini.

**4.2.3. Preferensi Produk per Cabang**

*[Insert Gambar 4.5: Heatmap Produk per Cabang]*

| Produk \ City | Mandalay | Naypyitaw | Yangon |
|--------------|:--------:|:---------:|:------:|
| Electronic accessories | $17,051 | $18,969 | $18,317 |
| Fashion accessories | $16,413 | $21,560 | $16,333 |
| Food and beverages | $15,215 | **$23,767** | $17,163 |
| Health and beauty | $19,981 | $16,615 | $12,598 |
| Home and lifestyle | $17,549 | $13,896 | **$22,417** |
| Sports and travel | $19,988 | $15,762 | $19,373 |

**Insight:** Terdapat perbedaan preferensi produk yang signifikan antar cabang:
- **Naypyitaw:** Dominasi Food & Beverages ($23,767) dan Fashion accessories ($21,560)
- **Yangon:** Unggul di Home & Lifestyle ($22,417) dan Sports & Travel ($19,373)
- **Mandalay:** Cenderung merata dengan Sports & Travel ($19,988) dan Health & Beauty ($19,981) sebagai yang tertinggi

Temuan ini mengindikasikan bahwa strategi promosi dan pengelolaan stok perlu disesuaikan per cabang.

#### 4.3. Analisis Pelanggan

**4.3.1. Perbandingan Member vs Normal**

Analisis membandingkan dua tipe pelanggan: Member (pelanggan terdaftar) dan Normal (pelanggan umum).

| Metrik | Member | Normal | Selisih |
|--------|:------:|:------:|:-------:|
| Jumlah Transaksi | 501 (50.1%) | 499 (49.9%) | +2 |
| Total Revenue | $164,223.44 | $158,743.31 | +$5,480.13 |
| Rata-rata per Transaksi | **$327.79** | $318.12 | +$9.67 (+3%) |
| Rata-rata Rating | 6.94 | **7.01** | -0.07 |

**Insight:** Member menghabiskan **$9.67 lebih banyak** per transaksi (+3%) dibanding pelanggan Normal. Ini menunjukkan program Member sudah cukup efektif dalam meningkatkan nilai transaksi. Namun, rating Member sedikit lebih rendah (6.94 vs 7.01) — kemungkinan karena ekspektasi yang lebih tinggi dari pelanggan terdaftar.

**4.3.2. Analisis Metode Pembayaran**

| Metode | Jumlah Transaksi | % | Total Revenue | Avg Rating |
|--------|:----------------:|:-:|:------------:|:----------:|
| Cash | 344 | 34.4% | $112,206.57 | 6.97 |
| Ewallet | 345 | 34.5% | $109,993.11 | 6.95 |
| Credit card | 311 | 31.1% | $100,767.07 | 7.00 |

**Insight:** Cash dan Ewallet sama-sama dominan (~34.5% masing-masing). Credit card adalah metode pembayaran yang paling jarang digunakan (31.1%). Pengguna Credit card memberi rating sedikit lebih tinggi (7.00).

#### 4.4. Analisis Korelasi

**4.4.1. Korelasi Total vs Rating**

*[Insert Gambar: Scatter Plot Total vs Rating]*

Analisis korelasi menggunakan scatter plot menunjukkan bahwa tidak terdapat hubungan linear antara nilai transaksi (Total) dengan rating kepuasan. Nilai R² mendekati 0, yang berarti tidak ada korelasi signifikan. Pelanggan dengan transaksi kecil ($10) dapat memberikan rating tinggi (10), dan sebaliknya pelanggan dengan transaksi besar ($1,000) dapat memberikan rating rendah (4).

**4.4.2. Korelasi Quantity vs Rating**

Hasil yang sama ditemukan pada analisis antara jumlah item (Quantity) dengan rating. Jumlah produk yang dibeli tidak mempengaruhi tingkat kepuasan pelanggan.

**Insight:** Kepuasan pelanggan tidak ditentukan oleh seberapa banyak mereka berbelanja atau seberapa besar nilai transaksi mereka. Faktor yang lebih berpengaruh adalah **kualitas layanan** dan **kualitas produk** itu sendiri.

#### 4.5. Calculated Fields

Untuk memperkaya analisis, dibuat 7 Calculated Fields di Tableau:

| # | Nama Field | Formula | Fungsi |
|:-:|-----------|---------|--------|
| 1 | Hour | `INT(LEFT([Time], 2))` | Ekstrak jam dari Time string |
| 2 | Day of Week | `DATENAME('weekday', [Date])` | Nama hari untuk analisis mingguan |
| 3 | Month | `DATENAME('month', [Date])` | Nama bulan untuk analisis bulanan |
| 4 | Revenue per Unit | `[Total] / [Quantity]` | Harga rata-rata per unit |
| 5 | Rating Category | `IF [Rating]>=9 THEN "High" ELSEIF [Rating]>=7 THEN "Medium" ELSE "Low" END` | Kategorisasi rating |
| 6 | Transaction Size | `IF [Quantity]>=7 THEN "Large" ELSEIF [Quantity]>=4 THEN "Medium" ELSE "Small" END` | Ukuran transaksi |
| 7 | Week Number | `DATEPART('week', [Date])` | Nomor minggu dalam tahun |

*[Insert Gambar CF: Screenshot daftar Calculated Fields di panel Data Tableau]*

#### 4.6. Ringkasan Temuan Analisis

| # | Temuan | Detail | Implikasi Bisnis |
|:-:|--------|--------|-----------------|
| 1 | Naypyitaw memiliki revenue tertinggi | $110,568 — AOV $337.10 | Cabang Naypyitaw sebagai role model |
| 2 | Peak hour di jam 19:00 | 113 transaksi, $39,699 revenue | Tambah staf di jam sibuk |
| 3 | Food & Beverages terpopuler | $56,144 revenue & rating 7.11 | Prioritaskan stok F&B |
| 4 | Member spend 3% lebih tinggi | $327.79 vs $318.12 | Program member cukup efektif |
| 5 | Tidak ada korelasi Total-Rating | Scatter plot acak | Fokus pada kualitas layanan |
| 6 | Cash & Ewallet dominan | Masing-masing ~34.5% | Pertahankan fleksibilitas pembayaran |
| 7 | Mandalay rating terendah | 6.82 vs 7.07 Naypyitaw | Investigasi kualitas layanan |
| 8 | Naypyitaw dominan F&B | $23,767 dari F&B | Promosi lintas kategori |
| 9 | Yangon dominan Home & Lifestyle | $22,417 | Perkuat branding kategori ini |
| 10 | Kategori merata | 5 kategori ~$54K | Diversifikasi berjalan baik |

---

### BAB 5: DASHBOARD INTERAKTIF

#### 5.1. Komponen Dashboard

Dashboard interaktif dibangun menggunakan Tableau Desktop dengan komponen sebagai berikut:

| Komponen | Jumlah | Detail |
|----------|:------:|--------|
| Sheet Visualisasi | 6 sheet | Revenue Trend, Product Performance, Customer Analysis, Hourly Activity, City Comparison, Rating Distribution |
| Quick Filter | 2 filter | City (drop-down), Product line (drop-down) |
| Filter Action | 2 action | Filter by City, Filter by Product |
| Parameter | 1 parameter | Top N Products (1-6) |

#### 5.2. Layout Dashboard

*[Insert Gambar 5.1: Full Dashboard Screenshot — LAYAR PENUH]*

Dashboard terdiri dari 6 sheet yang diatur dalam layout grid:

| Baris | Kiri | Kanan |
|:-----:|:----:|:-----:|
| **Header** | Judul + Quick Filters (City, Product line) | |
| **Baris 1** | Revenue Trend (Line Chart) | Product Performance (Bar Chart) |
| **Baris 2** | Customer Analysis (Stacked Bar) | Hourly Activity (Bar Chart) |
| **Baris 3** | City Comparison (Side-by-side Bar) — Full width | |
| **Footer** | Parameter: Top N Products | |

#### 5.3. Interaktivitas Dashboard

**Quick Filter — City:**
Pengguna dapat memilih cabang tertentu (Yangon/Mandalay/Naypyitaw) dari drop-down filter. Seluruh sheet akan menampilkan data hanya untuk cabang yang dipilih.

**Quick Filter — Product line:**
Pengguna dapat memilih kategori produk tertentu untuk melihat performanya di semua sheet.

**Filter Action — Klik Cabang:**
Dengan mengklik salah satu garis cabang di sheet Revenue Trend, seluruh sheet lain akan otomatis terfilter untuk cabang tersebut. Fitur ini memungkinkan eksplorasi data yang intuitif.

*[Insert Gambar 5.2: Dashboard saat difilter untuk Naypyitaw]*

*[Insert Gambar 5.3: Konfigurasi Filter Action]*

**Parameter — Top N Products:**
Parameter ini memungkinkan pengguna memilih jumlah produk teratas (1-6) yang ditampilkan berdasarkan revenue. Saat parameter diubah, sheet Product Performance akan menyesuaikan jumlah bar yang ditampilkan.

#### 5.4. Panduan Penggunaan

1. **Memfilter per Cabang:** Gunakan drop-down "City" di bagian atas dashboard
2. **Memfilter per Produk:** Gunakan drop-down "Product line" di bagian atas
3. **Eksplorasi Interaktif:** Klik cabang di chart Revenue Trend untuk filter action
4. **Mengatur Top N:** Ubah slider parameter "Top N Products" untuk melihat N produk teratas
5. **Reset Filter:** Klik tombol "Show All" atau tanda X pada filter untuk mereset

---

### BAB 6: KESIMPULAN DAN REKOMENDASI

#### 6.1. Kesimpulan

Berdasarkan analisis data 1.000 transaksi dari tiga cabang supermarket (Yangon, Mandalay, Naypyitaw) selama periode Januari hingga Maret 2019, berikut adalah kesimpulan yang diperoleh:

**1. Faktor yang Mempengaruhi Penjualan:**
- **Lokasi cabang** merupakan faktor paling signifikan — Naypyitaw mencatat revenue tertinggi ($110,568) meskipun jumlah transaksi paling sedikit, menunjukkan efektivitas operasional yang lebih baik
- **Waktu transaksi** sangat mempengaruhi volume penjualan — jam 19:00 adalah peak hour dengan 113 transaksi dan revenue $39,699
- **Kategori produk** memiliki pengaruh moderat — Food & Beverages unggul tipis dengan kontribusi 17.38%
- **Tipe pelanggan** memiliki pengaruh kecil namun positif — Member menghabiskan 3% lebih banyak per transaksi

**2. Faktor yang Mempengaruhi Kepuasan Pelanggan:**
- Kepuasan pelanggan **tidak dipengaruhi** oleh nilai transaksi atau jumlah item yang dibeli
- Faktor yang lebih berpengaruh adalah kategori produk (F&B rating tertinggi 7.11) dan lokasi cabang (Naypyitaw 7.07 vs Mandalay 6.82)
- Hal ini mengindikasikan bahwa **kualitas layanan dan produk** lebih penting daripada nominal belanja dalam membentuk kepuasan

**3. Kondisi Data:**
- Dataset sudah sangat bersih — 0 missing values, 0 duplikasi, format konsisten
- Tidak diperlukan pembersihan substansial, hanya konversi tipe data Date dan Time

#### 6.2. Rekomendasi

**Prioritas Tinggi (P1):**

**1. Optimasi Jam Operasional**
- Tambahkan 2 kasir tambahan pada shift 18:30-20:00 di semua cabang untuk mengatasi peak hour
- Terapkan "Happy Hour Promo" di jam sepi (17:00-18:00) untuk meratakan distribusi transaksi
- Target: Meningkatkan revenue jam sepi sebesar 15%

**2. Tingkatkan Program Member**
- Implementasi tiered membership (Silver/Gold/Platinum) berdasarkan frekuensi belanja
- Program referral: Member yang mereferensikan pelanggan Normal mendapat poin reward
- Member-only promo untuk kategori dengan rating rendah (Home & Lifestyle)
- Target: Meningkatkan rasio member dari 50.1% menjadi 60%

**Prioritas Sedang (P2):**

**3. Strategi Produk per Cabang**
- Naypyitaw: Fokus stok dan promosi Food & Beverages serta Fashion accessories
- Yangon: Perkuat display dan promosi Home & Lifestyle serta Sports & Travel
- Mandalay: Optimasi Health & Beauty dan perbaikan kualitas layanan (rating terendah)

**4. Investigasi Rating Mandalay**
- Lakukan survei kepuasan pelanggan khusus untuk cabang Mandalay
- Evaluasi kualitas layanan staf dan kebersihan toko
- Target: Meningkatkan rating Mandalay dari 6.82 ke 7.0

**Prioritas Rendah (P3):**

**5. Promosi Credit Card**
- Tawarkan diskon 2% untuk pembayaran Credit Card
- Kerja sama dengan bank untuk promo cicilan 0%
- Target: Meningkatkan penggunaan Credit Card dari 31.1% ke 35%

#### 6.3. Keterbatasan Penelitian

| Keterbatasan | Dampak | Mitigasi |
|-------------|--------|----------|
| Data hanya mencakup 3 bulan | Tidak dapat mendeteksi pola musiman tahunan | Gunakan sebagai baseline monitoring |
| Dataset bersifat sintetis | Pola mungkin tidak mencerminkan realitas sempurna | Validasi dengan data tambahan |
| Tidak ada data biaya operasional | Tidak dapat menghitung profitabilitas bersih | Fokus pada revenue dan gross income |
| Rating bersifat subjektif | Interpretasi rating bisa bervariasi | Analisis berdasarkan tren, bukan absolut |
| Tidak ada data kompetitor | Tidak bisa benchmarking | Tambahkan data kompetitor jika tersedia |

#### 6.4. Saran Penelitian Lanjutan

1. Analisis year-over-year dengan data multi-tahun untuk mengidentifikasi tren jangka panjang
2. Segmentasi pelanggan lebih granular berdasarkan frekuensi belanja dan kategori favorit (RFM Analysis)
3. Analisis profitabilitas bersih dengan memperhitungkan biaya sewa, gaji, dan utilitas per cabang
4. Analisis pengaruh promosi diskon terhadap volume penjualan dan loyalitas pelanggan (A/B Testing)
5. Analisis sentimen ulasan pelanggan jika tersedia data kualitatif

---

### DAFTAR PUSTAKA

1. Aung Pyae. (2019). *Supermarket Sales Dataset*. Kaggle. https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales
2. Tableau Software. (2024). *Tableau Desktop Documentation*. https://help.tableau.com
3. [Materi kuliah Big Data Science — pertemuan 1-14]
4. [Referensi buku/textbook yang digunakan]

### LAMPIRAN

**Lampiran 1:** Perhitungan Statistik Detail
**Lampiran 2:** Screenshot Tambahan Proses di Tableau
**Lampiran 3:** Daftar Lengkap Calculated Fields
**Lampiran 4:** Dokumentasi Filter Action dan Parameter

---

## FORMATTING UNTUK WORD

| Elemen | Setting |
|--------|---------|
| Font | Times New Roman / Calibri, 12pt |
| Spasi | 1.5 lines |
| Margin | 3 cm (kiri, kanan, atas, bawah) |
| Judul Bab | Bold, 14pt |
| Sub-bab | Bold, 12pt |
| Tabel | Center, font 10-11pt |
| Caption Gambar | Center, italic, 10pt, "Gambar X.Y: ..." |
| Caption Tabel | Center, bold, 10pt, "Tabel X.Y: ..." |
| Numbering | 1, 1.1, 1.1.1 |
| Halaman | Bottom center |

**Estimasi Halaman (dengan screenshot):**
| Bab | Estimasi Hal |
|-----|:-----------:|
| Cover | 1 hal |
| Bab 1 | 3 hal |
| Bab 2 | 2 hal |
| Bab 3 | 3 hal (banyak screenshot) |
| Bab 4 | 6 hal (terberat) |
| Bab 5 | 3 hal |
| Bab 6 | 2 hal |
| Daftar Pustaka | 1 hal |
| Lampiran | 1-2 hal |
| **Total** | **~20 hal** [OK] |
