# PENDAHULUAN

## Latar Belakang

Dalam era Big Data, analisis data transaksi ritel menjadi sangat penting untuk memahami perilaku konsumen, mengoptimalkan operasi bisnis, dan meningkatkan keuntungan. Supermarket sebagai salah satu sektor ritel yang besar menghasilkan volume data transaksi yang signifikan setiap harinya melalui sistem Point of Sale (POS). Data yang terkumpul meliputi informasi produk, harga, jumlah pembelian, metode pembayaran, hingga tingkat kepuasan pelanggan. Dengan menganalisis data ini secara sistematis, manajemen dapat membuat keputusan berbasis data yang lebih akurat dan strategis.

Perkembangan teknologi Big Data telah membuka peluang besar bagi sektor ritel untuk melakukan analisis mendalam terhadap data transaksi mereka. Konsep 5V Big Data — Volume, Velocity, Variety, Veracity, dan Value — menjadi kerangka kerja yang relevan dalam memahami potensi dan tantangan pengolahan data ritel skala menengah hingga besar. Visualisasi data memegang peran krusial dalam menjembatani data mentah dengan pengambilan keputusan, dan Tableau hadir sebagai salah satu platform visualisasi data terdepan yang memungkinkan pembuatan dashboard interaktif tanpa memerlukan keahlian pemrograman yang mendalam.

Dataset yang digunakan dalam penelitian ini adalah **Supermarket Sales Dataset** yang diperoleh dari Kaggle, dikumpulkan oleh Aung Pyae Ap. Dataset ini merepresentasikan data transaksi penjualan dari sebuah perusahaan supermarket fiktif yang memiliki tiga cabang di tiga kota besar di Myanmar, yaitu Yangon, Mandalay, dan Naypyitaw. Dataset mencakup 1.000 transaksi selama periode 3 bulan (Januari – Maret 2019) dengan 17 kolom informasi yang mencakup detail transaksi, produk, pelanggan, dan metrik kepuasan.

Oleh karena itu, penelitian ini bertujuan untuk menganalisis data penjualan supermarket menggunakan Tableau dengan pendekatan Big Data, menghasilkan dashboard interaktif, serta merumuskan rekomendasi strategis untuk peningkatan pendapatan dan loyalitas pelanggan.

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

## Manfaat Penelitian

Manfaat dari penelitian ini adalah:

1. **Bagi Manajemen Supermarket**: Memberikan insight berbasis data untuk pengambilan keputusan strategis terkait operasional, stok produk, dan program loyalitas pelanggan.
2. **Bagi Akademia**: Menambah referensi dan studi kasus dalam bidang analisis data ritel dan visualisasi menggunakan Tableau.
3. **Bagi Pengembang Sistem**: Menyediakan informasi untuk perbaikan sistem POS dan manajemen inventaris berbasis data.
4. **Bagi Peneliti Selanjutnya**: Menjadi dasar untuk penelitian lebih lanjut mengenai analisis data penjualan ritel dengan cakupan data yang lebih luas.

## Batasan Masalah

Batasan masalah dalam penelitian ini adalah:

1. Dataset yang digunakan adalah Supermarket Sales Dataset dari Kaggle dengan 1.000 baris data dan 17 kolom.
2. Data mencakup periode 1 Januari 2019 hingga 9 Maret 2019 (89 hari).
3. Analisis dilakukan menggunakan Tableau Desktop sebagai alat visualisasi utama.
4. Fokus analisis terbatas pada tiga cabang: Yangon, Mandalay, dan Naypyitaw.
5. Enam kategori produk yang dianalisis: Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel.
6. Metrik evaluasi kepuasan terbatas pada rating numerik (skala 1–10) tanpa data kualitatif.

## Sistematika Penulisan

Laporan ini disusun dalam lima bab yang sistematis sebagai berikut:

- **BAB I: PENDAHULUAN** — Berisi latar belakang, rumusan masalah, tujuan penelitian, manfaat penelitian, batasan masalah, dan sistematika penulisan.
- **BAB II: LANDASAN TEORI** — Memaparkan konsep dasar Big Data dan 5V, metodologi analisis data, Tableau sebagai alat visualisasi, serta penelitian terkait.
- **BAB III: METODOLOGI PENELITIAN** — Menjelaskan sumber data, preprocessing data, cara kerja analisis dengan Tableau, serta tools dan library yang digunakan.
- **BAB IV: HASIL DAN PEMBAHASAN** — Menyajikan hasil analisis mencakup profiling data, data cleaning, exploratory data analysis, dashboard interaktif, dan rekomendasi strategis.
- **BAB V: PENUTUP** — Berisi kesimpulan dari seluruh rangkaian penelitian dan saran untuk pengembangan selanjutnya.


