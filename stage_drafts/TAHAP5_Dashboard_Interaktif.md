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
| 1 | Tampilan Data Source — semua tipe data sudah benar | [X] (assets/Data-Source.png) |
| 2 | Daftar Calculated Fields di panel Data | [X] (assets/Data-Source.png) |
| 3 | Quick Filter: City (drop-down) | [X] (assets/Revenue-Trend.png) |
| 4 | Quick Filter: Product line (drop-down) | [X] (assets/Product-Performance.png) |
| 5 | Filter Action: Konfigurasi pop-up | [X] (assets/Revenue-Trend.png) |
| 6 | Parameter: Top N Products — show parameter control | [X] (assets/Product-Performance.png) |
| 7 | Layout dashboard — tampilan penuh | [X] (assets/City-Comparison.png) |
| 8 | Dashboard saat difilter — salah satu cabang | [X] (assets/City-Comparison.png) |
| 9 | Dashboard saat parameter diubah — Top 3 | [X] (assets/Product-Performance.png) |
| 10 | Export .twbx — file di file explorer | [X] |

---

*Lanjut ke **Tahap 6: Sintesis Insight & Rekomendasi** setelah dashboard selesai.*
