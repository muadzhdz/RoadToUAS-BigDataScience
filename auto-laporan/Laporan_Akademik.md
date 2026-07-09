# PENDAHULUAN

## Latar Belakang

Dalam era Big Data, analisis data transaksi ritel menjadi sangat penting untuk memahami perilaku konsumen, mengoptimalkan operasi bisnis, dan meningkatkan keuntungan. Supermarket sebagai salah satu sektor ritel yang besar menghasilkan volume data transaksi yang signifikan setiap harinya melalui sistem Point of Sale (POS). Data yang terkumpul meliputi informasi produk, harga, jumlah pembelian, metode pembayaran, hingga tingkat kepuasan pelanggan. Dengan menganalisis data ini secara sistematis, manajemen dapat membuat keputusan berbasis data yang lebih akurat dan strategis.

Domain dataset dalam penelitian ini adalah ritel supermarket, dengan **Supermarket Sales Dataset** yang diperoleh dari Kaggle sebagai sumber data. Dataset ini merepresentasikan data transaksi penjualan dari sebuah perusahaan supermarket fiktif yang memiliki tiga cabang di tiga kota besar di Myanmar, yaitu Yangon, Mandalay, dan Naypyitaw. Dataset mencakup 1.000 transaksi selama periode 3 bulan (Januari – Maret 2019) dengan 17 kolom informasi yang mencakup detail transaksi, produk, pelanggan, dan metrik kepuasan.

### Relevansi Big Data 5V

Dataset ini dianalisis menggunakan kerangka kerja Big Data 5V (Ruscom, 2014):

1. **Volume** — 1.000 baris transaksi data penjualan supermarket
2. **Velocity** — Data transaksi harian dengan timestamp, mencerminkan aliran data real-time dari sistem POS
3. **Variety** — 17 kolom dengan tipe data beragam: numerik, kategorikal, temporal, dan tekstual
4. **Veracity** — Dataset bersih tanpa missing values, namun sintetis sehingga memiliki konsistensi tinggi
5. **Value** — Analisis menghasilkan insight strategis untuk optimasi bisnis supermarket

### Pemangku Kepentingan (Stakeholder)

| Stakeholder | Peran | Kepentingan |
|-------------|-------|-------------|
| Manajer Regional | Mengawasi kinerja 3 cabang | Mengetahui cabang dengan kinerja terbaik dan faktor pendorongnya |
| Manajer Cabang | Mengelola operasional harian | Insight pola penjualan per produk dan jam sibuk untuk mengatur stok dan shift |
| Tim Marketing | Menyusun strategi promosi dan loyalitas | Efektivitas program member vs non-member, produk yang perlu dipromosikan |
| Tim Keuangan | Mengelola pendapatan dan pajak | Analisis pendapatan kotor, margin, dan tren biaya |

### Posisi dalam Data Lifecycle

Siklus hidup data dalam analisis ini mengikuti alur:

```
[Sumber Data] → [Pengumpulan] → [Penyimpanan] → [Analisis] → [Presentasi]
     (POS)        (CSV File)      (Database)     (Tableau)     (Dashboard)
```

Dataset berada pada tahap penyimpanan dan diproses melalui tahap analisis hingga presentasi sesuai alur kerja data analyst.

## Rumusan Masalah

Berdasarkan latar belakang di atas, rumusan masalah dalam penelitian ini adalah:

1. Bagaimana karakteristik dan kualitas dataset penjualan supermarket ditinjau dari perspektif Big Data (5V)?
2. Bagaimana tren penjualan harian dan mingguan di setiap cabang selama periode Januari–Maret 2019? Apakah ada pola musiman atau hari tertentu yang menunjukkan lonjakan penjualan?
3. Kategori produk apa yang paling berkontribusi terhadap total pendapatan dan memiliki tingkat kepuasan tertinggi? Apakah ada perbedaan preferensi produk antar cabang?
4. Bagaimana pengaruh tipe pelanggan (Member vs Normal) dan metode pembayaran terhadap nilai transaksi dan rating kepuasan?
5. Apakah terdapat korelasi antara rating kepuasan dengan nilai transaksi, jumlah item, atau waktu transaksi?
6. Bagaimana merancang dan membangun dashboard interaktif yang dapat memvisualisasikan seluruh temuan analisis secara komprehensif?

## Tujuan Penelitian

Tujuan dari penelitian ini adalah:

1. Melakukan analisis profil dan kualitas data pada dataset Supermarket Sales menggunakan pendekatan Big Data 5V.
2. Mengidentifikasi pola tren penjualan harian dan mingguan di ketiga cabang supermarket.
3. Menentukan kategori produk yang paling berkontribusi terhadap total pendapatan serta menganalisis preferensi produk per cabang.
4. Menganalisis pengaruh tipe pelanggan (Member vs Normal) dan metode pembayaran terhadap nilai transaksi dan rating kepuasan.
5. Mengidentifikasi korelasi antara rating kepuasan dengan variabel transaksi lainnya.
6. Membangun dashboard interaktif Tableau yang komprehensif untuk visualisasi hasil analisis.
7. Menyusun rekomendasi strategis berbasis data untuk peningkatan kinerja bisnis supermarket.


# PROFILING DAN PERSIAPAN DATA

## Dataset

### Sumber Dataset

Dataset yang digunakan dalam penelitian ini adalah **Supermarket Sales Dataset** yang berasal dari Kaggle (Kaggle, 2019). Dataset ini merupakan dataset transaksi penjualan supermarket fiktif yang memiliki tiga cabang di tiga kota besar di Myanmar.

| Metrik | Nilai |
|--------|-------|
| **Sumber** | Kaggle — Supermarket Sales Dataset |
| **Kolektor** | Aung Pyae Ap |
| **Jumlah Instance** | 1.000 transaksi |
| **Jumlah Kolom** | 17 field |
| **Rentang Waktu** | 1 Januari 2019 – 9 Maret 2019 (89 hari) |
| **Rentang Jam** | 10:00 – 20:59 |
| **Total Pendapatan** | \$322,966.75 |
| **Total HPP (COGS)** | \$307,587.38 |
| **Total Gross Income** | \$15,379.37 |
| **Rata-rata Rating** | 6.97 / 10 |
| **Tipe Pelanggan** | Member (50.1%), Normal (49.9%) |

### Informasi Fitur

Dataset memiliki 17 kolom yang terdiri dari identifier transaksi, data demografi, detail produk, metrik keuangan, dan metrik kepuasan:

\footnotesize

| No | Nama Field | Tipe Data | Deskripsi |
|:--:|-----------|:---------:|-----------|
| 1 | Invoice ID | String (Text) | Nomor unik setiap transaksi — identifier utama |
| 2 | Branch | String (Kategorikal) | Kode cabang: A (Yangon), B (Mandalay), C (Naypyitaw) |
| 3 | City | String (Kategorikal) | Kota lokasi cabang |
| 4 | Customer type | String (Kategorikal) | Tipe pelanggan: Member / Normal |
| 5 | Gender | String (Kategorikal) | Jenis kelamin: Male / Female |
| 6 | Product line | String (Kategorikal) | Kategori produk (6 kategori) |
| 7 | Unit price | Numerik (Decimal) | Harga satuan per produk (USD) |
| 8 | Quantity | Numerik (Integer) | Jumlah unit produk yang dibeli |
| 9 | Tax 5% | Numerik (Decimal) | Pajak 5% dari total transaksi |
| 10 | Total | Numerik (Decimal) | Total nilai transaksi setelah pajak |
| 11 | Date | Date (Tanggal) | Tanggal transaksi |
| 12 | Time | Time (Waktu) | Jam transaksi |
| 13 | Payment | String (Kategorikal) | Metode pembayaran: Cash, Ewallet, Credit card |
| 14 | cogs | Numerik (Decimal) | Cost of Goods Sold — Harga pokok penjualan |
| 15 | gross margin percentage | Numerik (Decimal) | Persentase margin kotor (4.76% konstan) |
| 16 | gross income | Numerik (Decimal) | Pendapatan kotor (Total - cogs) |
| 17 | Rating | Numerik (Decimal) | Rating kepuasan pelanggan (1–10) |

\normalsize

### Distribusi Data per Cabang

| Cabang | Kota | Jumlah Transaksi | Total Revenue | Rata-rata Rating |
|:------:|:----:|:----------------:|:-------------:|:----------------:|
| A | Yangon | 340 | \$106,200.37 | 7.03 |
| B | Mandalay | 332 | \$106,197.67 | 6.82 |
| C | Naypyitaw | 328 | \$110,568.71 | 7.07 |

## Pengecekan Tipe Data

Pengecekan tipe data dilakukan dengan membandingkan tipe data hasil impor CSV dengan tipe data yang seharusnya:

\footnotesize