# LANDASAN TEORI

## Konsep Big Data dan 5V

Big Data merujuk pada kumpulan data yang sangat besar, cepat, dan kompleks yang tidak dapat diolah dengan alat pemrosesan data tradisional. Karakteristik Big Data sering digambarkan melalui konsep 5V (Ruscom, 2014):

1. **Volume** — Jumlah data yang dihasilkan dan disimpan. Dalam konteks ritel, volume data mencakup jutaan transaksi harian dari berbagai cabang. Dataset yang digunakan memiliki volume 1.000 baris yang representatif untuk analisis ritel skala menengah.

2. **Velocity** — Kecepatan data masuk dan diproses. Data transaksi POS bersifat real-time dengan timestamp per transaksi, memungkinkan analisis pola waktu seperti jam sibuk dan tren harian.

3. **Variety** — Keragaman tipe data. Dataset memiliki 17 kolom dengan tipe data beragam: numerik (Total, Quantity, Rating), kategorikal (Branch, Product line, Payment), temporal (Date, Time), dan tekstual (Invoice ID).

4. **Veracity** — Kualitas dan akurasi data. Dataset tergolong bersih tanpa missing values, namun merupakan data sintetis sehingga memiliki konsistensi tinggi.

5. **Value** — Nilai bisnis yang dapat diekstrak dari data. Analisis menghasilkan rekomendasi strategis untuk optimasi stok, evaluasi program member, strategi pricing per cabang, dan peningkatan kepuasan pelanggan.

## Siklus Hidup Data (Data Lifecycle)

Siklus hidup data dalam analisis data ritel mengikuti alur:

```
[Sumber Data] → [Pengumpulan] → [Penyimpanan] → [Analisis] → [Presentasi]
     (POS System)    (CSV File)     (Database)     (Tableau)    (Dashboard)
```

Dataset yang digunakan berada pada tahap penyimpanan (storage) dan diproses melalui tahap analisis hingga presentasi sesuai alur kerja data analyst.

## Metodologi Analisis Data

Metodologi yang digunakan dalam penelitian ini mengikuti proses analisis data standar yang terdiri dari enam tahap (Wixom & Watson, 2010):

1. **Pemahaman Masalah** — Identifikasi stakeholder, domain bisnis, dan pertanyaan bisnis.
2. **Profiling dan Persiapan Data** — Pemahaman struktur data, tipe data, dan kualitas data.
3. **Pembersihan Data** — Penanganan missing values, duplikasi, outlier, dan standarisasi tipe data.
4. **Analisis Eksploratif dan Mendalam (EDA)** — Visualisasi distribusi data, analisis tren, korelasi, dan segmentasi.
5. **Dashboard Interaktif** — Penggabungan visualisasi ke dalam satu antarmuka yang dapat diinteraksi.
6. **Sintesis Insight dan Rekomendasi** — Penarikan kesimpulan dan formulasi rekomendasi strategis.

## Tableau sebagai Alat Visualisasi

Tableau adalah platform business intelligence dan visualisasi data yang memungkinkan pengguna untuk terhubung ke berbagai sumber data, membuat visualisasi interaktif, dan membagikannya dalam bentuk dashboard. Tableau dipilih dalam penelitian ini karena beberapa keunggulan (Tableau Software, 2021):

- **Konektivitas Data**: Mendukung berbagai sumber data termasuk file CSV, Excel, database SQL, dan layanan cloud.
- **Antarmuka Drag-and-Drop**: Memungkinkan pembuatan visualisasi tanpa coding, dengan sistem drag-and-drop yang intuitif.
- **Calculated Fields dan Parameter**: Mendukung pembuatan field kalkulasi dan parameter untuk analisis yang lebih dinamis.
- **Dashboard Interaktif**: Mampu menggabungkan beberapa sheet visualisasi dengan filter, parameter, dan filter actions.
- **Ekspor Fleksibel**: Mendukung ekspor ke berbagai format termasuk image, PDF, dan Tableau Packaged Workbook (.twbx).

## Penelitian Terkait

