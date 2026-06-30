# [SETTING] TABLEAU WORKFLOW — STEP BY STEP GRANULAR
## Supermarket Sales Analysis

---

> **WORKFLOW INI SANGAT DETAIL** — setiap klik, setiap drag, setiap setting.
> Cocok untuk lo yang mau panduan "no step left behind" di Tableau.

---

## [GREEN] FASE 0: PERSIAPAN

### 0.1. Cek File CSV
```bash
ls -la datasets/retail/supermarket_sales.csv
```
Pastikan file ada dan tidak corrupt (size ~30KB).

### 0.2. Buka Tableau Desktop
1. Double klik icon Tableau Desktop
2. Tunggu hingga halaman **Start Page** muncul (biasanya ~5-10 detik)
3. Di sebelah kiri, ada panel **Connect**

---

## [GREEN] FASE 1: IMPORT DATA

### 1.1. Koneksi ke CSV
1. Di halaman **Start**, klik **Connect → To a File → Text File**
   - *Alternatif: Di panel Connect, klik "Text File"*
2. Navigasi ke: `datasets/retail/supermarket_sales.csv`
3. Klik file → **Open**

### 1.2. Verifikasi Data Source
Setelah terbuka, lo akan melihat tab **Data Source** (di kiri bawah, dekat ikon [CUSTOMER]).

**Ceklist Verifikasi:**
```
□ Nama koneksi: supermarket_sales (di panel Connections)
□ Jumlah baris: 1.000 (tertulis di status bar bawah)
□ Jumlah kolom: 17 (dari Invoice ID sampai Rating)
□ Semua data muncul tanpa error
```

### 1.3. Rename Data Source (Opsional)
1. Klik kanan **supermarket_sales** di panel Connections
2. Pilih **Rename** → ketik "Supermarket Sales"
3. Enter

---

## [GREEN] FASE 2: KONVERSI TIPE DATA

### 2.1. Konversi Date (String → Date)

**Cara 1 — Lewat Data Source (rekomendasi):**
1. Di tab **Data Source**, cari kolom `Date`
2. Arahin mouse ke ikon tipe data di header kolom (ikon `Abc`)
3. Klik → pilih **Date**
4. Tableau akan langsung mengubah data. Format: `M/D/YYYY`

**Cara 2 — Lewat Worksheet:**
1. Klik tab **Sheet 1** (di bawah)
2. Di panel **Data** (kiri), cari field `Date`
3. Klik kanan `Date` → **Change Data Type → Date**

[OK] **Verifikasi:** Ikon `Date` berubah dari `Abc` menjadi [DATE].
[SCREENSHOT] **SCREENSHOT:** Ambil screenshot untuk laporan (lihat SCREENSHOT_GUIDE.md - Gambar 3.1).

### 2.2. Konversi Time (String → Hour)

> **Catatan:** Tableau tidak punya tipe data "Time" murni. Solusi: buat Calculated Field untuk ekstrak jam.

1. Klik tab **Sheet 1**
2. Di panel **Data** (kiri), klik icon segitiga [DOWN] → **Create Calculated Field**
   - *Alternatif: Klik kanan di area kosong panel Data → **Create Calculated Field***
3. Isi:
   - **Name:** `Hour`
   - **Formula:** `INT(LEFT([Time], 2))`
4. Klik **OK**

[OK] **Verifikasi:** Field `Hour` muncul di panel Data dengan ikon `#` (numerik).
[SCREENSHOT] **SCREENSHOT:** Ambil screenshot Calculated Field.

### 2.3. Buat Calculated Field Lainnya (7 Field)

Ulangi langkah 2.2 untuk semua field berikut:

| # | Name | Formula | Tipe Hasil |
|:-:|------|---------|:----------:|
| 1 | **Hour** | `INT(LEFT([Time], 2))` | Number |
| 2 | **Day of Week** | `DATENAME('weekday', [Date])` | String |
| 3 | **Month** | `DATENAME('month', [Date])` | String |
| 4 | **Revenue per Unit** | `[Total] / [Quantity]` | Number |
| 5 | **Rating Category** | `IF [Rating] >= 9 THEN "High" ELSEIF [Rating] >= 7 THEN "Medium" ELSE "Low" END` | String |
| 6 | **Transaction Size** | `IF [Quantity] >= 7 THEN "Large" ELSEIF [Quantity] >= 4 THEN "Medium" ELSE "Small" END` | String |
| 7 | **Week Number** | `DATEPART('week', [Date])` | Number |

