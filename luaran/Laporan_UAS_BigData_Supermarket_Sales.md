# Laporan UAS Big Data Science
## Analisis Data Penjualan Supermarket Menggunakan Tableau

**Anggota Kelompok:** [Nama 1 - NIM], [Nama 2 - NIM], [Nama 3 - NIM]
**Dosen:** Nur Choiriyati
**Dataset:** Supermarket Sales
**Tools:** Tableau Desktop, Python

---

## Catatan Penyusunan

Dokumen ini adalah draft gabungan dari seluruh tahap. Sebelum dikumpulkan, masukkan screenshot Tableau sesuai SCREENSHOT_GUIDE.md, isi nama anggota, rapikan nomor gambar, dan pastikan total halaman maksimal 20 halaman.

---

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

---

# Tahap 2: Profiling dan Persiapan Data
## Supermarket Sales Analysis

---

## 1. Kondisi Dasar Dataset

| Metrik | Nilai |
|--------|-------|
| **Jumlah Baris** | 1.000 transaksi |
| **Jumlah Kolom** | 17 field |
| **Rentang Waktu** | 1 Januari 2019 – 9 Maret 2019 (89 hari) |
| **Rentang Jam** | 10:00 – 20:59 |
| **Total Pendapatan** | $322,966.75 |
| **Total HPP (COGS)** | $307,587.38 |
| **Total Gross Income** | $15,379.37 |
| **Sumber Data** | Kaggle — Supermarket Sales Dataset |

---

## 2. Deskripsi Setiap Field

| # | Nama Field | Tipe Data | Makna dalam Konteks Bisnis |
|---|------------|-----------|---------------------------|
| 1 | **Invoice ID** | String (Text) | Nomor unik setiap transaksi — identifier utama |
| 2 | **Branch** | String (Kategorikal) | Kode cabang supermarket: A (Yangon), B (Mandalay), C (Naypyitaw) |
| 3 | **City** | String (Kategorikal) | Kota lokasi cabang |
| 4 | **Customer type** | String (Kategorikal) | Tipe pelanggan: Member (terdaftar) atau Normal (umum) |
| 5 | **Gender** | String (Kategorikal) | Jenis kelamin pelanggan: Male / Female |
| 6 | **Product line** | String (Kategorikal) | Kategori produk yang dibeli (6 kategori) |
| 7 | **Unit price** | Numerik (Decimal) | Harga satuan per produk (dalam USD) |
| 8 | **Quantity** | Numerik (Integer) | Jumlah unit produk yang dibeli |
| 9 | **Tax 5%** | Numerik (Decimal) | Pajak 5% dari total transaksi |
| 10 | **Total** | Numerik (Decimal) | Total nilai transaksi setelah pajak |
| 11 | **Date** | Date (Tanggal) | Tanggal transaksi |
| 12 | **Time** | Time (Waktu) | Jam transaksi |
| 13 | **Payment** | String (Kategorikal) | Metode pembayaran: Cash, Ewallet, Credit card |
| 14 | **cogs** | Numerik (Decimal) | Cost of Goods Sold — Harga pokok penjualan |
| 15 | **gross margin percentage** | Numerik (Decimal) | Persentase margin kotor (4.76% konstan) |
| 16 | **gross income** | Numerik (Decimal) | Pendapatan kotor (Total - cogs) |
| 17 | **Rating** | Numerik (Decimal) | Rating kepuasan pelanggan (1-10) |

---

## 3. Pengecekan Tipe Data

### 3.1. Ringkasan Pengecekan

| Field | Tipe Saat Ini (CSV) | Seharusnya | Perlu Diubah? |
|-------|--------------------|------------|:---:|
| Invoice ID | String | String | [NO] Tidak |
| Branch | String | String (Kategorikal) | [NO] Tidak |
| City | String | String (Kategorikal) | [NO] Tidak |
| Customer type | String | String (Kategorikal) | [NO] Tidak |
| Gender | String | String (Kategorikal) | [NO] Tidak |
| Product line | String | String (Kategorikal) | [NO] Tidak |
| Unit price | Numerik | Number (Decimal) | [NO] Tidak |
| Quantity | Numerik | Number (Integer) | [NO] Tidak |
| Tax 5% | Numerik | Number (Decimal) | [NO] Tidak |
| Total | Numerik | Number (Decimal) | [NO] Tidak |
| **Date** | **String (M/D/YYYY)** | **Date** | **[OK] WAJIB — Parse ke Date** |
| **Time** | **String (HH:MM)** | **Time** | **[OK] WAJIB — Parse ke Time** |
| Payment | String | String (Kategorikal) | [NO] Tidak |
| cogs | Numerik | Number (Decimal) | [NO] Tidak |
| gross margin percentage | Numerik | Number (Decimal) | [NO] Tidak |
| gross income | Numerik | Number (Decimal) | [NO] Tidak |
| Rating | Numerik | Number (Decimal) | [NO] Tidak |

### 3.2. Pengecekan Missing Values

**Hasil: TIDAK ADA missing values (0 null) di seluruh 17 kolom.** Semua 1.000 baris memiliki data lengkap. Data sudah bersih dari sisi kelengkapan.

### 3.3. Pengecekan Duplikasi

**Hasil: TIDAK ADA data duplikat.** Setiap Invoice ID unik — 1.000 nilai unik dari 1.000 baris.

---

## 4. Standardisasi Tipe Data

### 4.1. Konversi Date (String → Date)

**Sebelum:** `Date` bertipe String dengan format `M/D/YYYY` (contoh: `1/5/2019`, `3/8/2019`)

**Di Tableau:**
1. Setelah import CSV, buka tab **Data Source**
2. Klik ikon tipe data pada kolom `Date`
3. Pilih **Date**
4. Pastikan Tableau membaca format tanggal sebagai **M/D/YYYY**

**Screenshot:** *(Screenshot saat konfigurasi Date di Tableau akan ditambahkan saat praktik)*

### 4.2. Konversi Time (String → Time)

**Sebelum:** `Time` bertipe String dengan format `HH:MM` (contoh: `13:08`, `10:29`)

**Di Tableau:**
1. `Time` dapat dibaca sebagai teks oleh default
2. Rekomendasi praktis: biarkan `Time` sebagai teks dan buat calculated field `Hour`