Beberapa penelitian terkait yang relevan dengan analisis data penjualan supermarket menggunakan Tableau:

1. **Chen et al. (2012)** — Membahas peran Business Intelligence dan Big Data Analytics dalam transformasi bisnis. Menekankan pentingnya visualisasi data dalam pengambilan keputusan strategis.

2. **Few (2012)** — Membahas prinsip-prinsip desain visualisasi data yang efektif dalam buku *Show Me the Numbers*, yang menjadi acuan dalam perancangan dashboard.

3. **Wang et al. (2018)** — Mengkaji kemampuan Big Data Analytics dalam sektor kesehatan dan ritel, menunjukkan bahwa analisis data dapat memberikan manfaat signifikan bagi organisasi.

4. **Larik (2020)** — Membahas algoritma, teknik, dan aplikasi Big Data Analytics dalam berbagai domain termasuk ritel.

5. **Wixom & Watson (2010)** — Melakukan investigasi empiris tentang faktor-faktor yang mempengaruhi kesuksesan data warehousing, yang relevan dengan tahap persiapan data dalam penelitian ini.


# METODOLOGI PENELITIAN

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
| **Tugas Analisis** | Analisis deskriptif, visualisasi, dashboard interaktif |

### Informasi Fitur

Dataset memiliki 17 kolom yang terdiri dari identifier transaksi, data demografi, detail produk, metrik keuangan, dan metrik kepuasan:

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

### Distribusi Data per Cabang

| Cabang | Kota | Jumlah Transaksi | Total Revenue | Rata-rata Rating |
|:------:|:----:|:----------------:|:-------------:|:----------------:|
| A | Yangon | 340 | \$106,200.37 | 7.03 |
| B | Mandalay | 332 | \$106,197.67 | 6.82 |
| C | Naypyitaw | 328 | \$110,568.71 | 7.07 |

## Preprocessing Data

### Pengecekan Tipe Data

Pengecekan tipe data dilakukan dengan membandingkan tipe data hasil impor CSV dengan tipe data yang seharusnya:

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

### Handling Missing Values dan Duplikasi

- **Missing Values**: TIDAK ADA missing values (0 null) di seluruh 17 kolom. Semua 1.000 baris memiliki data lengkap.
- **Duplikasi**: TIDAK ADA data duplikat. Setiap Invoice ID unik — 1.000 nilai unik dari 1.000 baris.

### Feature Engineering (Calculated Fields)

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

## Cara Kerja Analisis dengan Tableau

Alur kerja analisis data dalam penelitian ini mengikuti langkah-langkah sistematis sebagai berikut:

### Langkah 1: Import Data

Dataset `supermarket_sales.csv` diimpor ke Tableau melalui koneksi **Text File**. Tableau secara otomatis mendeteksi tipe data dari setiap kolom.

### Langkah 2: Verifikasi dan Konversi Tipe Data

Setelah impor, dilakukan verifikasi tipe data di tab Data Source. Kolom `Date` dan `Time` yang awalnya terbaca sebagai String dikonversi ke tipe Date dan Time/Datetime.

### Langkah 3: Pengecekan Kualitas Data

Dilakukan pengecekan missing values, duplikasi, inkonsistensi format kategorikal, dan outlier melalui box plot.

### Langkah 4: Pembuatan Calculated Field

Dibuat 7 calculated field untuk mendukung analisis yang lebih mendalam.

### Langkah 5: Pembuatan Visualisasi

Dibuat 15 sheet visualisasi yang mencakup histogram distribusi data, line chart tren penjualan, bar chart performa produk, scatter plot korelasi, dan heatmap preferensi cabang.

### Langkah 6: Pembuatan Dashboard

Keenam sheet terbaik digabungkan ke dalam satu dashboard interaktif dengan filter, parameter, dan filter actions.

### Langkah 7: Sintesis Insight dan Rekomendasi

Seluruh temuan analisis disintesis menjadi kesimpulan dan rekomendasi strategis.

## Tools dan Library

| Tool/Library | Versi | Fungsi |
|-------------|:-----:|--------|
| Tableau Desktop | 2023.x | Visualisasi data, analisis eksploratif, dashboard interaktif |
| Tableau Public | 2023.x | Berbagi dashboard secara online |
| Kaggle | — | Sumber dataset supermarket sales |
| Git | 2.x | Version control dan manajemen dokumentasi |
| Markdown (Pandoc) | — | Penulisan laporan dan dokumentasi |