### 2.4. Verifikasi Semua Field

Buat worksheet sederhana:
1. Klik **Sheet 1** → rename ke "Verifikasi Data"
2. Drag `Invoice ID` ke **Rows**
3. Drag `Date`, `Hour`, `Total`, `Rating Category` ke **Rows**
4. Pastikan semua field muncul dengan benar

Jika ada error:
- `Date` error → cek format M/D/YYYY
- `Hour` error → cek Time format (HH:MM)
- `Rating Category` error → cek penulisan `ELSEIF` (satu kata!)

[SCREENSHOT] **SCREENSHOT:** Ambil screenshot panel Data dengan semua CF (lihat SCREENSHOT_GUIDE.md - Gambar CF).

---

## [GREEN] FASE 3: CEK KEBERSIHAN DATA

### 3.1. Cek Missing Values

**Langkah:**
1. **Sheet baru** → rename ke "Cek Missing Values"
2. Drag `Invoice ID` ke **Rows**
3. Dari panel **Data**, drag **Measure Names** (di bagian Measures) ke **Filters**
4. Di dialog, pilih **All** (centang semua measure) → **OK**
5. Dari panel **Data**, drag **Measure Values** ke **Text**
6. Perhatikan label: semua angka harus terisi

**Alternatif (lebih visual):**
1. Drag semua field (satu per satu) ke **Rows**
2. Lihat status bar di kanan bawah: harus terbaca "1.000 of 1.000 rows"
3. Jika ada field yang menunjukkan < 1.000 → ada missing value

[OK] **Hasil:** 1.000 dari 1.000 — tidak ada missing value.
[SCREENSHOT] **SCREENSHOT:** Gambar 3.1.

### 3.2. Cek Duplikasi

**Langkah:**
1. **Sheet baru** → rename ke "Cek Duplikasi"
2. Drag `Invoice ID` ke **Rows**
3. Klik kanan `Invoice ID` → **Measure → Count**
4. Drag `Invoice ID` lagi ke **Label** → **Measure → Count (Distinct)**
5. Buat **Calculated Field** untuk validasi:
   - Name: `Duplicate Check`
   - Formula: `COUNT([Invoice ID]) - COUNTD([Invoice ID])`
6. Drag `Duplicate Check` ke **Label**
7. Hasil: COUNT = 1.000, COUNTD = 1.000, Duplicate Check = 0

[OK] **Hasil:** 0 duplikasi.
[SCREENSHOT] **SCREENSHOT:** Gambar 3.2.

### 3.3. Cek Inkonsistensi Format

**Langkah:**
1. Kembali ke tab **Data Source** (di kiri bawah)
2. Arahin mouse ke header kolom `City`
3. Klik ikon sort [UP] (Sort Ascending)
4. Perhatikan: "Mandalay", "Naypyitaw", "Yangon" — konsisten
5. Ulangi untuk: `Branch`, `Product line`, `Payment`, `Customer type`, `Gender`
6. Ulangi sort [DOWN] (Descending) untuk double-check

[OK] **Hasil:** Semua konsisten, tidak ada variasi seperti "naypyitaw" vs "Naypyitaw".
[SCREENSHOT] **SCREENSHOT:** Gambar 3.3.

### 3.4. Cek Outlier dengan Box Plot

**Langkah Box Plot Total per City:**
1. **Sheet baru** → rename ke "Box Plot Total"
2. Drag `Total` ke **Columns**
3. Drag `City` ke **Rows**
4. Di **Marks** card, ubah dari `Automatic` ke `Circle`
5. Klik kanan di canvas → **Distribution Band → Box Plot**
6. Atur:
   - **Distribution:** Percentile
   - **Value:** IQR
   - **Show:** Outliers
7. Amati: ada titik di luar whiskers?