**Rekomendasi:** Buat **Calculated Field** baru:
```
Hour = INT(LEFT([Time], 2))
```
Ini memudahkan analisis tren per jam.

### 4.3. Verifikasi Numerik

Semua field numerik (Unit price, Quantity, Tax 5%, Total, cogs, gross margin percentage, gross income, Rating) sudah dalam format numerik yang benar:

| Field | Range | Valid |
|-------|-------|:-----:|
| Unit price | 10.08 – 99.96 | [OK] |
| Quantity | 1 – 10 | [OK] |
| Total | $10.68 – $1,042.65 | [OK] |
| Rating | 4.0 – 10.0 | [OK] |
| gross income | $0.51 – $49.65 | [OK] |

---

## 5. Field Utama untuk Analisis

Berdasarkan pertanyaan bisnis dan sub-pertanyaan analitik, berikut field utama yang akan digunakan:

| Prioritas | Field | Peran dalam Analisis |
|:---------:|-------|---------------------|
| [PRIMER] **Primer** | **Total** | Metrik utama — nilai penjualan |
| [PRIMER] **Primer** | **Date** | Dimensi waktu — tren penjualan |
| [PRIMER] **Primer** | **City / Branch** | Dimensi cabang — perbandingan antar kota |
| [SEKUNDER] **Sekunder** | **Product line** | Dimensi produk — performa kategori |
| [SEKUNDER] **Sekunder** | **Rating** | Metrik kepuasan — korelasi dengan penjualan |
| [SEKUNDER] **Sekunder** | **Customer type** | Segmen pelanggan — analisis member vs normal |
| [BLUE] **Tersier** | **Payment** | Metode bayar — preferensi pembayaran |
| [BLUE] **Tersier** | **Quantity** | Volume — jumlah item per transaksi |
| [BLUE] **Tersier** | **Time** | Waktu — jam sibuk |
| [PENDUKUNG] **Pendukung** | **Gender** | Demografi — filter tambahan |

---

## 6. Persiapan di Tableau

### Langkah-langkah:

1. **Import CSV** ke Tableau (Connect → Text File)
2. **Verifikasi tipe data** otomatis:
   - `Date` → Date (M/D/YYYY)
   - `Time` → Text (akan dibuatkan `Hour` sebagai calculated field)
   - Semua numerik → Number
   - Sisanya → Text (kategorikal)
3. **Buat Calculated Field** untuk memperkaya analisis:
   - `Hour` = `INT(LEFT([Time], 2))` — jam transaksi
   - `Day of Week` = `DATENAME('weekday', [Date])` — nama hari
   - `Month` = `DATENAME('month', [Date])` — bulan
   - `Revenue per Unit` = `[Total] / [Quantity]` — harga rata-rata per item
4. **Data siap** untuk tahap analisis selanjutnya

### Catatan:
Tidak ada perubahan struktur data yang signifikan karena dataset sudah dalam kondisi baik. Semua langkah di atas bersifat standarisasi format untuk memudahkan visualisasi dan kalkulasi di Tableau.

---

*Lanjut ke **Tahap 3: Pembersihan Data** setelah dokumen ini disetujui.*

---

# Tahap 3: Pembersihan Data (Data Cleaning)
## Supermarket Sales Analysis — Tableau

---

## 1. Tujuan Pembersihan Data

Membersihkan dan memvalidasi dataset supermarket_sales.csv agar siap untuk tahap analisis eksploratif dan visualisasi di Tableau. Fokus utama:
1. **Missing Values** — Pastikan tidak ada data kosong
2. **Duplikasi** — Pastikan tidak ada transaksi ganda
3. **Inkonsistensi Format** — Validasi konsistensi nilai kategorikal
4. **Outlier** — Deteksi nilai ekstrem yang mempengaruhi analisis
5. **Tipe Data** — Konversi Date & Time dari String

---

## 2. Langkah Pembersihan di Tableau

### 2.1. Import Data

**Langkah di Tableau:**
1. Buka Tableau → Connect → **Text File**
2. Pilih `supermarket_sales.csv`
3. Tableau akan otomatis mendeteksi tipe data

---

### 2.2. Pengecekan Tipe Data

**Langkah:**
1. Buka tab **Data Source** (bagian kiri bawah)
2. Perhatikan ikon di setiap kolom:
   - `#` = Numerik (Abc) = String,  (Kalender) = Date,  (Jam) = Time

**Hasil Pengecekan:**

| Field | Tipe Tableau | Valid? |
|-------|-------------|:------:|
| Invoice ID | String (Abc) | [OK] |
| Branch | String (Abc) | [OK] |
| City | String (Abc) | [OK] |
| Customer type | String (Abc) | [OK] |
| Gender | String (Abc) | [OK] |
| Product line | String (Abc) | [OK] |
| Unit price | Number (decimal) # | [OK] |
| Quantity | Number (whole) # | [OK] |
| Tax 5% | Number (decimal) # | [OK] |
| Total | Number (decimal) # | [OK] |
| Date | **String (Abc)** | [NO] → **Ubah ke Date** |
| Time | **String (Abc)** | [NO] → **Ubah ke Time** |
| Payment | String (Abc) | [OK] |
| cogs | Number (decimal) # | [OK] |
| gross margin percentage | Number (decimal) # | [OK] |
| gross income | Number (decimal) # | [OK] |
| Rating | Number (decimal) # | [OK] |

---

### 2.3. Konversi Date & Time

**Date (String → Date):**
1. Di Data Source, klik dropdown pada kolom `Date`
2. Pilih **Change Data Type → Date**
3. Tableau akan otomatis mem-parse format `M/D/YYYY`
4. **Screenshot:** *(Abadikan momen ini — klik kanan Date → Change Data Type → Date)*

**Time (String → Time):**
1. Di Data Source, klik dropdown pada kolom `Time`
2. Pilih **Change Data Type → Datetime** (Tableau tidak punya tipe Time murni)
3. Atau biarkan sebagai String dan buat **Calculated Field** untuk ekstrak jamnya:
   ```
   Hour = INT(LEFT([Time], 2))
   ```
4. **Screenshot:** *(Abadikan momen ini)*