# HASIL DAN PEMBAHASAN

## Hasil Preprocessing dan Profiling Data

### Analisis 5V Big Data

| V | Penjelasan | Relevansi Dataset |
|---|-----------|-------------------|
| **Volume** | Jumlah data yang besar | 1.000 baris transaksi — skala kecil namun cukup representatif untuk analisis ritel skala menengah |
| **Velocity** | Kecepatan data masuk | Data transaksi bersifat harian dengan timestamp per transaksi, mencerminkan aliran data real-time pada sistem POS |
| **Variety** | Keragaman tipe data | Dataset memiliki 17 kolom dengan tipe data beragam: numerik (Total, Quantity, Rating), kategorikal (Branch, Product line, Payment), temporal (Date, Time), dan tekstual (Invoice ID) |
| **Veracity** | Kualitas dan akurasi data | Data bersih tanpa missing value, namun merupakan data sintetis sehingga memiliki konsistensi tinggi |
| **Value** | Nilai bisnis yang dapat diekstrak | Analisis menghasilkan rekomendasi strategis: optimasi stok produk, evaluasi program member, strategi pricing per cabang, dan peningkatan kepuasan pelanggan |

### Identifikasi Pemangku Kepentingan (Stakeholder)

| Stakeholder | Peran | Kepentingan |
|-------------|-------|-------------|
| Manajer Regional | Mengawasi kinerja 3 cabang | Mengetahui cabang dengan kinerja terbaik dan faktor pendorongnya |
| Manajer Cabang | Mengelola operasional harian | Insight pola penjualan per produk dan jam sibuk untuk mengatur stok dan shift |
| Tim Marketing | Menyusun strategi promosi dan loyalitas | Efektivitas program member vs non-member, produk yang perlu dipromosikan |
| Tim Keuangan | Mengelola pendapatan dan pajak | Analisis pendapatan kotor, margin, dan tren biaya |

### Kualitas Dataset

Pengecekan data source di Tableau memastikan bahwa seluruh kolom memiliki tipe data yang sesuai:

![Data Source Tableau](Proyek_BigData/assets/Data-Source.jpg)

## Hasil Data Cleaning

### Pengecekan Missing Values dan Duplikasi

Hasil pengecekan menggunakan Tableau menunjukkan:

- **Missing Values**: 0 null dari 1.000 baris × 17 kolom — dataset sangat bersih
- **Duplikasi**: COUNT(Invoice ID) = 1.000 dan COUNTD(Invoice ID) = 1.000 — tidak ada duplikasi

![Pengecekan Kualitas Data](Proyek_BigData/assets/Data-Quality.jpg)

### Pengecekan Inkonsistensi Format Kategorikal

| Field | Nilai Unik | Format Konsisten? |
|-------|-----------|:-----------------:|
| City | Yangon, Mandalay, Naypyitaw | [OK] |
| Branch | A, B, C | [OK] |
| Customer type | Member, Normal | [OK] |
| Gender | Male, Female | [OK] |
| Product line | 6 kategori (capitalized consistently) | [OK] |
| Payment | Cash, Ewallet, Credit card | [OK] |

### Pengecekan Outlier

**Box Plot Total per City**: Nilai Total berkisar \$10.68–\$1,042.65, tidak ada outlier signifikan per cabang.

![Box Plot Total per City](Proyek_BigData/assets/Box-Plot-Total.jpg)

**Box Plot Rating per Product Line**: Rating 4.0–10.0, tidak ada outlier ekstrem, sebaran normal.

![Box Plot Rating per Product Line](Proyek_BigData/assets/Box-Plot-Rating.jpg)

### Validasi Numerik

| Field | Nilai Min | Nilai Max | Range Wajar? |
|-------|-----------|-----------|:------------:|
| Unit price | \$10.08 | \$99.96 | [OK] |
| Quantity | 1 | 10 | [OK] |
| Tax 5% | \$0.51 | \$49.65 | [OK] |
| Total | \$10.68 | \$1,042.65 | [OK] |
| cogs | \$10.16 | \$993.00 | [OK] |
| gross income | \$0.51 | \$49.65 | [OK] |

**Verifikasi Relasi**: Semua konsisten — Total = cogs + gross income, Tax 5% = Total × 5/105.

### Ringkasan Pembersihan Data