**Langkah Box Plot Rating per Product:**
1. **Sheet baru** → rename ke "Box Plot Rating"
2. Drag `Rating` ke **Columns**
3. Drag `Product line` ke **Rows**
4. Klik kanan → **Distribution Band → Box Plot**

[OK] **Hasil:** Tidak ada outlier ekstrem.
[SCREENSHOT] **SCREENSHOT:** Gambar 3.4.

---

## [GREEN] FASE 4: BUAT SHEET VISUALISASI

### 4.1. Sheet 1: Revenue Trend (Line Chart)

**Tujuan:** Tren penjualan harian per cabang

**Langkah:**
1. **Sheet baru** → rename ke "Revenue Trend"
2. Drag `Date` ke **Columns**
3. Klik kanan `Date` di Columns → pilih **Day** (continuous) — ikon hijau
4. Drag `Total` ke **Rows** → otomatis **SUM(Total)**
5. Drag `City` ke **Color** (di Marks card)
6. Drag `City` ke **Filters** → centang Yangon, Mandalay, Naypyitaw → OK
7. Klik kanan `City` di Filters → **Show Filter**
8. Format angka: Klik kanan `SUM(Total)` di Rows → **Default Properties → Number Format → Currency (Custom)** → $ → 2 decimal
9. Format judul: Klik kanan sheet tab → **Rename** → "Revenue Trend"
10. Atur tooltip: Klik **Tooltip** di Marks card → edit:

```
<Sheet name>
Date: <Date>
City: <City>
Revenue: <SUM(Total)>
```

**Verifikasi:**
- 3 garis dengan 3 warna berbeda
- Sumbu X: tanggal (continuous)
- Sumbu Y: currency $$$

[SCREENSHOT] **SCREENSHOT:** Gambar 4.1.

### 4.2. Sheet 2: Product Performance (Bar Chart)

**Tujuan:** Revenue per kategori produk

**Langkah:**
1. **Sheet baru** → rename ke "Product Performance"
2. Drag `Product line` ke **Rows**
3. Drag `Total` ke **Columns** → **SUM(Total)**
4. Drag `City` ke **Color** (stacked bar)
5. Drag `Total` ke **Label** → **SUM(Total)**
6. Klik kanan `SUM(Total)` di Label → **Default Properties → Number Format → Currency**
7. Sort: Klik ikon sort [DOWN] di toolbar → **Sort by → SUM(Total) → Descending**
8. Format judul: double klik "Sheet 2" → "Product Performance"

**Verifikasi:**
- Bar horizontal, dari terbesar ke terkecil
- Warna stacked per cabang
- Label mata uang di setiap bar

[SCREENSHOT] **SCREENSHOT:** Gambar 4.2.

### 4.3. Sheet 3: Rating Analysis (Bar Chart)

**Tujuan:** Rata-rata rating per produk

**Langkah:**
1. **Sheet baru** → rename ke "Rating Analysis"
2. Drag `Product line` ke **Rows**
3. Drag `Rating` ke **Columns** → otomatis **SUM(Rating)**
4. Klik kanan `SUM(Rating)` di Columns → **Measure → Average**
5. Drag `Rating` ke **Label** → **AVG(Rating)**
6. Format angka: Klik kanan `AVG(Rating)` → **Default Properties → Number Format → Number** → 2 decimal
7. Tambahkan **Reference Line**:
   - Klik kanan di sumbu X (angka rating)
   - Pilih **Add Reference Line**
   - **Value:** Average → **Label:** "Avg: 6.97"
   - **Line:** Dashed red

**Verifikasi:**
- Bar horizontal dengan label rating
- Reference line merah di 6.97
- Produk dengan rating di atas/bawah garis langsung terlihat

[SCREENSHOT] **SCREENSHOT:** Gambar 4.3.

### 4.4. Sheet 4: City Comparison (Side-by-Side Bars)

**Tujuan:** Perbandingan metrik antar cabang