---

### 2.4. Pengecekan Missing Values

**Langkah di Tableau:**
1. Buat **New Worksheet**
2. Drag semua field ke **Rows** (satu per satu)
3. Perhatikan jumlah baris yang tampil — jika semua menunjukkan 1.000, maka [OK]
4. Cara alternatif: Drag semua field ke label dan cek apakah ada `(null)`

**Cara cepat dengan Tableau:**
1. Buat worksheet baru
2. Drag `Invoice ID` ke **Rows**
3. Drag `Measure Names` ke **Filters** → pilih semua Measure
4. Drag `Measure Values` ke **Text**
5. Cari baris yang memiliki nilai `Null`

**Hasil: TIDAK ADA MISSING VALUES.**
Semua 17 kolom memiliki 1.000 nilai valid dari 1.000 baris.
**Screenshot:** *(Tampilkan worksheet dengan count per field)*

---

### 2.5. Pengecekan Duplikasi

**Langkah di Tableau:**
1. Buat worksheet baru
2. Drag `Invoice ID` ke **Rows**
3. Klik kanan `Invoice ID` → **Measure → Count**
4. Drag `Invoice ID` lagi → **Measure → Count (Distinct)**
5. Bandingkan: `COUNT = 1.000` dan `COUNTD = 1.000` → **SAMA**

**Hasil: TIDAK ADA DUPLIKASI.**
Setiap Invoice ID unik — 1.000 nilai unik.
**Screenshot:** *(Tampilkan baris dengan COUNT dan COUNTD)*

---

### 2.6. Pengecekan Inkonsistensi Format Kategorikal

**Langkah di Tableau:**
1. Buka Data Source tab
2. Klik header kolom `City` → **Sort ascending**
3. Amati: Yangon, Mandalay, Naypyitaw — konsisten [OK]
4. Repeat untuk: `Product line`, `Payment`, `Customer type`, `Gender`

**Hasil Pengecekan Kategorikal:**

| Field | Nilai Unik | Format Konsisten? |
|-------|-----------|:-----------------:|
| City | Yangon, Mandalay, Naypyitaw | [OK] |
| Branch | A, B, C | [OK] |
| Customer type | Member, Normal | [OK] |
| Gender | Male, Female | [OK] |
| Product line | 6 kategori (capitalized consistently) | [OK] |
| Payment | Cash, Ewallet, Credit card | [OK] |

**Screenshot:** *(Tampilkan Data Source dengan kolom kategorikal yang sudah disortir)*

---

### 2.7. Pengecekan Outlier (Box Plot)

**Langkah di Tableau — Box Plot Total:**
1. Buat worksheet baru
2. Drag `Total` ke **Columns**
3. Drag `City` ke **Rows**
4. Klik kanan di canvas → **Distribution Band → Box Plot**
5. Atur: **IQR Outlier Detection**

**Hasil:**
- `Total` berkisar $10.68 – $1,042.65
- Tidak ada outlier signifikan per cabang
- Distribusi relatif normal

**Langkah — Box Plot Rating:**
1. Buat worksheet baru
2. Drag `Rating` ke **Columns**
3. Drag `Product line` ke **Rows**
4. Buat **Box Plot** dengan cara yang sama

**Hasil:**
- Rating 4.0 – 10.0
- Tidak ada outlier ekstrem
- Sebaran normal

**Screenshot:** *(Tampilkan Box Plot Total per City dan Rating per Product line)*

---

### 2.8. Pengecekan Validasi Numerik

| Field | Nilai Min | Nilai Max | Range Wajar? |
|-------|-----------|-----------|:------------:|
| Unit price | $10.08 | $99.96 | [OK] |
| Quantity | 1 | 10 | [OK] |
| Tax 5% | $0.51 | $49.65 | [OK] (5% dari Total) |
| Total | $10.68 | $1,042.65 | [OK] |
| cogs | $10.16 | $993.00 | [OK] (Total - Tax) |
| gross income | $0.51 | $49.65 | [OK] (Total - cogs) |

**Verifikasi Relasi:**
- `Total = cogs + gross income` [OK]
- `gross income = Total - cogs` [OK]
- `Tax 5% = Total × 5/105` [OK] (karena Total sudah termasuk pajak)

---

## 3. Ringkasan Pembersihan

| Aspek | Status | Detail |
|-------|:-----:|--------|
| **Missing Values** | [OK] Bersih | 0 null dari 1.000 baris × 17 kolom |
| **Duplikasi** | [OK] Bersih | 0 duplikat |
| **Inkonsistensi Format** | [OK] Bersih | Semua nilai kategorikal konsisten |
| **Outlier** | [OK] Bersih | Tidak ada outlier ekstrem |
| **Konversi Date** | [OK] Selesai | String → Date (M/D/YYYY) |
| **Konversi Time** | [OK] Selesai | String → Time / Hour extracted |

### Keputusan:
**TIDAK ADA pembersihan data yang diperlukan secara substansial.** Dataset sudah dalam kondisi sangat bersih. Langkah yang dilakukan hanyalah:
1. Konversi tipe data Date & Time
2. Ekstraksi field turunan (Hour, Day of Week)

### Field Tambahan yang Dibuat:
| Calculated Field | Formula Tableau |
|-----------------|----------------|
| Hour | `INT(LEFT([Time], 2))` |
| Day of Week | `DATENAME('weekday', [Date])` |
| Month | `DATENAME('month', [Date])` |
| Revenue per Unit | `[Total] / [Quantity]` |

---

## 4. Screenshot Checklist

| # | Screenshot | Sudah? |
|:-:|-----------|:------:|
| 1 | Data Source — tipe data Date diubah ke Date | [ ] |
| 2 | Data Source — tipe data Time atau Hour CF | [ ] |
| 3 | Missing values check — 0 null untuk semua field | [ ] |
| 4 | Duplicate check — COUNT vs COUNTD = 1.000 | [ ] |
| 5 | Inkonsistensi format — sortir kategorikal | [ ] |
| 6 | Box Plot Total per City | [ ] |
| 7 | Box Plot Rating per Product line | [ ] |
| 8 | Calculated Fields — daftar CF yang dibuat | [ ] |

---

