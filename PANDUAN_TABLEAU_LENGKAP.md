# [GUIDE] PANDUAN LENGKAP TABLEAU — Supermarket Sales Analysis
## Step-by-Step dari Awal Sampai Akhir

---

## [LIST] Daftar Isi

1. [Import Data](#1-import-data)
2. [Konversi Tipe Data](#2-konversi-tipe-data)
3. [Pembersihan Data](#3-pembersihan-data-di-tableau)
4. [Calculated Fields](#4-calculated-fields)
5. [Visualisasi Analisis](#5-visualisasi-analisis)
6. [Dashboard Interaktif](#6-dashboard-interaktif)
7. [Export & Finalisasi](#7-export--finalisasi)

---

## 1. IMPORT DATA

### Langkah 1: Buka Tableau
Buka aplikasi Tableau Desktop di virtual machine kamu.

### Langkah 2: Connect ke Data
1. Di halaman awal, klik **Connect → Text File** (atau **To a File → Text File**)
2. Navigasi ke folder tempat `supermarket_sales.csv` disimpan
3. Pilih file → klik **Open**

### Langkah 3: Verifikasi Data Source
1. Tableau akan menampilkan tab **Data Source** (bagian kiri bawah)
2. Di panel **Connections**, pastikan `supermarket_sales` muncul
3. Di panel **Preview**, kamu akan melihat 1.000 baris data dalam tabel

### Layout Data Source:
```
┌────────────────────────────────────────────────────────┐
│ Connections │ Sheets                                   │
│ ┌─────────┐ │ ┌────────┬────────┬────────┬──────────┐ │
│ │supermar-│ │ │Invoice │Branch  │City    │Customer  │ │
│ │ket_sales│ │ │ID (Abc)│(Abc)   │(Abc)   │type (Abc)│ │
│ └─────────┘ │ ├────────┼────────┼────────┼──────────┤ │
│             │ │750-... │A       │Yangon  │Member    │ │
│             │ │226-... │C       │Naypyit.│Normal    │ │
│             │ │...     │...     │...     │...       │ │
└─────────────┴────────────────────────────────────────┘
```

---

## 2. KONVERSI TIPE DATA

### Kenapa Perlu?
Data dari CSV membaca:
- `Date` sebagai **String** → harus diubah ke **Date**
- `Time` sebagai **String** → harus diubah ke **Time** (atau diekstrak jamnya)

### Langkah Konversi Date:

**Cara 1 — Di Data Source:**
1. Di tab **Data Source**, cari kolom `Date`
2. Klik ikon tipe data di header (yang bertuliskan `Abc`)
3. Pilih **Date**
4. Tableau otomatis mendeteksi format `M/D/YYYY`

**Cara 2 — Di Worksheet:**
1. Di panel **Data** (kiri), cari field `Date`
2. Klik kanan → **Change Data Type → Date**

### Langkah Konversi Time:

**Opsi A — Ubah ke Datetime:**
1. Klik dropdown kolom `Time` di Data Source
2. Pilih **Change Data Type → Datetime**
3. Tableau akan membaca jamnya (tanggal default ke 1/1/1900)

**Opsi B — Buat Calculated Field Hour (REKOMENDASI):**
1. Biarkan `Time` sebagai String
2. Buat **Calculated Field** baru:
   ```
   Hour = INT(LEFT([Time], 2))
   ```

### Verifikasi:
Klik tab **Sheet 1** → di panel **Data**, pastikan:
- `Date` memiliki ikon [DATE] (Date)
- `Hour` memiliki ikon # (Number)

[OK] **SELESAI — KONVERSI TIPE DATA DONE**

---

## 3. PEMBERSIHAN DATA DI TABLEAU

Dataset ini sudah bersih, tapi kamu tetap harus **MENDOKUMENTASIKAN** proses pengecekan di Tableau dengan screenshot.

### 3.1. Cek Missing Values

**Langkah:**
1. **Sheet 1** → rename ke "Cek Missing Values"
2. Drag `Invoice ID` ke **Rows**
3. Drag **Measure Names** (di panel Data → bagian Measures) ke **Filters**
4. Pilih semua Measure → klik OK
5. Drag **Measure Values** ke **Text**
6. Perhatikan: Tidak ada baris yang kosong

**Cara Alternatif:**
1. Drag semua field ke **Rows** (satu per satu)
2. Perhatikan jumlah baris di bagian **status bar** (bawah)
3. Jika semua field = 1.000 baris → **[OK] Tidak ada missing value**

[SCREENSHOT] **SCREENSHOT 1:** Tampilkan status bar dengan 1.000 dari 1.000 baris

### 3.2. Cek Duplikasi

**Langkah:**
1. **Sheet 2** → rename ke "Cek Duplikasi"
2. Drag `Invoice ID` ke **Rows**
3. Klik kanan `Invoice ID` → **Measure → Count**
4. Drag `Invoice ID` lagi ke **Text** → **Measure → Count (Distinct)**
5. Buat **Calculated Field** untuk selisih:
   ```
   Duplicate Check = COUNT([Invoice ID]) - COUNTD([Invoice ID])
   ```
6. Drag field ini ke **Text**

**Hasil:** Jika COUNT = COUNTD = 1.000 → **[OK] Tidak ada duplikasi**

[SCREENSHOT] **SCREENSHOT 2:** Tampilkan COUNT = 1.000, COUNTD = 1.000

### 3.3. Cek Inkonsistensi Format

**Langkah:**
1. Kembali ke tab **Data Source**
2. Klik header kolom `City` → **Sort Ascending**
3. Amati: "Mandalay", "Naypyitaw", "Yangon" — semuanya konsisten [OK]
4. Ulangi untuk: `Product line`, `Payment`, `Customer type`, `Gender`

[SCREENSHOT] **SCREENSHOT 3:** Tampilkan Data Source dengan kolom kategorikal yang disortir

### 3.4. Cek Outlier dengan Box Plot

**Box Plot Total per City:**
1. **Sheet 3** → rename ke "Box Plot Total"
2. Drag `Total` ke **Columns**
3. Drag `City` ke **Rows**
4. Klik kanan di canvas → **Distribution Band → Box Plot**
5. Atur: **IQR Outlier Detection** → **Show**

**Hasil:** Tidak ada outlier ekstrem di luar whiskers.

[SCREENSHOT] **SCREENSHOT 4:** Box Plot Total per City

---

## 4. CALCULATED FIELDS

### 4.1. Daftar dan Cara Buat

Buat semua field berikut. Caranya:
1. Klik kanan di panel **Data** (sebelah kiri)
2. Pilih **Create → Calculated Field**
3. Isi **Name** dan **Formula**
4. Klik **OK**

### Field 1: Hour
```
Name: Hour
Formula: INT(LEFT([Time], 2))
```
Untuk ekstrak jam dari string time "13:08" → 13

### Field 2: Day of Week
```
Name: Day of Week
Formula: DATENAME('weekday', [Date])
```
Untuk "Monday", "Tuesday", ...

### Field 3: Month
```
Name: Month
Formula: DATENAME('month', [Date])
```
Untuk "January", "February", ...

### Field 4: Revenue per Unit
```
Name: Revenue per Unit
Formula: [Total] / [Quantity]
```
Rata-rata harga per unit yang terjual

### Field 5: Rating Category
```
Name: Rating Category
Formula: IF [Rating] >= 9 THEN "High"
         ELSEIF [Rating] >= 7 THEN "Medium"
         ELSE "Low"
         END
```
Kategorisasi rating untuk filter cepat

### Field 6: Transaction Size
```
Name: Transaction Size
Formula: IF [Quantity] >= 7 THEN "Large"
         ELSEIF [Quantity] >= 4 THEN "Medium"
         ELSE "Small"
         END
```
Berdasarkan jumlah item per transaksi

### Field 7: Week Number
```
Name: Week Number
Formula: DATEPART('week', [Date])
```
Nomor minggu dalam tahun

### Field 8: Revenue per Customer (Table Calc)
```
Name: Revenue per Customer
Formula: SUM([Total]) / COUNTD([Invoice ID])
```
Rata-rata revenue per transaksi

[SCREENSHOT] **SCREENSHOT 5:** Tampilkan panel Data dengan semua Calculated Fields

---

## 5. VISUALISASI ANALISIS

### SHEET 1: Revenue Trend (Line Chart)

Tujuan: Melihat tren penjualan harian per cabang

**Langkah:**
1. **Sheet 1** → rename ke "Revenue Trend"
2. Drag `Date` ke **Columns** → pilih **DAY** (continuous)
3. Drag `Total` ke **Rows** → **SUM**
4. Drag `City` ke **Color**
5. Drag `City` ke **Filters** → ceklis semua → **Show Filter**
6. Atur format: Klik kanan `Total` → **Default Properties → Number Format → Currency**
7. Tambahkan **Tooltip**: `City`, `Date`, `Total`

**Hasil:** Line chart 3 warna (Naypyitaw [GREEN], Yangon [BLUE], Mandalay [ORANGE])
**Insight:** Naypyitaw konsisten di atas.

[SCREENSHOT] **SCREENSHOT 6:** Revenue Trend

---

### SHEET 2: Product Performance (Bar Chart)

Tujuan: Membandingkan revenue per kategori produk

**Langkah:**
1. **Sheet 2** → rename ke "Product Performance"
2. Drag `Product line` ke **Rows**
3. Drag `Total` ke **Columns** → **SUM**
4. Drag `Total` ke **Label** → format Currency
5. Drag `City` ke **Color** (stacked bar)
6. Atur **Sort**: Klik ikon sort di toolbar → **Descending → Total**

**Hasil:** Bar chart horizontal, Food & Beverages di atas
**Insight:** 5 dari 6 kategori hampir sama.

[SCREENSHOT] **SCREENSHOT 7:** Product Performance

---

### SHEET 3: Rating Analysis

Tujuan: Melihat rating per product line

**Langkah:**
1. **Sheet 3** → rename ke "Rating Analysis"
2. Drag `Product line` ke **Rows**
3. Drag `Rating` ke **Columns** → **AVG**
4. Drag `City` ke **Color**
5. Drag `Rating` ke **Label** → **AVG** → format: Number (2 decimal)
6. Tambahkan **Reference Line**: Klik kanan sumbu X → **Add Reference Line**
   - Value: **Average**
   - Label: "Avg: 6.97"

**Hasil:** Food & Beverages rating tertinggi (7.11)
**Insight:** Home & Lifestyle perlu ditingkatkan.

[SCREENSHOT] **SCREENSHOT 8:** Rating Analysis

---

### SHEET 4: City Comparison

Tujuan: Perbandingan metrik antar cabang

**Langkah:**
1. **Sheet 4** → rename ke "City Comparison"
2. Drag `City` ke **Columns**
3. Drag `Total` ke **Rows** → **SUM**
4. Drag `Rating` ke **Rows** (kedua) → **AVG**
5. Drag `Quantity` ke **Rows** (ketiga) → **SUM**
6. Atur dual-axis jika perlu
7. Format angka dengan benar

**Hasil:** Side-by-side comparison
**Insight:** Dashboard view.

[SCREENSHOT] **SCREENSHOT 9:** City Comparison

---

### SHEET 5: Hourly Activity (Bar Chart)

Tujuan: Menganalisis jam sibuk

**Langkah:**
1. **Sheet 5** → rename ke "Hourly Activity"
2. Drag `Hour` ke **Columns**
3. Drag `Invoice ID` ke **Rows** → **Count**
4. Drag `City` ke **Color**
5. Drag `Hour` ke **Label** → **Count**
6. Atur **Sort**: Manual (0,1,2,...,23)

**Hasil:** Bar chart — jam 19:00 punya bar tertinggi
**Insight:** Golden hour = 19:00.

[SCREENSHOT] **SCREENSHOT 10:** Hourly Activity

---

### SHEET 6: Customer Analysis

Tujuan: Member vs Normal

**Langkah:**
1. **Sheet 6** → rename ke "Customer Analysis"
2. Drag `Customer type` ke **Columns**
3. Drag `Total` ke **Rows** → **SUM**
4. Drag `Total` ke **Label**
5. Drag `Product line` ke **Color** (stacked)

**Hasil:** Member sedikit lebih unggul

---

### SHEET 7: Payment Preference

Tujuan: Analisis metode pembayaran

**Langkah:**
1. **Sheet 7** → rename ke "Payment Preference"
2. Drag `Payment` ke **Columns**
3. Drag `Invoice ID` ke **Rows** → **Count**
4. Drag `Customer type` ke **Color**
5. Atur **Stacked Bar**

**Hasil:** Cash dan Ewallet dominan

---

### SHEET 8: Total vs Rating (Scatter Plot)

Tujuan: Cek korelasi

**Langkah:**
1. **Sheet 8** → rename ke "Total vs Rating"
2. Drag `Total` ke **Columns**
3. Drag `Rating` ke **Rows**
4. Drag `City` ke **Color**
5. Klik kanan → **Trend Line → Linear**
6. Perhatikan nilai R²

**Hasil:** R² mendekati 0 → tidak ada korelasi

[SCREENSHOT] **SCREENSHOT 11:** Scatter Plot

---

## 6. DASHBOARD INTERAKTIF

### 6.1. Buat Dashboard Baru

1. Klik ikon **New Dashboard** (folder [FOLDER] + plus + di bagian bawah)
2. Atur **Size**: 1200 × 900 (Fixed Size)
3. Rename ke "Supermarket Sales Dashboard"

### 6.2. Susun Layout

**Langkah:**
1. Drag **Text** dari Objects panel → Tulis judul:
   ```
   [DASHBOARD] Supermarket Sales Dashboard — Jan-Mar 2019
   Total Revenue: $322,966.75 | Avg Rating: 6.97/10 | Transactions: 1,000
   ```
2. Drag **Horizontal Container** → letakkan di bawah judul
3. Drag **Quick Filter** `City` dan `Product line` ke dalam container
4. Drag **Sheet 1 (Revenue Trend)** ke kiri atas
5. Drag **Sheet 2 (Product Performance)** ke kanan atas
6. Drag **Sheet 6 (Customer Analysis)** ke kiri bawah
7. Drag **Sheet 5 (Hourly Activity)** ke kanan bawah
8. Drag **Sheet 4 (City Comparison)** ke bagian bawah (full width)

### 6.3. Tambahkan Quick Filters

**Filter 1 — City:**
1. Klik kanan di area dashboard → **Filter → City**
2. Format: **Single Value (drop-down)**
3. Ceklis **Show Filter**
4. Drag ke posisi yang diinginkan

**Filter 2 — Product line:**
1. Klik kanan → **Filter → Product line**
2. Format: **Single Value (drop-down)**
3. Ceklis **Show Filter**

**Filter 3 — Date Range (opsional):**
1. Klik kanan → **Filter → Date**
2. Format: **Range of Date**

### 6.4. Tambahkan Filter Actions

**Action 1 — Filter by City:**
1. **Dashboard → Actions → Add Action → Filter**
2. **Name:** "Filter by City"
3. **Source Sheets:** Revenue Trend
4. **Target Sheets:** Semua sheet
5. **Target Filters:** `City`
6. **Clearing:** Show All Values

**Action 2 — Filter by Product (opsional):**
1. **Add Action → Filter**
2. **Name:** "Filter by Product"
3. **Source Sheets:** Product Performance
4. **Target Sheets:** Customer Analysis, Hourly Activity
5. **Target Filters:** `Product line`

### 6.5. Tambahkan Parameter

**Parameter — Top N Products:**
1. Klik kanan di panel Data → **Create Parameter**
2. **Name:** "Top N Products"
3. **Type:** Integer
4. **Range:** 1 to 6, step 1
5. Klik **OK**
6. **Show Parameter Control** (klik kanan parameter → Show Parameter Control)

**Cara menggunakan parameter di sheet:**
1. Buka sheet **Product Performance**
2. Drag `Product line` ke **Filters** → **Top** tab
3. Pilih **By Field**:
   - Top: `6` → ganti jadi `[Top N Products]`
   - By: `SUM(Total)`, Descending
4. Klik **OK**

### 6.6. Finalisasi Dashboard

**Warna:**
1. Klik kanan legend warna → **Edit Colors**
2. Atur: Naypyitaw [GREEN], Yangon [BLUE], Mandalay [ORANGE]
3. Gunakan **Color Blind Safe** jika perlu

**Tooltip:**
1. Klik sheet di dashboard
2. Klik **Tooltip** di Marks
3. Tambahkan informasi lengkap

**Border & Padding:**
1. Klik kanan sheet → **Format**
2. Atur **Border** dan **Padding** sesuai selera

[SCREENSHOT] **SCREENSHOT 12:** Full Dashboard

---

## 7. EXPORT & FINALISASI

### 7.1. Export Image (untuk Laporan)

1. Klik kanan dashboard → **Copy → Image**
2. Buka Word → **Paste**
3. Atau: **File → Export As → Image**

### 7.2. Export PDF

1. **File → Print to PDF**
2. Layout: **Landscape**
3. Simpan sebagai: `Supermarket_Sales_Dashboard.pdf`

### 7.3. Export .twbx (WAJIB — untuk Dikumpulkan)

**.twbx = Tableau Packaged Workbook** → File siap kumpul yang berisi data + dashboard.

**Langkah:**
1. **File → Export Packaged Workbook**
2. Pilih lokasi: `luaran/`
3. Nama file: `Supermarket_Sales_Dashboard.twbx`
4. Klik **Save**

### 7.4. Cek List Final Sebelum Kumpul

| # | Item | Format | Status |
|:-:|------|--------|:------:|
| 1 | .twbx file | File | [ ] |
| 2 | Laporan (max 20 halaman) | .docx/.pdf | [ ] |
| 3 | Slide presentasi (max 15 slide) | .pptx/.pdf | [ ] |
| 4 | Screenshot dashboard | Image | [ ] |
| 5 | Screenshot tahap cleaning | 4-5 image | [ ] |

---

## 8. SHORTCUT TABLEAU YANG MEMBANTU

| Shortcut | Fungsi |
|----------|--------|
| **Ctrl + D** | Duplicate sheet |
| **Ctrl + W** | Hapus sheet |
| **Ctrl + R** | Refresh data |
| **Ctrl + Shift + B** | Tambahkan Reference Line |
| **F7** | Show/Hide panel Data |
| **F11** | Full screen |

---

## 9. TROUBLESHOOTING UMUM

| Masalah | Solusi |
|---------|--------|
| **Date tidak terdeteksi** | Pastikan format M/D/YYYY. Coba ubah ke Date manual |
| **Parameter tidak muncul** | Klik kanan parameter → Show Parameter Control |
| **Filter Action tidak jalan** | Cek Source Sheets → pastikan field City ada di sheet tsb |
| **Dashboard terlalu penuh** | Kurangi jumlah sheet, gunakan container |
| **.twbx gagal export** | Pastikan ada cukup disk space |
| **SUM(Total) terlalu besar** | Cek apakah ada agregasi ganda |
| **AVG(Rating) salah** | Pastikan Rating adalah Average, bukan SUM |

---

## [OK] FINAL CHECKLIST

```
□ Step 1: Import data ke Tableau — DONE
□ Step 2: Konversi Date & Time — DONE
□ Step 3: Cek missing values — DONE
□ Step 4: Cek duplikasi — DONE
□ Step 5: Cek outlier — DONE
□ Step 6: Buat 8 Calculated Fields — DONE
□ Step 7: Buat 8+ sheet visualisasi — DONE
□ Step 8: Buat dashboard — DONE
□ Step 9: Tambah Quick Filters — DONE
□ Step 10: Tambah Filter Actions — DONE
□ Step 11: Tambah Parameter — DONE
□ Step 12: Export .twbx — DONE
□ Step 13: Screenshot untuk laporan — DONE
□ Step 14: Siap menyusun laporan & slide — DONE
```

---

**SELAMAT!  Dashboard Tableau Supermarket Sales selesai!**

Sekarang lanjut ke pembuatan:
1. **[REPORT] Laporan Tertulis** (max 20 halaman) → lihat TEMPLATE_LAPORAN.md
2. **[SLIDES] Slide Presentasi** (max 15 slide) → lihat TEMPLATE_SLIDE.md