| Aspek | Status | Detail |
|-------|:-----:|--------|
| Missing Values | [OK] Bersih | 0 null dari 1.000 baris × 17 kolom |
| Duplikasi | [OK] Bersih | 0 duplikat |
| Inkonsistensi Format | [OK] Bersih | Semua nilai kategorikal konsisten |
| Outlier | [OK] Bersih | Tidak ada outlier ekstrem |
| Konversi Date | [OK] Selesai | String → Date (M/D/YYYY) |
| Konversi Time | [OK] Selesai | String → Time / Hour extracted |

## Hasil Exploratory Data Analysis (EDA)

### Analisis Distribusi Data

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

### Analisis Tren Waktu (Sub-Pertanyaan 1)

**Q1**: *Bagaimana tren penjualan harian dan mingguan di setiap cabang selama periode Jan–Mar 2019?*

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

### Analisis Performa Produk (Sub-Pertanyaan 2)

**Q2**: *Kategori produk apa yang paling berkontribusi terhadap total pendapatan?*

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

### Analisis Pelanggan (Sub-Pertanyaan 3)

**Q3**: *Bagaimana pengaruh tipe pelanggan (Member vs Normal) dan metode pembayaran terhadap nilai transaksi dan rating?*

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

### Analisis Korelasi (Sub-Pertanyaan 4)

**Q4**: *Apakah terdapat korelasi antara rating kepuasan dengan nilai transaksi, jumlah item, atau waktu transaksi?*

**Scatter Plot Total vs Rating**: Tidak ada korelasi kuat antara nilai transaksi dengan rating (R² mendekati 0). Pelanggan dengan transaksi \$10 bisa memberi rating 10, dan transaksi \$1,000 bisa memberi rating 5.

**Scatter Plot Quantity vs Rating**: Jumlah item yang dibeli juga tidak berkorelasi signifikan dengan rating.

**Rata-rata Rating per Jam**: Rating cenderung lebih tinggi di jam-jam tertentu. Jam sibuk (19:00) memiliki rating yang cukup baik, mengindikasikan staf masih mampu melayani dengan baik di jam padat.

### Analisis Demografi (Sub-Pertanyaan 5)

**Q5**: *Metode pembayaran apa yang paling dominan digunakan oleh tiap segmen pelanggan?*

Cash dan Ewallet sama-sama populer di semua segmen pelanggan. Credit card sedikit kurang digunakan. Tidak ada perbedaan signifikan preferensi pembayaran antara Member dan Normal, maupun antara gender.

### Ringkasan Temuan Analisis

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

### Daftar Visualisasi

| No | Nama Sheet | Tipe Chart | Sub-Pertanyaan |
|:--:|-----------|:----------:|:--------------:|
| 1 | Histogram Total | Histogram | EDA |
| 2 | Histogram Rating | Histogram | EDA |
| 3 | Tren Penjualan Harian | Line Chart | Q1 |
| 4 | Penjualan per Hari | Bar Chart | Q1 |
| 5 | Jam Sibuk | Bar Chart | Q1 |
| 6 | Revenue per Product | Bar Chart | Q2 |
| 7 | Gross Income per Product | Bar Chart | Q2 |
| 8 | Rating per Product | Bar Chart | Q2 |
| 9 | Produk per Cabang (Heatmap) | Heatmap | Q2 |
| 10 | Member vs Normal | Bar Chart | Q3 |
| 11 | Preferensi Pembayaran | Bar Chart | Q3 |
| 12 | Total vs Rating (Scatter) | Scatter Plot | Q4 |
| 13 | Rating per Jam | Bar Chart | Q4 |
| 14 | Gender Analysis | Bar Chart | Q5 |
| 15 | Payment by Gender | Heatmap/Bar | Q5 |

## Dashboard Interaktif

### Tujuan Dashboard

Menggabungkan semua sheet analisis ke dalam satu dashboard interaktif yang memungkinkan stakeholder untuk:
- Memonitor kinerja penjualan secara real-time
- Membandingkan performa antar cabang
- Menganalisis tren produk dan pelanggan
- Membuat keputusan berbasis data dengan filter interaktif

### Sheet yang Digunakan

Enam sheet terbaik dipilih untuk dashboard:

| No | Nama Sheet | Tipe | Fungsi |
|:--:|-----------|:----:|--------|
| 1 | **Revenue Trend** | Line Chart | Tren penjualan harian per cabang |
| 2 | **Product Performance** | Bar Chart | Revenue dan rating per product line |
| 3 | **Customer Analysis** | Bar Chart | Member vs Normal comparison |
| 4 | **Hourly Activity** | Bar Chart | Peak hours analysis |
| 5 | **City Comparison** | Side-by-side Bar | Perbandingan metrik antar cabang |
| 6 | **Rating Distribution** | Histogram | Sebaran rating kepuasan |

### Quick Filters

1. **Filter City (Drop-down)**: Memungkinkan pengguna memilih satu atau semua cabang
2. **Filter Product line (Drop-down)**: Memungkinkan pengguna fokus pada kategori produk tertentu
3. **Filter Customer type (Drop-down)**: Filter berdasarkan tipe pelanggan

### Filter Actions

**Action — Filter by City**: Klik pada cabang di sheet Revenue Trend akan memfilter semua sheet lain untuk menampilkan data cabang yang dipilih.

### Parameter

**Parameter — Top N Products**: Parameter integer (1–6) untuk menampilkan N produk teratas berdasarkan revenue. Parameter ini dikontrol melalui slider di dashboard.

### Layout Dashboard

```
+------------------------------------------------------------------+
|  SUPERMARKET SALES DASHBOARD - Jan-Mar 2019                      |
+------------------------------------------------------------------+
|  [City: All]  [Product: All]  [Customer: All]                    |
+-----------------------------+------------------------------------+
|   REVENUE TREND             |   PRODUCT PERFORMANCE              |
|   (Line Chart)              |   (Bar Chart)                     |
+-----------------------------+------------------------------------+
|   CUSTOMER ANALYSIS         |   HOURLY ACTIVITY                  |
|   (Bar Chart)               |   (Bar Chart)                     |
+-----------------------------+------------------------------------+
|   CITY COMPARISON           |   RATING DISTRIBUTION              |
|   (Side-by-side bars)       |   (Histogram)                     |
+-----------------------------+------------------------------------+
|  Filter Action: Klik cabang -> filter semua sheet               |
|  Parameter: Top N Products [1] [2] [3] [4] [5] [6]              |
+------------------------------------------------------------------+
```

### Formatting dan Finishing

- **Color Palette**: Naypyitaw (Green), Yangon (Blue), Mandalay (Orange)
- **Tooltip**: Informasi City, Revenue, Transactions saat hover
- **Format Angka**: Total dalam Currency (\$ dengan 2 desimal), Rating dalam Number (2 desimal)

### Export

Dashboard diekspor dalam format **.twbx** (Tableau Packaged Workbook) yang berisi data dan seluruh visualisasi, siap dibuka di Tableau Desktop mana pun.

## Sintesis Insight dan Rekomendasi

### Jawaban Pertanyaan Bisnis Utama

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

### Rekomendasi Strategis

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

**Rekomendasi 4: Investigasi Rating Mandalay (Prioritas Sedang)**

Temuan: Mandalay memiliki rating terendah (6.82) dibanding Naypyitaw (7.07) dan Yangon (7.03).

Rekomendasi:
- Lakukan survei kepuasan pelanggan khusus untuk cabang Mandalay
- Evaluasi kualitas layanan staf dan kebersihan toko
- Bandingkan jam operasional dan tata letak toko dengan cabang lain
- Target: Meningkatkan rating Mandalay ke 7.0 dalam 3 bulan

**Rekomendasi 5: Promosi Credit Card (Prioritas Rendah)**

Temuan: Credit card paling sedikit digunakan (31.1%) namun penggunanya memberi rating tertinggi (7.00).

Rekomendasi:
- Tawarkan diskon 2% untuk pembayaran Credit Card
- Kerja sama dengan bank untuk promo cicilan 0%
- Target: Meningkatkan penggunaan CC ke 35%

### Matriks Prioritas Rekomendasi

| No | Rekomendasi | Dampak | Usaha | Prioritas |
|:--:|------------|:------:|:----:|:---------:|
| 1 | Optimasi jam operasional | Tinggi | Rendah | **P1** |
| 2 | Tingkatkan program member | Tinggi | Sedang | **P1** |
| 3 | Strategi produk per cabang | Sedang | Sedang | **P2** |
| 4 | Investigasi rating Mandalay | Sedang | Rendah | **P2** |
| 5 | Promosi Credit Card | Rendah | Rendah | **P3** |