*Lanjut ke **Tahap 4: Analisis Eksploratif & Mendalam** setelah pembersihan selesai.*

---

# Tahap 4: Analisis Eksploratif dan Analisis Mendalam
## Supermarket Sales Analysis — Tableau

---

## 1. EDA — Distribusi Data Dasar

### 1.1. Histogram Total Transaksi

**Langkah Tableau:**
1. Buat worksheet baru
2. Drag `Total` ke **Columns**
3. Klik kanan `Total` → **Create → Bins...** → Size = 50
4. Drag `Total (bin)` ke **Columns**
5. Drag `Invoice ID` ke **Rows** → **Count**
6. Tambahkan `City` sebagai **Color**

**Interpretasi:**
Distribusi `Total` miring ke kanan (right-skewed) — mayoritas transaksi bernilai kecil-menengah ($10–$400), dengan sedikit transaksi besar ($800–$1,042). Ini adalah pola normal untuk data retail.

**Screenshot:** *(Histogram Total dengan bin size 50)*

---

### 1.2. Distribusi Rating

**Langkah Tableau:**
1. Buat worksheet baru
2. Drag `Rating` ke **Columns**
3. Klik kanan `Rating` → **Create → Bins...** → Size = 1
4. Drag `Rating (bin)` ke **Columns**
5. Drag `Invoice ID` ke **Rows** → Count
6. Tambahkan `Product line` sebagai **Color**

**Data Aktual:**
| Rating Range | Jumlah Transaksi | Persentase |
|:-----------:|:----------------:|:----------:|
| 4.0 – 5.0 | 174 | 17.4% |
| 6.0 – 7.0 | 345 | 34.5% |
| 8.0 – 9.0 | 330 | 33.0% |
| 10.0 | 151 | 15.1% |

**Insight:**
Mayoritas pelanggan memberi rating 6-9 (67.5%). Rating rendah (<5) hanya 17.4% — tingkat kepuasan tergolong baik. Tidak ada rating di bawah 4.0.

**Screenshot:** *(Histogram Rating dengan bin size 1)*

---

### 1.3. Distribusi Quantity

**Langkah Tableau:**
1. Buat worksheet baru
2. Drag `Quantity` ke **Columns** (ubah ke **Dimension**)
3. Drag `Invoice ID` ke **Rows** → Count

**Insight:**
Mayoritas transaksi membeli 5-7 unit produk. Quantity range: 1-10 unit per transaksi.

**Screenshot:** *(Bar chart distribusi Quantity)*

---

## 2. Analisis Tren Waktu (Sub-Pertanyaan 1)

> **Q1:** *Bagaimana tren penjualan harian dan mingguan di setiap cabang selama periode Jan-Mar 2019?*

### 2.1. Tren Penjualan Harian per Cabang

**Langkah Tableau:**
1. Buat worksheet baru → "Trend Penjualan Harian"
2. Drag `Date` ke **Columns** → pilih **DAY** (continuous)
3. Drag `Total` ke **Rows** → **SUM**
4. Drag `City` ke **Color**
5. Klik kanan canvas → **Dual Axis** (opsional)

**Data Aktual:**
- Naypyitaw: $110,568.71 (total tertinggi, meski jumlah transaksi paling sedikit = 328)
- Yangon: $106,200.37 (340 transaksi — paling banyak transaksi, tapi revenue lebih rendah)
- Mandalay: $106,197.67 (332 transaksi)

**Insight:**
Naypyitaw unggul dalam **average transaction value** ($337.10 vs $312.35 Yangon vs $319.87 Mandalay). Meskipun volume transaksi paling sedikit, Naypyitaw menghasilkan revenue tertinggi.

**Screenshot:** *(Line chart tren harian per City)*

### 2.2. Penjualan per Hari dalam Seminggu

**Langkah Tableau:**
1. Buat worksheet baru → "Penjualan per Hari"
2. Drag `Date` ke **Columns** → pilih **WEEKDAY**
3. Drag `Total` ke **Rows** → **SUM**
4. Drag `City` ke **Color**

**Insight:**
Hari tertentu di akhir pekan menunjukkan volume tinggi. Hal ini berguna untuk penjadwalan staf dan promosi.

### 2.3. Jam Sibuk (Peak Hours)

**Langkah Tableau:**
1. Buat worksheet baru → "Jam Sibuk"
2. Drag `Hour` (calculated field) ke **Columns**
3. Drag `Invoice ID` ke **Rows** → **Count**
4. Drag `City` ke **Color**

**Data Aktual:**
| Jam | Jumlah Transaksi | Total Revenue |
|:---:|:----------------:|:------------:|
| 10:00 | 101 | $31,421.48 |
| 13:00 | 103 | $34,723.23 |
| 15:00 | 102 | $31,179.51 |
| 19:00 | **113** | **$39,699.51** (PUNCAK) |
| 20:00 | 75 | $22,969.53 |

**Insight:**
Jam 19:00 (7-8 PM) adalah puncak aktivitas belanja — 113 transaksi dengan revenue $39,699.51. Ini adalah "golden hour" untuk operasional. Sebaliknya, jam 17:00-18:00 cenderung sepi.

**Rekomendasi:** Tambah kasir dan staf di jam 18:30-19:30 untuk mengoptimalkan peak hour. Pertimbangkan promosi "happy hour" di jam sepi (17:00-18:00).

**Screenshot:** *(Bar chart jam sibuk)*

---

## 3. Analisis Performa Produk (Sub-Pertanyaan 2)

> **Q2:** *Kategori produk apa yang paling berkontribusi terhadap total pendapatan?*

### 3.1. Revenue per Product Line

**Langkah Tableau:**
1. Buat worksheet baru → "Revenue per Product"
2. Drag `Product line` ke **Rows**
3. Drag `Total` ke **Columns** → **SUM**
4. Drag `Total` ke **Label** — format sebagai Currency
5. Tambahkan `City` sebagai **Color** (stacked)

**Data Aktual:**
| Product Line | Total Revenue | % Kontribusi |
|-------------|:------------:|:------------:|
| Food and beverages | $56,144.84 | **17.38%** |
| Sports and travel | $55,122.83 | 17.07% |
| Electronic accessories | $54,337.53 | 16.82% |
| Fashion accessories | $54,305.89 | 16.81% |
| Home and lifestyle | $53,861.91 | 16.68% |
| Health and beauty | $49,193.74 | **15.23%** (terendah) |