| Field | Tipe Saat Ini (CSV) | Seharusnya | Perlu Diubah? |
|-------|--------------------|------------|:-------------:|
| Invoice ID | String | String | [Tidak] |
| Branch | String | String (Kategorikal) | [Tidak] |
| City | String | String (Kategorikal) | [Tidak] |
| Customer type | String | String (Kategorikal) | [Tidak] |
| Gender | String | String (Kategorikal) | [Tidak] |
| Product line | String | String (Kategorikal) | [Tidak] |
| Unit price | Numerik | Number (Decimal) | [Tidak] |
| Quantity | Numerik | Number (Integer) | [Tidak] |
| Tax 5% | Numerik | Number (Decimal) | [Tidak] |
| Total | Numerik | Number (Decimal) | [Tidak] |
| **Date** | **String (M/D/YYYY)** | **Date** | **[Ya] — Parse ke Date** |
| **Time** | **String (HH:MM)** | **Time** | **[Ya] — Parse ke Time** |
| Payment | String | String (Kategorikal) | [Tidak] |
| cogs | Numerik | Number (Decimal) | [Tidak] |
| gross margin percentage | Numerik | Number (Decimal) | [Tidak] |
| gross income | Numerik | Number (Decimal) | [Tidak] |
| Rating | Numerik | Number (Decimal) | [Tidak] |

\normalsize

Dua kolom (Date dan Time) perlu dikonversi dari String ke tipe Date dan Time. Proses konversi dilakukan langsung di Tableau melalui tab Data Source. Berikut adalah tampilan data source setelah konversi:

![Data Source Tableau](Proyek_BigData/assets/Data-Source.jpg)


# PEMBERSIHAN DATA

## Pengecekan Missing Values dan Duplikasi

Hasil pengecekan menggunakan Tableau menunjukkan:

- **Missing Values**: 0 null dari 1.000 baris × 17 kolom — dataset sangat bersih, tidak diperlukan tindakan imputasi
- **Duplikasi**: COUNT(Invoice ID) = 1.000 dan COUNTD(Invoice ID) = 1.000 — tidak ada duplikasi, setiap transaksi unik

![Pengecekan Kualitas Data](Proyek_BigData/assets/Data-Quality.jpg)

## Pengecekan Inkonsistensi Format Kategorikal

| Field | Nilai Unik | Format Konsisten? |
|-------|-----------|:-----------------:|
| City | Yangon, Mandalay, Naypyitaw | [OK] |
| Branch | A, B, C | [OK] |
| Customer type | Member, Normal | [OK] |
| Gender | Male, Female | [OK] |
| Product line | 6 kategori (capitalized consistently) | [OK] |
| Payment | Cash, Ewallet, Credit card | [OK] |

Semua nilai kategorikal sudah konsisten tanpa perlu standarisasi.

## Pengecekan Outlier

**Box Plot Total per City**: Nilai Total berkisar \$10.68–\$1,042.65, tidak ada outlier signifikan per cabang. Distribusi total transaksi relatif seragam antar cabang.

![Box Plot Total per City](Proyek_BigData/assets/Box-Plot-Total.jpg)

**Box Plot Rating per Product Line**: Rating 4.0–10.0, tidak ada outlier ekstrem, sebaran normal di semua kategori produk.

![Box Plot Rating per Product Line](Proyek_BigData/assets/Box-Plot-Rating.jpg)

## Validasi Numerik

| Field | Nilai Min | Nilai Max | Range Wajar? |
|-------|-----------|-----------|:------------:|
| Unit price | \$10.08 | \$99.96 | [OK] |
| Quantity | 1 | 10 | [OK] |
| Tax 5% | \$0.51 | \$49.65 | [OK] |
| Total | \$10.68 | \$1,042.65 | [OK] |
| cogs | \$10.16 | \$993.00 | [OK] |
| gross income | \$0.51 | \$49.65 | [OK] |

**Verifikasi Relasi**: Semua konsisten — Total = cogs + gross income, Tax 5% = Total × 5/105.

## Ringkasan Pembersihan Data

| Aspek | Status | Detail |
|-------|:-----:|--------|
| Missing Values | [OK] Bersih | 0 null dari 1.000 baris × 17 kolom |
| Duplikasi | [OK] Bersih | 0 duplikat |
| Inkonsistensi Format | [OK] Bersih | Semua nilai kategorikal konsisten |
| Outlier | [OK] Bersih | Tidak ada outlier ekstrem |
| Konversi Date | [OK] Selesai | String → Date (M/D/YYYY) |
| Konversi Time | [OK] Selesai | String → Time / Hour extracted |


# ANALISIS EKSPLORATIF DAN MENDALAM

## Feature Engineering (Calculated Fields)

Untuk memperkaya analisis, dibuat 7 calculated field di Tableau:

| No | Nama Field | Formula | Kegunaan |
|:--:|-----------|---------|----------|
| 1 | **Hour** | `INT(LEFT([Time], 2))` | Ekstrak jam dari Time untuk analisis jam sibuk |
| 2 | **Day of Week** | `DATENAME('weekday', [Date])` | Nama hari untuk analisis pola mingguan |
| 3 | **Month** | `DATENAME('month', [Date])` | Nama bulan untuk analisis tren bulanan |
| 4 | **Revenue per Unit** | `[Total] / [Quantity]` | Harga rata-rata per unit yang terjual |
| 5 | **Rating Category** | `IF [Rating] >= 9 THEN "High" ELSEIF [Rating] >= 7 THEN "Medium" ELSE "Low" END` | Kategorisasi rating untuk filter |
| 6 | **Transaction Size** | `IF [Quantity] >= 7 THEN "Large" ELSEIF [Quantity] >= 4 THEN "Medium" ELSE "Small" END` | Ukuran transaksi berdasarkan jumlah item |
| 7 | **Week Number** | `DATEPART('week', [Date])` | Nomor minggu untuk analisis tren mingguan |

## Analisis Distribusi Data

**Distribusi Total Transaksi**: Distribusi miring ke kanan (right-skewed) — mayoritas transaksi bernilai kecil-menengah (\$10–\$400), dengan sedikit transaksi besar (\$800–\$1,042). Pola ini normal untuk data ritel.

**Distribusi Rating**:

| Rating Range | Jumlah Transaksi | Persentase |
|:-----------:|:----------------:|:----------:|
| 4.0 – 5.0 | 174 | 17.4% |
| 6.0 – 7.0 | 345 | 34.5% |
| 8.0 – 9.0 | 330 | 33.0% |
| 10.0 | 151 | 15.1% |

**Insight**: Mayoritas pelanggan memberi rating 6–9 (67.5%). Rating rendah (<5) hanya 17.4%. Tidak ada rating di bawah 4.0.

![Distribusi Rating Pelanggan](Proyek_BigData/assets/Rating-Distribution.jpg)

## Analisis Tren Waktu

**Pertanyaan**: *Bagaimana tren penjualan harian dan mingguan di setiap cabang selama periode Jan–Mar 2019?*

**Tren Penjualan Harian per Cabang**:

| Kota | Jumlah Transaksi | Total Revenue | Avg Transaction Value |
|:----:|:----------------:|:-------------:|:---------------------:|
| Naypyitaw | 328 | \$110,568.71 | **\$337.10** |
| Yangon | 340 | \$106,200.37 | \$312.35 |
| Mandalay | 332 | \$106,197.67 | \$319.87 |

**Insight**: Naypyitaw unggul dalam average transaction value meskipun memiliki volume transaksi paling sedikit. Ketiga cabang menunjukkan pola tren yang relatif paralel, mengindikasikan faktor eksternal (hari libur, cuaca) mempengaruhi semua cabang secara seragam.

![Tren Penjualan Harian per Cabang](Proyek_BigData/assets/Revenue-Trend.jpg)

**Jam Sibuk (Peak Hours)**:

| Jam | Jumlah Transaksi | Total Revenue |
|:---:|:----------------:|:-------------:|
| 10:00 | 101 | \$31,421.48 |
| 13:00 | 103 | \$34,723.23 |
| 15:00 | 102 | \$31,179.51 |
| 19:00 | **113** | **\$39,699.51** (Puncak) |
| 20:00 | 75 | \$22,969.53 |

**Insight**: Jam 19:00 adalah puncak aktivitas belanja dengan 113 transaksi dan revenue \$39,699.51. Jam 17:00–18:00 cenderung sepi.

![Jam Sibuk (Hourly Activity)](Proyek_BigData/assets/Hourly-Activity.jpg)

## Analisis Performa Produk

**Pertanyaan**: *Kategori produk apa yang paling berkontribusi terhadap total pendapatan?*

**Revenue per Product Line**:

| Product Line | Total Revenue | Kontribusi | Avg Rating |
|-------------|:------------:|:----------:|:----------:|
| Food and beverages | \$56,144.84 | **17.38%** | **7.11** |
| Sports and travel | \$55,122.83 | 17.07% | 6.92 |
| Electronic accessories | \$54,337.53 | 16.82% | 6.92 |
| Fashion accessories | \$54,305.89 | 16.81% | 7.03 |
| Home and lifestyle | \$53,861.91 | 16.68% | 6.84 |
| Health and beauty | \$49,193.74 | 15.23% | 7.00 |

**Insight**: Kontribusi relatif merata antar kategori (15–17%). Food & beverages unggul tipis di revenue dan rating. Health & beauty paling rendah di revenue.

![Performa Produk per Kategori](Proyek_BigData/assets/Product-Performance.jpg)

