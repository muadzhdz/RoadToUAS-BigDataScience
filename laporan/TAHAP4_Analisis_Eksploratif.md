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