**Insight:**
Kontribusi relatif merata antar kategori (15-17%). Food & beverages unggul tipis. Health & beauty paling rendah — 5 kategori lainnya hampir identik.

**Screenshot:** *(Bar chart Revenue per Product line)*

### 3.2. Gross Income per Product Line

**Langkah Tableau:**
1. Buat worksheet baru → "Gross Income per Product"
2. Drag `Product line` ke **Rows**
3. Drag `gross income` ke **Columns** → **SUM**

**Data Aktual:**
| Product Line | Gross Income |
|-------------|:-----------:|
| Food and beverages | $2,673.56 |
| Sports and travel | $2,624.90 |
| Electronic accessories | $2,587.50 |
| Fashion accessories | $2,585.99 |
| Home and lifestyle | $2,564.85 |
| Health and beauty | $2,342.56 |

**Insight:** Margin keuntungan konsisten ~4.76% untuk semua produk. Tidak ada perbedaan margin antar kategori.

### 3.3. Rating per Product Line

**Langkah Tableau:**
1. Buat worksheet baru → "Rating per Product"
2. Drag `Product line` ke **Rows**
3. Drag `Rating` ke **Columns** → **AVG**
4. Tambahkan reference line untuk rata-rata keseluruhan (6.97)

**Data Aktual:**
| Product Line | Average Rating |
|-------------|:------------:|
| Food and beverages | **7.11** (tertinggi) |
| Fashion accessories | 7.03 |
| Health and beauty | 7.00 |
| Sports and travel | 6.92 |
| Electronic accessories | 6.92 |
| Home and lifestyle | **6.84** (terendah) |

**Insight:**
Food & beverages memiliki rating tertinggi (7.11) — artinya pelanggan paling puas dengan produk ini. Home & lifestyle paling rendah (6.84). Namun, semua kategori masih di atas 6.8 dari skala 10.

**Screenshot:** *(Bar chart rating per Product line dengan reference line)*

### 3.4. Preferensi Produk per Cabang

**Langkah Tableau:**
1. Buat worksheet baru → "Produk per Cabang"
2. Drag `City` ke **Columns**
3. Drag `Product line` ke **Rows**
4. Drag `Total` ke **Text** → **SUM**
5. Drag `Total` ke **Color** → **SUM**
6. Atur **Marks** ke **Square** (Heatmap)

**Data Aktual (Revenue):**
| Produk \ City | Mandalay | Naypyitaw | Yangon |
|--------------|:--------:|:---------:|:------:|
| Electronic accessories | $17,051 | $18,969 | $18,317 |
| Fashion accessories | $16,413 | $21,560 | $16,333 |
| Food and beverages | $15,215 | $23,767 | $17,163 |
| Health and beauty | $19,981 | $16,615 | $12,598 |
| Home and lifestyle | $17,549 | $13,896 | $22,417 |
| Sports and travel | $19,988 | $15,762 | $19,373 |

**Insight:**
- **Naypyitaw**: Dominasi Food & beverages ($23,767) dan Fashion accessories ($21,560) — cabang ini paling kuat di kategori lifestyle
- **Yangon**: Unggul di Home & lifestyle ($22,417) dan Sports & travel ($19,373)
- **Mandalay**: Cenderung merata dengan Sports & travel ($19,988) dan Health & beauty ($19,981) sebagai yang tertinggi

**Rekomendasi:** Strategi promosi harus berbeda per cabang — Naypyitaw fokus F&B, Yangon fokus Home & lifestyle.

**Screenshot:** *(Heatmap produk per cabang)*

---

## 4. Analisis Pelanggan (Sub-Pertanyaan 3)

> **Q3:** *Bagaimana pengaruh tipe pelanggan (Member vs Normal) dan metode pembayaran terhadap nilai transaksi dan rating?*

### 4.1. Perbandingan Member vs Normal

**Langkah Tableau:**
1. Buat worksheet baru → "Member vs Normal"
2. Drag `Customer type` ke **Columns**
3. Drag `Total` ke **Rows** → **SUM**
4. Drag `Total` ke **Label**

**Data Aktual:**
| Metrik | Member | Normal | Selisih |
|--------|:------:|:------:|:-------:|
| Jumlah Transaksi | 501 | 499 | +2 |
| Total Revenue | $164,223.44 | $158,743.31 | +$5,480.13 |
| Avg Spend per Transaksi | **$327.79** | $318.12 | +$9.67 |
| Avg Rating | 6.94 | **7.01** | -0.07 |

**Insight:**
Member menghabiskan **$9.67 lebih banyak** per transaksi dibanding pelanggan normal ($327.79 vs $318.12), atau sekitar +3% lebih tinggi. Namun, rating member sedikit **lebih rendah** (6.94 vs 7.01) — mungkin karena ekspektasi yang lebih tinggi.

**Screenshot:** *(Bar chart Member vs Normal total revenue)*

### 4.2. Preferensi Produk: Member vs Normal

**Langkah Tableau:**
1. Buat worksheet baru → "Produk Favorit per Segmen"
2. Drag `Product line` ke **Rows**
3. Drag `Customer type` ke **Columns**
4. Drag `Total` ke **Text** → **SUM**
5. Drag `Total` ke **Color**

### 4.3. Analisis Metode Pembayaran

**Langkah Tableau:**
1. Buat worksheet baru → "Preferensi Pembayaran"
2. Drag `Payment` ke **Columns**
3. Drag `Total` ke **Rows** → **SUM**
4. Drag `Customer type` ke **Color**

**Data Aktual:**
| Payment | Count | Total Revenue | Avg Rating |
|---------|:-----:|:------------:|:----------:|
| Cash | 344 | $112,206.57 | 6.97 |
| Ewallet | 345 | $109,993.11 | 6.95 |
| Credit card | 311 | $100,767.07 | **7.00** |

**Insight:**
Cash dan Ewallet hampir sama populer. Credit card paling sedikit digunakan. Pelanggan Credit card memberi rating sedikit lebih tinggi (7.00).