**Preferensi Produk per Cabang (Heatmap)**:

| Produk \ City | Mandalay | Naypyitaw | Yangon |
|--------------|:--------:|:---------:|:------:|
| Electronic accessories | \$17,051 | \$18,969 | \$18,317 |
| Fashion accessories | \$16,413 | \$21,560 | \$16,333 |
| Food and beverages | \$15,215 | **\$23,767** | \$17,163 |
| Health and beauty | \$19,981 | \$16,615 | \$12,598 |
| Home and lifestyle | \$17,549 | \$13,896 | **\$22,417** |
| Sports and travel | \$19,988 | \$15,762 | \$19,373 |

**Insight**:
- **Naypyitaw**: Dominasi Food & beverages (\$23,767) dan Fashion accessories (\$21,560)
- **Yangon**: Unggul di Home & lifestyle (\$22,417) dan Sports & travel (\$19,373)
- **Mandalay**: Cenderung merata dengan Sports & travel (\$19,988) dan Health & beauty (\$19,981) sebagai yang tertinggi

![Perbandingan Antar Cabang](Proyek_BigData/assets/City-Comparison.jpg)

## Analisis Pelanggan

**Pertanyaan**: *Bagaimana pengaruh tipe pelanggan (Member vs Normal) dan metode pembayaran terhadap nilai transaksi dan rating?*

**Perbandingan Member vs Normal**:

| Metrik | Member | Normal | Selisih |
|--------|:------:|:------:|:-------:|
| Jumlah Transaksi | 501 | 499 | +2 |
| Total Revenue | \$164,223.44 | \$158,743.31 | +\$5,480.13 |
| Avg Spend per Transaksi | **\$327.79** | \$318.12 | +\$9.67 (+3%) |
| Avg Rating | 6.94 | **7.01** | -0.07 |

**Insight**: Member menghabiskan \$9.67 lebih banyak per transaksi (+3%) dibanding pelanggan normal. Namun rating member sedikit lebih rendah (6.94 vs 7.01), kemungkinan karena ekspektasi yang lebih tinggi.

![Analisis Pelanggan Member vs Normal](Proyek_BigData/assets/Customer-Analysis.jpg)

**Analisis Metode Pembayaran**:

| Payment | Count | Total Revenue | Avg Rating |
|---------|:-----:|:-------------:|:----------:|
| Cash | 344 | \$112,206.57 | 6.97 |
| Ewallet | 345 | \$109,993.11 | 6.95 |
| Credit card | 311 | \$100,767.07 | **7.00** |

**Insight**: Cash dan Ewallet hampir sama populer. Credit card paling sedikit digunakan (31.1%) namun penggunanya memberi rating tertinggi (7.00).

![Analisis Metode Pembayaran](Proyek_BigData/assets/Payment-Analysis.jpg)

## Analisis Korelasi

**Pertanyaan**: *Apakah terdapat korelasi antara rating kepuasan dengan nilai transaksi, jumlah item, atau waktu transaksi?*

**Scatter Plot Total vs Rating**: Tidak ada korelasi kuat antara nilai transaksi dengan rating (R² mendekati 0). Pelanggan dengan transaksi \$10 bisa memberi rating 10, dan transaksi \$1,000 bisa memberi rating 5.

**Scatter Plot Quantity vs Rating**: Jumlah item yang dibeli juga tidak berkorelasi signifikan dengan rating.

**Rata-rata Rating per Jam**: Rating cenderung lebih tinggi di jam-jam tertentu. Jam sibuk (19:00) memiliki rating yang cukup baik, mengindikasikan staf masih mampu melayani dengan baik di jam padat.

## Analisis Demografi

**Pertanyaan**: *Metode pembayaran apa yang paling dominan digunakan oleh tiap segmen pelanggan?*

Cash dan Ewallet sama-sama populer di semua segmen pelanggan. Credit card sedikit kurang digunakan. Tidak ada perbedaan signifikan preferensi pembayaran antara Member dan Normal, maupun antara gender.

## Ringkasan Temuan Analisis