**Langkah:**
1. **Sheet baru** → rename ke "City Comparison"
2. Drag `City` ke **Columns**
3. Drag `Total` ke **Rows** → **SUM(Total)** → format Currency
4. Drag `Product line` ke **Color**
5. Drag `City` ke **Label**
6. Untuk dual-axis (tambah metrik kedua):
   - Drag `Rating` ke **Rows** (di samping SUM(Total))
   - Klik kanan `AVG(Rating)` → **Dual Axis** (jika perlu)
   - Sinkronkan sumbu: klik kanan sumbu kanan → **Synchronize Axis**

**Verifikasi:**
- 3 bar untuk 3 cabang
- Warna stacked per produk

[SCREENSHOT] **SCREENSHOT:** Gambar bisa disatukan di dashboard nanti.

### 4.5. Sheet 5: Hourly Activity (Bar Chart)

**Tujuan:** Distribusi transaksi per jam

**Langkah:**
1. **Sheet baru** → rename ke "Hourly Activity"
2. Drag `Hour` ke **Columns**
3. Klik kanan `Hour` → **Dimension** (ubah dari Measure ke Dimension)
4. Drag `Invoice ID` ke **Rows** → **Count**
5. Drag `City` ke **Color**
6. Drag `Hour` ke **Label** → **Count**
7. Format label: klik kanan `COUNT(Invoice ID)` → Format → Pane → Numbers
8. Sort: Klik kanan `Hour` → **Sort** → **Manual** → urut 0-23

**Verifikasi:**
- Bar chart per jam (10, 11, 12, ..., 20)
- Bar tertinggi di jam 19:00 (113 transaksi)
- Warna per cabang

[SCREENSHOT] **SCREENSHOT:** Gambar 4.4.

### 4.6. Sheet 6: Customer Analysis (Stacked Bar)

**Tujuan:** Member vs Normal

**Langkah:**
1. **Sheet baru** → rename ke "Customer Analysis"
2. Drag `Customer type` ke **Columns**
3. Drag `Total` ke **Rows** → **SUM(Total)** → format Currency
4. Drag `Product line` ke **Color**
5. Drag `Total` ke **Label** → **SUM(Total)**
6. Drag `Customer type` ke **Label** (juga)

**Verifikasi:**
- 2 bar: Member dan Normal
- Member bar lebih tinggi

### 4.7. Sheet 7: Total vs Rating (Scatter Plot)

**Tujuan:** Cek korelasi

**Langkah:**
1. **Sheet baru** → rename ke "Total vs Rating"
2. Drag `Total` ke **Columns**
3. Drag `Rating` ke **Rows**
4. Drag `City` ke **Color**
5. Ubah Marks dari `Automatic` ke **Circle**
6. Klik kanan di canvas → **Trend Line → Linear**
7. Klik kanan trend line → **Describe Trend Line** → lihat R²
8. Drag `Invoice ID` ke **Label** (opsional, untuk hover detail)

**Ekspektasi:**
- R² mendekati 0 (0.00 sekian)
- Trend line hampir horizontal (datar)

[SCREENSHOT] **SCREENSHOT:** Gambar untuk slide 10 (korelasi).

### 4.8. Sheet 8: Heatmap Produk per Cabang

**Tujuan:** Visualisasi preferensi produk × cabang

**Langkah:**
1. **Sheet baru** → rename ke "Heatmap Produk"
2. Drag `City` ke **Columns**
3. Drag `Product line` ke **Rows**
4. Drag `Total` ke **Text** → **SUM(Total)** → format Currency
5. Drag `Total` ke **Color** → **SUM(Total)**
6. Di Marks card, ubah ke **Square**
7. Klik **Color** → **Edit Colors** → pilih palette **Orange-Blue Diverging**

**Verifikasi:**
- 3 × 6 grid
- Warna lebih gelap = revenue lebih tinggi
- Naypyitaw-F&B ($23,767) paling gelap

[SCREENSHOT] **SCREENSHOT:** Gambar 4.5.

---

## [GREEN] FASE 5: DASHBOARD

### 5.1. Buat Dashboard Baru

1. Klik ikon **New Dashboard** ([FOLDER] +) di bagian bawah
2. Di panel **Dashboard** (sebelah kiri):
   - **Size:** pilih **Fixed Size** → 1200 × 900
   - **Show Title:** centang