### Keterbatasan Analisis

| No | Keterbatasan | Dampak | Mitigasi |
|:--:|-------------|:------:|----------|
| 1 | Data hanya 3 bulan | Tidak bisa mendeteksi pola musiman tahunan | Gunakan sebagai baseline monitoring |
| 2 | Dataset sintetis | Pola data mungkin tidak mencerminkan realitas | Validasi dengan data tambahan |
| 3 | Tidak ada data biaya operasional | Tidak bisa menghitung profitabilitas bersih | Fokus pada revenue dan gross income |
| 4 | Tidak ada demografi detail | Segmentasi terbatas pada Member/Normal | Pertimbangkan survei tambahan |
| 5 | Rating subjektif | Interpretasi rating antar pelanggan bisa berbeda | Analisis berdasarkan tren, bukan absolut |


# PENUTUP

## Kesimpulan

Berdasarkan penelitian yang telah dilakukan mengenai analisis data penjualan supermarket menggunakan Tableau, dapat ditarik kesimpulan sebagai berikut:

1. **Dataset Supermarket Sales** memiliki kualitas yang sangat baik dengan 0 missing values, 0 duplikasi, dan tidak ada outlier signifikan. Dari perspektif Big Data 5V, dataset ini memberikan nilai (Value) yang signifikan untuk analisis ritel meskipun volume (Volume) tergolong kecil.

2. **Lokasi cabang dan waktu transaksi** merupakan faktor yang paling signifikan mempengaruhi total penjualan. Naypyitaw menunjukkan performa terbaik dengan total revenue \$110,568.71 meskipun memiliki jumlah transaksi paling sedikit (328), didorong oleh average transaction value tertinggi (\$337.10). Jam 19:00 teridentifikasi sebagai peak hour dengan 113 transaksi dan revenue \$39,699.51.

3. **Food & Beverages** adalah kategori produk paling unggul dengan kontribusi revenue tertinggi (\$56,144.84 atau 17.38%) dan rating kepuasan tertinggi (7.11). Distribusi revenue cukup merata antar kategori, menunjukkan diversifikasi produk berjalan baik.

4. **Program member terbukti efektif** dengan peningkatan rata-rata spend sebesar \$9.67 per transaksi (+3%) dibanding pelanggan normal. Namun rating member (6.94) sedikit lebih rendah dari normal (7.01), mengindikasikan adanya celah ekspektasi yang perlu diatasi.

5. **Tidak terdapat korelasi signifikan** antara nilai transaksi atau jumlah item dengan rating kepuasan pelanggan. Faktor yang lebih berpengaruh terhadap kepuasan adalah kategori produk dan lokasi cabang, mengindikasikan bahwa kualitas layanan dan produk lebih penting daripada nominal belanja.

6. **Dashboard interaktif Tableau** berhasil dibangun dengan 6 sheet visualisasi, 3 quick filters, filter actions, dan parameter Top N Products. Dashboard ini memungkinkan stakeholder melakukan eksplorasi data secara mandiri dan mendukung pengambilan keputusan berbasis data.

## Saran

Untuk pengembangan penelitian selanjutnya, beberapa saran yang dapat diberikan adalah:

1. **Memperluas cakupan data** — Menggunakan data dengan rentang waktu minimal 1 tahun untuk mendeteksi pola musiman dan tren tahunan yang lebih akurat.

2. **Menambahkan data biaya operasional** — Mengumpulkan data biaya sewa, gaji, utilitas, dan biaya operasional lainnya untuk melakukan analisis profitabilitas bersih per cabang.

3. **Memperkaya data demografi** — Menambahkan variabel seperti usia, pekerjaan, dan tingkat pendapatan untuk segmentasi pelanggan yang lebih granular.

4. **Integrasi data kualitatif** — Melakukan survei langsung kepada pelanggan untuk mendapatkan data kualitatif yang melengkapi rating numerik.

5. **Analisis prediktif** — Mengembangkan model machine learning untuk memprediksi tren penjualan dan perilaku pelanggan di masa mendatang.

6. **Perbandingan antar periode** — Membandingkan data dengan periode yang sama di tahun berikutnya untuk mengukur pertumbuhan dan efektivitas rekomendasi yang telah diimplementasikan.

7. **Integrasi data kompetitor** — Menambahkan data pasar dan kompetitor untuk analisis pangsa pasar yang lebih komprehensif.


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