**Screenshot:** *(Bar chart preferensi pembayaran)*

### 4.4. Metode Pembayaran per Tipe Pelanggan

**Langkah Tableau:**
1. Buat worksheet baru → "Payment x Customer Type"
2. Drag `Payment` ke **Columns**
3. Drag `Customer type` ke **Color**
4. Drag `Invoice ID` ke **Rows** → **Count**
5. Pilih **Stacked Bar**

---

## 5. Analisis Korelasi (Sub-Pertanyaan 4)

> **Q4:** *Apakah terdapat korelasi antara rating kepuasan dengan nilai transaksi, jumlah item, atau waktu transaksi?*

### 5.1. Scatter Plot: Total vs Rating

**Langkah Tableau:**
1. Buat worksheet baru → "Total vs Rating"
2. Drag `Total` ke **Columns**
3. Drag `Rating` ke **Rows**
4. Drag `City` ke **Color**
5. Tambahkan **Trend Line** (klik kanan → Trend Line → Linear)

**Insight:**
Tidak ada korelasi kuat antara nilai transaksi dengan rating. Pelanggan dengan transaksi $10 bisa memberi rating 10, dan transaksi $1,000 bisa memberi rating 5. Kepuasan tidak tergantung pada nominal belanja.

**Screenshot:** *(Scatter plot Total vs Rating dengan trend line)*

### 5.2. Scatter Plot: Quantity vs Rating

**Langkah Tableau:**
1. Buat worksheet baru → "Quantity vs Rating"
2. Drag `Quantity` ke **Columns**
3. Drag `Rating` ke **Rows**
4. Tambahkan **Trend Line**

**Insight:**
Jumlah item yang dibeli juga tidak berkorelasi signifikan dengan rating.

### 5.3. Rata-rata Rating per Jam

**Langkah Tableau:**
1. Buat worksheet baru → "Rating per Jam"
2. Drag `Hour` ke **Columns**
3. Drag `Rating` ke **Rows** → **AVG**
4. Drag `City` ke **Color**

**Insight:**
Rating cenderung lebih tinggi di jam-jam tertentu. Jam sibuk (19:00) memiliki rating yang cukup baik — artinya staf masih mampu melayani dengan baik di jam padat.

---

## 6. Analisis Demografi (Sub-Pertanyaan 5)

> **Q5:** *Metode pembayaran apa yang paling dominan digunakan oleh tiap segmen pelanggan?*

### 6.1. Gender Distribution

**Langkah Tableau:**
1. Buat worksheet baru → "Gender Analysis"
2. Drag `Gender` ke **Columns**
3. Drag `Total` ke **Rows** → **SUM**
4. Drag `Product line` ke **Color**

### 6.2. Payment Preference by Gender

**Langkah Tableau:**
1. Buat worksheet baru → "Payment by Gender"
2. Drag `Payment` ke **Columns**
3. Drag `Gender` ke **Rows**
4. Drag `Invoice ID` ke **Text** → **Count**

---

## 7. Calculated Fields (Wajib Dibuat)

Buat semua calculated field berikut di Tableau sebelum membuat visualisasi:

| # | Nama Field | Formula | Kegunaan |
|:-:|-----------|---------|----------|
| 1 | **Hour** | `INT(LEFT([Time], 2))` | Ekstrak jam dari Time untuk analisis jam sibuk |
| 2 | **Day of Week** | `DATENAME('weekday', [Date])` | Nama hari untuk analisis pola mingguan |
| 3 | **Month** | `DATENAME('month', [Date])` | Nama bulan untuk analisis tren bulanan |
| 4 | **Revenue per Unit** | `[Total] / [Quantity]` | Harga rata-rata per unit yang terjual |
| 5 | **Rating Category** | `IF [Rating] >= 9 THEN "High" ELSEIF [Rating] >= 7 THEN "Medium" ELSE "Low" END` | Kategorisasi rating untuk filter/pengelompokan |
| 6 | **Transaction Size** | `IF [Quantity] >= 7 THEN "Large" ELSEIF [Quantity] >= 4 THEN "Medium" ELSE "Small" END` | Ukuran transaksi berdasarkan jumlah item |
| 7 | **Week Number** | `DATEPART('week', [Date])` | Nomor minggu untuk analisis tren mingguan |

**Langkah:**
1. Klik kanan di panel **Data** (sebelah kiri)
2. Pilih **Create Calculated Field**
3. Masukkan nama dan formula
4. Klik **OK**

**Screenshot:** *(Tampilkan daftar Calculated Fields di panel Data)*

---

## 8. Ringkasan Temuan Analisis

| # | Temuan | Detail | Signifikansi |
|:-:|--------|--------|:-----------:|
| 1 | **Naypyitaw unggul revenue** | $110,568.71 — tertinggi meski transaksi paling sedikit | AOV Naypyitaw $337.10 vs $312.35 (Yangon) |
| 2 | **Peak hour: 19:00** | 113 transaksi, $39,699.51 | Golden hour operasional |
| 3 | **Food & Beverages terpopuler** | $56,144.84 (17.38% revenue) & rating tertinggi (7.11) | Kategori paling menguntungkan |
| 4 | **Member spend lebih tinggi** | $327.79 vs $318.12 per transaksi (+3%) | Program member efektif |
| 5 | **Tidak ada korelasi Total-Rating** | Scatter plot acak | Kepuasan tidak tergantung nominal |
| 6 | **Cash & Ewallet dominan** | Masing-masing ~34.5% transaksi | CC hanya 31.1% |
| 7 | **Rating terkonsentrasi di 6-9** | 67.5% transaksi | Kepuasan pelanggan baik |
| 8 | **Naypyitaw kuat di F&B** | $23,767 dari Food & beverages | Peluang promosi lintas kategori |
| 9 | **Mandalay terendah rating** | 6.82 vs 7.07 (Naypyitaw) | Perlu investigasi kualitas layanan |
| 10 | **Distribusi revenue merata** | 5 dari 6 kategori ~$54K | Diversifikasi produk berjalan baik |

---

## 9. Daftar Visualisasi (Checklist)