| No | Temuan | Detail | Signifikansi |
|:--:|--------|--------|:-----------:|
| 1 | **Naypyitaw unggul revenue** | \$110,568.71 — tertinggi meski transaksi paling sedikit | AOV Naypyitaw \$337.10 vs \$312.35 (Yangon) |
| 2 | **Peak hour: 19:00** | 113 transaksi, \$39,699.51 | Golden hour operasional |
| 3 | **Food & Beverages terpopuler** | \$56,144.84 (17.38%) & rating tertinggi (7.11) | Kategori paling menguntungkan |
| 4 | **Member spend lebih tinggi** | \$327.79 vs \$318.12 per transaksi (+3%) | Program member efektif |
| 5 | **Tidak ada korelasi Total-Rating** | Scatter plot acak | Kepuasan tidak tergantung nominal |
| 6 | **Cash & Ewallet dominan** | Masing-masing ~34.5% transaksi | CC hanya 31.1% |
| 7 | **Rating terkonsentrasi di 6–9** | 67.5% transaksi | Kepuasan pelanggan baik |
| 8 | **Naypyitaw kuat di F&B** | \$23,767 dari Food & beverages | Peluang promosi lintas kategori |
| 9 | **Mandalay terendah rating** | 6.82 vs 7.07 (Naypyitaw) | Perlu investigasi kualitas layanan |
| 10 | **Distribusi revenue merata** | 5 dari 6 kategori ~\$54K | Diversifikasi produk berjalan baik |


# DASHBOARD INTERAKTIF

Dashboard interaktif ini menyediakan antarmuka visual yang komprehensif untuk mengeksplorasi data transaksi supermarket secara dinamis. Dashboard dilengkapi dengan beragam filter interaktif serta visualisasi yang saling terhubung untuk memudahkan analisis data ritel.

![Dashboard Interaktif Supermarket Sales](Proyek_BigData/assets/Dashboard.jpeg)

### Elemen Interaktif

**Filter (Quick Filters)**:

Dashboard dilengkapi dengan 6 quick filter yang memungkinkan pengguna menyaring data secara real-time:

| Filter | Tipe | Fungsi |
|--------|------|--------|
| **Day of Date** | Slider (Range-select) | Menyaring rentang tanggal transaksi (Rentang default: 1 Januari 2019 -- 30 Maret 2019). |
| **Product line** | Checkbox (Multi-select) | Memilih kategori lini produk yang ingin dianalisis (misal: Health and beauty, Home and lifestyle, Sports and travel, dll.). |
| **City** | Checkbox (Multi-select) | Memilih lokasi kota cabang supermarket (Mandalay, Naypyitaw, Yangon). |
| **Payment** | Checkbox (Multi-select) | Memilih jenis metode pembayaran (Credit card, Ewallet, Cash). |
| **Hour** | Checkbox (Multi-select) | Menyaring data transaksi berdasarkan jam tertentu (misal: jam 19, jam 20, dll.). |
| **Customer type** | Checkbox (Multi-select) | Memilih segmen tipe pelanggan (All / Member / Normal). |

Setiap perubahan pada filter di atas akan memperbarui seluruh tampilan visualisasi secara simultan untuk mempermudah analisis spesifik.

**Filter Actions (Cross-filtering)**:

Berdasarkan panduan operasional pada dashboard, sistem ini mendukung fitur interaksi antar-sheet:

- **Interaksi Grafik**: Pengguna dapat melakukan klik langsung pada elemen visual atau grafik mana pun untuk menjadikannya sebagai filter otomatis bagi visualisasi lainnya.
- **Reset Filter**: Pengguna cukup melakukan klik di luar area grafik (blank space) atau menghapus centang filter untuk mengembalikan visualisasi ke kumpulan data semula.

### Komponen Visualisasi (Sheets)

Dashboard ini tersusun atas beberapa komponen visualisasi utama yang menyajikan informasi performa ritel secara komprehensif:

**1. Key Performance Indicators (KPIs)**

Fungsi: Menampilkan ringkasan metrik performa utama bisnis di bagian atas panel untuk evaluasi cepat bagi pihak eksekutif.

Komponen:
- **Total Revenue**: Total pendapatan keseluruhan (877,1M).
- **Transactions**: Jumlah total transaksi yang tercatat (1.000 transaksi).
- **Products Sold**: Kuantitas produk yang berhasil terjual (5.510 unit).
- **Customer Rating**: Skor rata-rata kepuasan pelanggan (62,5 / 100).
- **Gross Income**: Total keuntungan kotor (41,8M).

**2. Revenue Trend**

Tipe Visualisasi: Line Chart (Grafik Garis).

Fungsi: Menampilkan tren naik-turun nilai total revenue harian sepanjang periode kuartal pertama tahun 2019 untuk mengidentifikasi pola penjualan pada tanggal-tanggal tertentu.

**3. Product Performance**

Tipe Visualisasi: Horizontal Stacked Bar Chart.

Fungsi: Membandingkan total volume penjualan di antara 6 lini produk utama. Pembagian warna di dalam setiap batang menunjukkan kontribusi segmentasi internal di tiap produk.

**4. Customer Analysis**

Tipe Visualisasi: Vertical Stacked Bar Chart.