3. Rename: klik kanan tab "Dashboard 1" → rename "Supermarket Sales Dashboard"

### 5.2. Atur Layout

**Langkah demi langkah:**

**1. Tambah Judul:**
- Dari panel **Objects** (kiri, di bawah Sheets), drag **Text** ke dashboard
- Ketik:
  ```
  [DASHBOARD] Supermarket Sales Dashboard
  Jan-Mar 2019 | Total Revenue: $322,966.75 | Avg Rating: 6.97 | Transactions: 1,000
  ```
- Atur font size judul: 28, bold
- Atur font size subtitle: 14

**2. Tambah Container Horizontal untuk Filter:**
- Drag **Horizontal** dari Objects ke bawah judul
- Ini akan menjadi wadah filter

**3. Tambah Quick Filter ke Container:**
- Klik kanan **City** di panel Data (kiri) → **Show Filter**
- Drag filter City ke dalam Horizontal Container
- Klik kanan **Product line** → **Show Filter**
- Drag ke dalam Horizontal Container

**4. Atur Filter Format:**
- Klik filter City → dropdown (kanan atas filter) → **Single Value (drop-down)**
- Klik filter Product line → **Single Value (drop-down)**

**5. Susun Sheet di Layout Grid:**

| Baris | Kiri (60%) | Kanan (40%) |
|:-----:|:----------:|:-----------:|
| 1 | Revenue Trend | Product Performance |
| 2 | Customer Analysis | Hourly Activity |
| 3 | City Comparison (full width) | — |

**Langkah drag:**
1. Drag **Revenue Trend** ke area kiri atas
2. Drag **Product Performance** ke kanan (sejajar)
3. Drag **Customer Analysis** ke kiri bawah
4. Drag **Hourly Activity** ke kanan (sejajar)
5. Drag **City Comparison** ke bagian paling bawah (full width)

**6. Atur ukuran sheet:**
- Klik border sheet → drag untuk atur ukuran
- Usahakan semua sheet muat dalam 1 layar (scroll minimal)
- Atau: klik kanan tiap sheet → **Fit → Entire View**

### 5.3. Tambah Filter Actions

**Langkah:**
1. **Dashboard → Actions** (menu atas)
2. Klik **Add Action → Filter**
3. Isi konfigurasi:

```
Action Name: Filter by City
Source Sheets: Revenue Trend
Target Sheets: Product Performance, Customer Analysis, Hourly Activity, City Comparison
Target Filters: Selected Fields → City
Clearing the Selection: Show all values
Run action on: Select
```

4. Klik **OK**

**Action 2 (opsional):**
```
Action Name: Filter by Product
Source Sheets: Product Performance
Target Sheets: Customer Analysis, Hourly Activity, City Comparison
Target Filters: Selected Fields → Product line
```

5. Klik **OK** lagi

### 5.4. Tambah Parameter

**Langkah:**
1. Klik kanan di panel **Data** (kiri) → **Create Parameter**
2. Isi:
   - **Name:** Top N Products
   - **Data Type:** Integer
   - **Allowable Values:** Range
     - Minimum: 1
     - Maximum: 6
     - Step Size: 1
3. Klik **OK**
4. Klik kanan parameter **Top N Products** → **Show Parameter Control**

**Gunakan parameter di Product Performance:**
1. Buka sheet **Product Performance**
2. Drag `Product line` ke **Filters**
3. Pilih tab **Top**
4. Pilih: **By Field**
   - **Top:** 6 → klik dropdown, pilih `[Top N Products]`
   - **By:** `SUM(Total)`, **Descending**
5. Klik **OK**

### 5.5. Finalisasi Dashboard

**Edit Warna:**
1. Klik kanan legend warna di salah satu sheet → **Edit Colors**
2. Atur:
   - Mandalay → [ORANGE] Orange
   - Naypyitaw → [GREEN] Green
   - Yangon → [BLUE] Blue
3. Centang **Color Blind Safe** (opsional)

**Atur Tooltip:**
1. Klik sheet di dashboard
2. Klik **Tooltip** di Marks card
3. Tambah/tambah informasi yang berguna