| # | Nama Sheet | Tipe Chart | Sub-Pertanyaan | Screenshot |
|:-:|-----------|:----------:|:--------------:|:----------:|
| 1 | Histogram Total | Histogram | EDA | [ ] |
| 2 | Histogram Rating | Histogram | EDA | [ ] |
| 3 | Tren Penjualan Harian | Line Chart | Q1 | [ ] |
| 4 | Penjualan per Hari | Bar Chart | Q1 | [ ] |
| 5 | Jam Sibuk | Bar Chart | Q1 | [ ] |
| 6 | Revenue per Product | Bar Chart | Q2 | [ ] |
| 7 | Gross Income per Product | Bar Chart | Q2 | [ ] |
| 8 | Rating per Product | Bar Chart | Q2 | [ ] |
| 9 | Produk per Cabang (Heatmap) | Heatmap | Q2 | [ ] |
| 10 | Member vs Normal | Bar Chart | Q3 | [ ] |
| 11 | Preferensi Pembayaran | Bar Chart | Q3 | [ ] |
| 12 | Total vs Rating (Scatter) | Scatter Plot | Q4 | [ ] |
| 13 | Rating per Jam | Bar Chart | Q4 | [ ] |
| 14 | Gender Analysis | Bar Chart | Q5 | [ ] |
| 15 | Payment by Gender | Heatmap/Bar | Q5 | [ ] |

---

*Lanjut ke **Tahap 5: Dashboard Interaktif** setelah semua sheet selesai dibuat.*

---

# Tahap 5: Dashboard Interaktif
## Supermarket Sales Analysis — Tableau

---

## 1. Tujuan Dashboard

Menggabungkan semua sheet analisis ke dalam satu dashboard interaktif yang memungkinkan stakeholder (Manajer Regional, Manajer Cabang, Tim Marketing, Tim Keuangan) untuk:
- Memonitor kinerja penjualan secara real-time
- Membandingkan performa antar cabang
- Menganalisis tren produk dan pelanggan
- Membuat keputusan berbasis data dengan filter interaktif

---

## 2. Sheet yang Akan Digunakan

Pilih **6 sheet** terbaik dari Tahap 4 untuk dimasukkan ke dashboard:

| # | Nama Sheet | Tipe | Fungsi dalam Dashboard |
|:-:|-----------|:----:|----------------------|
| 1 | **Revenue Trend** | Line Chart | Tren penjualan harian per cabang (ringkasan utama) |
| 2 | **Product Performance** | Bar Chart | Revenue & rating per product line |
| 3 | **Customer Analysis** | Bar Chart | Member vs Normal comparison |
| 4 | **Hourly Activity** | Bar Chart | Peak hours analysis |
| 5 | **City Comparison** | Side-by-side Bar | Perbandingan metrik antar cabang |
| 6 | **Rating Distribution** | Histogram | Sebaran rating kepuasan |

---

## 3. Pembuatan Quick Filters (Minimal 2)

### Filter 1: City (Drop-down)

**Langkah:**
1. Di dashboard, klik kanan area kosong → **Filter** → **City**
2. Atur sebagai **Single Value (drop-down)**
3. Ceklis **Show Filter**
4. Pindahkan ke posisi yang diinginkan

### Filter 2: Product line (Drop-down)

**Langkah:**
1. Klik kanan → **Filter** → **Product line**
2. Atur sebagai **Single Value (drop-down)**
3. Ceklis **Show Filter**

### Filter 3: Customer type (Drop-down — Opsional)

**Langkah:**
1. Klik kanan → **Filter** → **Customer type**
2. Bisa ditambahkan jika ada ruang

### Filter 4: Date Range (Slider — Opsional)

**Langkah:**
1. Klik kanan → **Filter** → **Date**
2. Pilih **Range of Date** → **Show Filter**

---

## 4. Pembuatan Filter Actions (Minimal 1)

### Action 1: Klik Cabang → Filter Semua Sheet

**Langkah:**
1. Klik menu **Dashboard** → **Actions**
2. Klik **Add Action → Filter**
3. Isi konfigurasi:
   - **Name:** "Filter by City"
   - **Source Sheets:** Pilih sheet yang akan jadi sumber klik (misal: Revenue Trend)
   - **Target Sheets:** Pilih semua sheet lain
   - **Target Filters:** Selected Fields → `City`
   - **Clearing the Selection:** Show all values
4. Klik **OK**

### Action 2: Klik Product → Filter Detail (Opsional)

**Langkah:**
1. **Add Action → Filter**
2. **Name:** "Filter by Product"
3. **Source Sheets:** Product Performance
4. **Target Sheets:** Customer Analysis, Hourly Activity
5. **Target Filters:** Selected Fields → `Product line`

---

## 5. Pembuatan Parameter (Minimal 1)

### Parameter 1: Top N Products

**Langkah:**
1. Klik kanan di panel **Data** → **Create Parameter**
2. **Name:** "Top N Products"
3. **Data Type:** Integer
4. **Allowable Values:** Range
   - Minimum: 1
   - Maximum: 6
   - Step Size: 1
5. Klik **OK**

**Cara Menggunakan:**
1. Buat worksheet baru
2. Drag `Product line` ke **Rows**
3. Drag `Total` ke **Columns** → **SUM**
4. Drag `Product line` ke **Filters** → **Top** → **By Field**
   - Top: `[Top N Products]` (pilih dari parameter)
   - By: SUM(Total), Descending
5. Tampilkan parameter: Klik kanan parameter → **Show Parameter Control**

### Parameter 2: Metric Selector (Opsional)

**Langkah:**
1. **Create Parameter**
2. **Name:** "Selected Metric"
3. **Data Type:** String
4. **Allowable Values:** List
   - Value: "Revenue" | Display: "Total Revenue"
   - Value: "Quantity" | Display: "Quantity Sold"
   - Value: "Rating" | Display: "Avg Rating"
5. Buat **Calculated Field**:
   ```
   CASE [Selected Metric]
     WHEN "Revenue" THEN SUM([Total])
     WHEN "Quantity" THEN SUM([Quantity])
     WHEN "Rating" THEN AVG([Rating])
   END
   ```
6. Gunakan field ini di visualisasi

---

## 6. Layout Dashboard

### 6.1. Desain Layout