Fungsi: Menganalisis pendapatan berdasarkan profil tipe pelanggan (Member vs Normal) yang diperdalam dengan pembagian nilai (skala jutaan/M) di setiap tingkat batangnya.

**5. Payment Analysis**

Tipe Visualisasi: Vertical Bar Chart (Grafik Batang).

Fungsi: Memetakan total pendapatan yang dihasilkan dari tiga metode pembayaran utama (Cash, Credit card, Ewallet) untuk melihat metode yang paling mendominasi.

**6. Hourly Activity**

Tipe Visualisasi: Vertical Stacked Bar Chart.

Fungsi: Menampilkan distribusi jumlah transaksi (Count of Invoice ID) berdasarkan jam terjadinya transaksi. Visualisasi ini membantu mengidentifikasi waktu-waktu sibuk (peak hours) supermarket.

**7. City Comparison**

Tipe Visualisasi: Vertical Bar Chart.

Fungsi: Membandingkan performa capaian total revenue antar tiga kota cabang (Mandalay, Naypyitaw, Yangon) guna mengetahui wilayah dengan performa bisnis tertinggi.

### Panduan Penggunaan

1. **Eksplorasi Mandiri**: Gunakan quick filter di panel sebelah kiri untuk memilih rentang tanggal, lini produk, kota, metode pembayaran, jam, atau tipe pelanggan yang ingin dianalisis.
2. **Interaksi Antar Visualisasi**: Klik elemen pada salah satu grafik (misalnya batang "Food and beverages" pada Product Performance) untuk menjadikannya sebagai filter otomatis bagi seluruh visualisasi lainnya.
3. **Reset Filter**: Klik di luar area grafik (blank space) atau hapus centang pada filter yang aktif untuk mengembalikan visualisasi ke kumpulan data semula.
4. **Ekspor**: Dashboard dapat diekspor ke format image atau PDF melalui menu File -- Export di Tableau untuk keperluan dokumentasi.


# SINTESIS DAN REKOMENDASI

## Jawaban Pertanyaan Bisnis Utama

> **Pertanyaan**: *"Faktor-faktor apa yang paling mempengaruhi total penjualan dan tingkat kepuasan pelanggan di ketiga cabang supermarket, dan bagaimana strategi yang dapat diterapkan untuk meningkatkan pendapatan serta loyalitas pelanggan?"*

**Faktor yang Mempengaruhi Total Penjualan**:

| Faktor | Dampak | Bukti Data |
|--------|--------|------------|
| **Lokasi Cabang** | SIGNIFIKAN | Naypyitaw unggul 4.1% dalam total revenue (\$110,568) vs Yangon (\$106,200) dan Mandalay (\$106,197) |
| **Waktu Transaksi** | SIGNIFIKAN | Jam 19:00 menyumbang 11.3% transaksi — tertinggi sepanjang hari |
| **Kategori Produk** | MODERAT | 5 dari 6 kategori memiliki kontribusi hampir identik (~\$54K) |
| **Tipe Pelanggan** | MODERAT | Member menghabiskan \$9.67 lebih banyak per transaksi (+3%) |
| **Metode Bayar** | RENDAH | Perbedaan revenue antar metode minimal |

**Faktor yang Mempengaruhi Kepuasan Pelanggan**:

| Faktor | Berpengaruh? | Detail |
|--------|:-----------:|--------|
| Kategori Produk | Ya | Food & Beverages rating tertinggi (7.11), Home & Lifestyle terendah (6.84) |
| Lokasi Cabang | Ya | Naypyitaw rating 7.07, Mandalay terendah 6.82 |
| Nilai Transaksi | Tidak | Scatter plot menunjukkan tidak ada korelasi antara Total dan Rating |
| Jumlah Item | Tidak | Quantity juga tidak berkorelasi dengan Rating |
| Metode Bayar | Minimal | Selisih rating antar metode hanya 0.05 poin |
| Tipe Pelanggan | Minimal | Member rating 6.94, Normal 7.01 |

## Rekomendasi Strategis

**Rekomendasi 1: Optimasi Jam Operasional (Prioritas Tinggi)**

Temuan: Jam 19:00 adalah peak hour dengan 113 transaksi dan revenue \$39,699.51.

Rekomendasi:
- Tambahkan 2 kasir tambahan pada shift 18:30–20:00 di semua cabang
- Pastikan stok produk populer (F&B) terisi penuh menjelang jam 18:00
- Terapkan "Happy Hour Promo" di jam sepi (17:00–18:00) untuk meratakan distribusi transaksi
- Target: Meningkatkan revenue jam sepi sebesar 15%