**Format Dashboard:**
1. Klik kanan dashboard → **Format**
2. Atur **Shading**: background putih bersih
3. Atur **Border**: tipis di tiap sheet

**Uji Coba:**
1. Klik filter City → pilih "Naypyitaw" → semua sheet berubah? [OK]
2. Klik garis Naypyitaw di Revenue Trend → sheet lain terfilter? [OK]
3. Ubah Top N ke 3 → cuma 3 produk muncul? [OK]

[SCREENSHOT] **SCREENSHOT:** Gambar 5.1, 5.2, 5.3.

---

## [GREEN] FASE 6: EXPORT

### 6.1. Export Image Dashboard
1. Klik kanan di area dashboard → **Copy → Image**
2. Buka Paint / Word → Paste
3. Simpan sebagai: `Dashboard_Full.png`

### 6.2. Export .twbx (WAJIB !!!)
1. **File → Export Packaged Workbook**
2. Navigasi ke: `luaran/`
3. Nama file: `Supermarket_Sales_Dashboard.twbx`
4. Klik **Save**
5. Tunggu proses (biasanya 5-30 detik)
6. Verifikasi: file ada dengan `ls -la luaran/`

### 6.3. Export .pdf (Cadangan)
1. **File → Print to PDF**
2. Atur **Layout**: Landscape
3. Simpan sebagai: `Supermarket_Sales_Dashboard.pdf`

### 6.4. Publish ke Tableau Public (Opsional — untuk link presentasi)
1. **File → Save to Tableau Public As...**
2. Login (buat akun gratis di tableau.com/public)
3. Beri judul: "Supermarket Sales Dashboard"
4. Publish
5. Copy link untuk dimasukkan ke slide

---

## [GREEN] FASE 7: FINAL CHECKLIST

Sebelum kumpul, pastikan semua ini beres:

```
□ 1.000 baris teimport semua
□ Date sudah Date (bukan String)
□ Hour CF sudah berfungsi
□ 7 CF sudah dibuat
□ Missing: 0 (ada screenshot)
□ Duplikat: 0 (ada screenshot)
□ Outlier: none (ada screenshot)
□ Sheet 1: Revenue Trend (Line chart)
□ Sheet 2: Product Performance (Bar)
□ Sheet 3: Rating Analysis (Bar + ref line)
□ Sheet 4: City Comparison (Side-by-side)
□ Sheet 5: Hourly Activity (Bar)
□ Sheet 6: Customer Analysis (Stacked bar)
□ Sheet 7: Total vs Rating (Scatter)
□ Sheet 8: Heatmap Produk per Cabang
□ Dashboard: 6 sheet dalam 1 layout
□ Quick Filter: City, Product line
□ Filter Action: minimal 1
□ Parameter: Top N Products
□ .twbx tersimpan di luaran/
□ Screenshot: 13 file di screenshots/
□ Laporan siap (copy dari REPORT_READY.md)
□ Slide siap (copy dari SLIDE_READY.md)
```

---

## [WARNING] TROUBLESHOOTING CEPAT

| Error | Penyebab | Solusi |
|-------|----------|--------|
| **Date error: "The field is not recognized"** | Format date tidak standar | Pastikan M/D/YYYY. Coba ubah ke Date manual |
| **Hour error: "Unknown field Time"** | Nama field salah | Cek ejaan: `[Time]`, bukan `[time]` atau `[Waktu]` |
| **SUM(Total) terlalu besar** | Agregasi ganda | Pastikan SUM, bukan COUNT atau AVG |
| **AVG(Rating) aneh** | Default SUM | Klik kanan → Measure → Average |
| **Filter Action tidak jalan** | Field tidak ada | Cek source sheet: City harus ada di sheet tsb |
| **Parameter tidak muncul** | Tidak di-show | Klik kanan → Show Parameter Control |
| **Dashboard terlalu panjang** | Layout tidak proporsional | Atur ukuran sheet lebih kecil |
| **.twbx gagal export** | Disk penuh | Hapus file sampah, coba save di tempat lain |
| **Tableau crash** | File corrupt | Import ulang CSV, mulai dari Fase 1.1 |

---

**SELAMAT BEKERJA! [TARGET] GASKEUN! [P1]**