```
┌──────────────────────────────────────────────────────────────────┐
│  [DASHBOARD] SUPERMARKET SALES DASHBOARD — Jan-Mar 2019                   │
├──────────────────────────────────────────────────────────────────┤
│  [[CITY] City: ▼ All]    [[OUTPUT] Product: ▼ All]    [[CUSTOMER] Customer: ▼ All] │
├──────────────────────────────┬───────────────────────────────────┤
│                              │                                   │
│  REVENUE TREND               │  PRODUCT PERFORMANCE              │
│  (Line Chart)                │  (Bar Chart)                      │
│                              │                                   │
│                              │                                   │
├──────────────────────────────┴───────────────────────────────────┤
│                              │                                   │
│  CUSTOMER ANALYSIS           │  HOURLY ACTIVITY                  │
│  (Bar Chart: Member vs Normal)│  (Bar Chart: Peak Hours)         │
│                              │                                   │
├──────────────────────────────┴───────────────────────────────────┤
│  CITY COMPARISON                         │  RATING DISTRIBUTION   │
│  (Side-by-side bars)                     │  (Histogram)           │
│                                          │                       │
├──────────────────────────────────────────┴───────────────────────┤
│  [PROCESS] Filter Action aktif: Klik cabang → filter semua sheet        │
│  [DATA] Parameter: Top N Products [1] [2] [3] [4] [5] [6]           │
└──────────────────────────────────────────────────────────────────┘
```

### 6.2. Langkah Layout di Tableau

1. Klik ikon **New Dashboard** (bagian bawah)
2. Atur **Size**: pilih **Automatic** atau **Fixed** (recommended: 1200×900)
3. Drag sheet satu per satu ke layout area
4. Atur posisi dan ukuran dengan drag border

### 6.3. Menambahkan Judul & Teks

1. Drag **Text** object dari panel **Objects** (kiri) ke dashboard
2. Ketik judul: **"[DASHBOARD] Supermarket Sales Dashboard — Jan-Mar 2019"**
3. Atur font size 24-28, bold
4. Tambahkan **subtitle** dengan metrik utama:
   ```
   Total Revenue: $322,966.75 | Avg Rating: 6.97/10 | Total Transactions: 1,000
   ```

### 6.4. Menambahkan Blank Container

1. Drag **Horizontal** atau **Vertical** container untuk grouping
2. Masukkan sheet + filter ke dalam container
3. Atur padding dan border

---

## 7. Formatting & Finishing

### 7.1. Warna dan Tema

**Color Palette (Rekomendasi):**
- Naypyitaw: [GREEN] Green
- Yangon: [BLUE] Blue
- Mandalay: [ORANGE] Orange

**Langkah:**
1. Klik kanan legend → **Edit Colors**
2. Pilih **Assign Palette** → atur sesuai preferensi
3. Gunakan **Color Blind Safe** palette jika perlu

### 7.2. Tooltip

**Langkah:**
1. Klik sheet di dashboard
2. Klik **Tooltip** di Marks card
3. Tambahkan informasi relevan:
   ```
   City: <City>
   Revenue: <SUM(Total)>
   Transactions: <COUNT(Invoice ID)>
   ```

### 7.3. Format Angka

**Langkah:**
1. Klik kanan field `Total` → **Default Properties → Number Format**
2. Pilih **Currency (Custom)** → $ → 2 decimal
3. Untuk `Rating` → Number → 2 decimal

---

## 8. Uji Coba Dashboard

Pastikan semua fungsi interaktif berjalan:

| Fitur | Cara Uji | Hasil |
|-------|---------|:-----:|
| **Quick Filter City** | Pilih "Naypyitaw" | Semua sheet menampilkan data Naypyitaw saja |
| **Quick Filter Product** | Pilih "Food and beverages" | Semua sheet menampilkan data F&B |
| **Filter Action (Klik City)** | Klik "Yangon" di Revenue Trend | Sheet lain filter ke Yangon |
| **Filter Action (Klik Product)** | Klik "Health and beauty" di Product Performance | Sheet terkait filter |
| **Parameter Top N** | Ubah slider ke 3 | Menampilkan 3 produk teratas |
| **Parameter Metric** | Ganti ke "Avg Rating" | Chart berubah metrik |
| **Reset Filter** | Klik "Show All" / tanda X | Semua data kembali |

---

## 9. Export Dashboard

### 9.1. Export sebagai Image (untuk laporan)

1. Klik kanan dashboard → **Copy → Image**
2. Paste ke Word/PDF

### 9.2. Export sebagai PDF

1. **File → Print to PDF**
2. Atur layout Landscape

### 9.3. Export sebagai .twbx (WAJIB )

**.twbx = Tableau Packaged Workbook** — file yang berisi data + seluruh visualisasi.

**Langkah:**
1. **File → Export Packaged Workbook → Tableau Package (.twbx)**
2. Simpan sebagai: `Supermarket_Sales_Dashboard.twbx`
3. File ini siap dikumpulkan sebagai luaran UAS

**Aba atau siapkan** di folder:
```
luaran/Supermarket_Sales_Dashboard.twbx
```

---

## 10. Screenshot Checklist

| # | Screenshot | Sudah? |
|:-:|-----------|:------:|
| 1 | Tampilan Data Source — semua tipe data sudah benar | [ ] |
| 2 | Daftar Calculated Fields di panel Data | [ ] |
| 3 | Quick Filter: City (drop-down) | [ ] |
| 4 | Quick Filter: Product line (drop-down) | [ ] |
| 5 | Filter Action: Konfigurasi pop-up | [ ] |
| 6 | Parameter: Top N Products — show parameter control | [ ] |
| 7 | Layout dashboard — tampilan penuh | [ ] |
| 8 | Dashboard saat difilter — salah satu cabang | [ ] |
| 9 | Dashboard saat parameter diubah — Top 3 | [ ] |
| 10 | Export .twbx — file di file explorer | [ ] |

---

*Lanjut ke **Tahap 6: Sintesis Insight & Rekomendasi** setelah dashboard selesai.*

---

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

---

## Lampiran

- Screenshot preprocessing dan dashboard.
- File Tableau Packaged Workbook (.twbx).
- Dataset mentah supermarket_sales.csv.
- Output validasi scripts/validation_report.txt.