**Rekomendasi 2: Tingkatkan Program Member (Prioritas Tinggi)**

Temuan: Member spend \$9.67 lebih banyak (+3%) dan terdapat 501 member dari 1.000 transaksi.

Rekomendasi:
- Tiered Membership: Buat level Silver/Gold/Platinum berdasarkan frekuensi belanja
- Member-only promo: Diskon khusus untuk kategori dengan rating rendah (Home & Lifestyle)
- Referral program: Member yang mereferensikan pelanggan normal mendapat poin reward
- Target: Meningkatkan rasio member dari 50.1% menjadi 60% dan avg spend member menjadi +5%

**Rekomendasi 3: Strategi Produk per Cabang (Prioritas Sedang)**

Temuan: Setiap cabang memiliki preferensi produk yang berbeda.

Rekomendasi:
- **Naypyitaw**: Fokus stok dan promosi Food & Beverages serta Fashion accessories
- **Yangon**: Tingkatkan display dan promosi Home & Lifestyle dan Sports & Travel
- **Mandalay**: Optimasi Health & Beauty dan Sports & Travel; perbaiki layanan (rating terendah 6.82)
- Target: Meningkatkan revenue per cabang sebesar 5%

## Keterbatasan Analisis

| No | Keterbatasan | Dampak | Mitigasi |
|:--:|-------------|:------:|----------|
| 1 | Data hanya 3 bulan | Tidak bisa mendeteksi pola musiman tahunan | Gunakan sebagai baseline monitoring |
| 2 | Dataset sintetis | Pola data mungkin tidak mencerminkan realitas | Validasi dengan data tambahan |
| 3 | Tidak ada data biaya operasional | Tidak bisa menghitung profitabilitas bersih | Fokus pada revenue dan gross income |
| 4 | Tidak ada demografi detail | Segmentasi terbatas pada Member/Normal | Pertimbangkan survei tambahan |
| 5 | Rating subjektif | Interpretasi rating antar pelanggan bisa berbeda | Analisis berdasarkan tren, bukan absolut |

## Pertanyaan Lanjutan

Beberapa pertanyaan yang dapat dijawab pada penelitian selanjutnya:

1. **Bagaimana pola musiman penjualan supermarket jika data diperpanjang hingga 1 tahun?** — Data 89 hari belum cukup untuk mendeteksi siklus tahunan
2. **Seberapa besar profitabilitas bersih per cabang setelah memperhitungkan biaya operasional?** — Diperlukan data biaya sewa, gaji, dan utilitas untuk analisis profitabilitas
3. **Dapatkah model machine learning memprediksi tren penjualan mingguan dengan akurat?** — Analisis prediktif dapat dikembangkan menggunakan data historis yang lebih panjang
4. **Apakah ada perbedaan signifikan antara data sintetis dengan data ritel nyata?** — Validasi dengan data supermarket sesungguhnya diperlukan untuk menggeneralisasi temuan


\clearpage
\addcontentsline{toc}{chapter}{DAFTAR PUSTAKA}
\vspace*{5pt}
\begin{center}
\bfseries\fontsize{14}{18}\selectfont DAFTAR PUSTAKA
\end{center}
\vspace{20pt}
\raggedright

Chen, H., Chiang, R. H. L., \& Storey, V. C. (2012). Business Intelligence and Analytics: From Big Data to Big Impact. *MIS Quarterly*, 36(4), 1165--1188. https://doi.org/10.2307/41703503

Few, S. (2012). *Show Me the Numbers: Designing Tables and Graphs to Enlighten* (2nd ed.). Analytics Press.

Kaggle. (2019). *Supermarket Sales Dataset*. https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales

Larik, B. (2020). *Big Data Analytics: Algorithms, Techniques, and Applications*. Springer.

Ruscom, P. (2014). *Big Data Analytics*. TDWI Research.

Tableau Software. (2021). *Tableau Desktop Help*. https://help.tableau.com/current/pro/desktop/en-us/index.htm

Venkatesh, V., Brown, S. A., \& Bala, H. (2013). Bridging the Qualitative-Quantitative Divide: Guidelines for Conducting Mixed Methods Research in Information Systems. *MIS Quarterly*, 37(1), 21--54.

Wang, Y., Kung, L., \& Byrd, T. A. (2018). Big Data Analytics: Understanding Its Capabilities and Potential Benefits for Healthcare Organizations. *IEEE Journal of Biomedical and Health Informatics*, 22(3), 662--673.

Wixom, B. H., \& Watson, H. J. (2010). An Empirical Investigation of the Factors Affecting Data Warehousing Success. *MIS Quarterly*, 34(4), 663--697.
