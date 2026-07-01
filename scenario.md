# Supermarket Sales Analysis Project
## AI CLI Execution Scenario

**Group Members:** Mu'adz Hudzaifah (24903460014), Alhaq Sabilil Izati (24903460012), Arfan Ghifari
**Dataset:** supermarket_sales.csv
**Dataset Path:** `datasets/retail/supermarket_sales.csv`
**Deadline:** Tanggal 9, pukul 23.59 sesuai brief dosen
**Project:** Automated execution via AI CLI for complete UAS deliverables

---

## TABLE OF CONTENTS (for AI CLI)

1. [Project Overview](#-project-overview)
2. [Data Specification](#-data-specification)
3. [Stage 1-6 Specifications](#-stages-1-6-specifications)
4. [Dashboard Specification](#-dashboard-specification)
5. [Output Requirements](#-output-requirements)
6. [Execution Commands](#-execution-commands)

---

## PROJECT OVERVIEW

**Objective:** Complete UAS Big Data Science deliverables via AI CLI automation

**Dataset:** 1,000 rows x 17 columns supermarket sales data
- Local path: `datasets/retail/supermarket_sales.csv`
- 3 branches: Yangon (A), Mandalay (B), Naypyitaw (C)
- Date range: 2019-01-01 to 2019-03-09
- 6 product categories, 3 payment methods
- 501 Member vs 499 Normal customers

**Main Business Question:** "Faktor apa yang paling mempengaruhi total penjualan dan tingkat kepuasan pelanggan di ketiga cabang supermarket, dan bagaimana strategi yang dapat diterapkan untuk meningkatkan pendapatan serta loyalitas pelanggan?"

**5 Sub-Questions:**
1. Bagaimana tren penjualan harian per cabang?
2. Kategori produk apa yang paling berkontribusi?
3. Member vs Normal - pengaruh ke nilai transaksi & rating?
4. Apakah rating berkorelasi dengan nilai transaksi?
5. Preferensi metode pembayaran per segmen?

**Required Outputs:**
1. Tableau Packaged Workbook (.twbx)
2. Written Report (.docx/.pdf, max 20 pages)
3. Presentation Slides (.pptx/.pdf, max 15 slides)

**Technical Boundary:** AI CLI can generate validation output, structured specs, draft report/slide files, and a `.twb` XML draft. The final `.twbx` must still be opened, verified, and exported from Tableau Desktop because Tableau Packaged Workbook is a Tableau-owned packaging format.

**Dataset Cleanliness Note:** Dataset is already very clean: 0 missing values and 0 duplicate `Invoice ID`. The only required preparation is data type standardization, especially `Date` from string `M/D/YYYY` to Date and `Time` from string `HH:MM` to either Time/Datetime or calculated `Hour = INT(LEFT([Time], 2))`.

---

## DATA SPECIFICATION

### 17 Fields

| # | Field | Current Type | Target Type | Role | Notes |
|---|-------|--------------|-------------|------|-------|
| 1 | Invoice ID | String | String | dimension | Unique transaction ID |
| 2 | Branch | String | String | dimension | A/B/C |
| 3 | City | String | String | dimension | Yangon/Mandalay/Naypyitaw |
| 4 | Customer type | String | String | dimension | Member/Normal |
| 5 | Gender | String | String | dimension | Male/Female |
| 6 | Product line | String | String | dimension | 6 categories |
| 7 | Unit price | Number | Number | measure | USD |
| 8 | Quantity | Number | Number | measure | 1-10 units |
| 9 | Tax 5% | Number | Number | measure | 5% tax |
| 10 | Total | Number | Number | measure | After tax total |
| 11 | Date | String (M/D/YYYY) | Date | dimension | Parse in Tableau |
| 12 | Time | String (HH:MM) | Datetime | dimension | Extract Hour |
| 13 | Payment | String | String | dimension | Cash/Ewallet/Credit card |
| 14 | cogs | Number | Number | measure | Cost of goods sold |
| 15 | gross margin % | Number | Number | measure | Fixed 4.76% |
| 16 | gross income | Number | Number | measure | Profit |
| 17 | Rating | Number | Number | measure | 1-10 scale |

### Required Calculated Fields (7 total)

| # | Name | Formula | Type |
|---|------|---------|------|
| 1 | Hour | `INT(LEFT([Time], 2))` | Number |
| 2 | Day of Week | `DATENAME('weekday', [Date])` | String |
| 3 | Month | `DATENAME('month', [Date])` | String |
| 4 | Revenue per Unit | `[Total] / [Quantity]` | Number |
| 5 | Rating Category | `IF [Rating] >= 9 THEN "High" ELSEIF [Rating] >= 7 THEN "Medium" ELSE "Low" END` | String |
| 6 | Transaction Size | `IF [Quantity] >= 7 THEN "Large" ELSEIF [Quantity] >= 4 THEN "Medium" ELSE "Small" END` | String |
| 7 | Week Number | `DATEPART('week', [Date])` | Number |

---

## STAGES 1-6 SPECIFICATIONS

### Stage 1: Pemahaman Masalah dan Konteks
**Output:** Laporan Tahap 1 (2-3 pages)

**Required content:**
- Domain & konteks: supermarket fiktif 3 cabang
- 4 Stakeholder: Manajer Regional, Manajer Cabang, Tim Marketing, Tim Keuangan
- Pertanyaan bisnis utama + 5 sub-pertanyaan
- 5V Big Data analysis (Volume, Velocity, Variety, Veracity, Value)
- Data lifecycle diagram (Sumber -> Pengumpulan -> Penyimpanan -> Analisis -> Presentasi)

### Stage 2: Profiling dan Persiapan Data
**Output:** Laporan Tahap 2 (2 pages)

**Required content:**
- Kondisi dasar: 1000 baris, 17 kolom, rentang waktu, total revenue $322,966.75
- Deskripsi 17 field dengan makna bisnis
- Pengecekan tipe data (Date & Time perlu konversi)
- Standardisasi: Date parse, Time extract Hour
- Persiapan Tableau

### Stage 3: Pembersihan Data
**Output:** Laporan Tahap 3 + 4 SCREENSHOTS

**Mandatory checks (document even if clean):**
| Check | Expected Result | Screenshot |
|-------|----------------|------------|
| Missing Values | 0 null (1000/1000 all fields) | Gambar 3.1 |
| Duplicates | COUNT=1000, COUNTD=1000 | Gambar 3.2 |
| Format Consistency | All categorical consistent | Gambar 3.3 |
| Outliers | Box Plot Total per City - none | Gambar 3.4 |

**Key:** Even if data is clean, MUST document verification process with screenshots

### Stage 4: Analisis Eksploratif dan Mendalam
**Output:** Laporan Tahap 4 (5-6 pages) + 8+ screenshots

**Required Visualizations:**

| # | Visualization | Key Insight |
|---|---------------|-------------|
| 1 | Revenue Trend (Line Chart) | Naypyitaw highest revenue despite fewer transactions |
| 2 | Product Performance (Bar) | F&B highest $56K, distribution fairly even |
| 3 | Rating Analysis (Bar) | F&B highest rating 7.11 |
| 4 | Hourly Activity (Bar) | Peak 19:00 = 113 transactions |
| 5 | City Comparison (Side-by-side) | Naypyitaw AOV $337 vs Yangon $312 |
| 6 | Customer Analysis (Stacked Bar) | Member +3% AOV but slightly lower rating |
| 7 | Rating Distribution (Histogram) | Majority 6-7 range |
| 8 | Heatmap Product x City | Naypyitaw -> F&B, Yangon -> Home & Lifestyle |

**Pre-computed Key Metrics (for verification):**
- Naypyitaw: $110,568 revenue, AOV $337.10, rating 7.07
- Yangon: $106,200 revenue, AOV $312.35, rating 7.03
- Mandalay: $106,198 revenue, AOV $319.87, rating 6.82
- Member: 501 tx, $164,223 total, AOV $327.79, rating 6.94
- Normal: 499 tx, $158,743 total, AOV $318.12, rating 7.01
- Peak hour: 19:00 (113 tx, $39,699)
- F&B: $56,144 (17.38%), rating 7.11

### Stage 5: Dashboard Interaktif
**Output:** Laporan Tahap 5 + dashboard screenshot

**Components:**
- **6 Sheets** in 1 dashboard
- **2 Quick Filters:** City (dropdown), Product line (dropdown)
- **1 Filter Action:** Click City in Revenue Trend -> filter all sheets
- **1 Parameter:** Top N Products (integer 1-6)

**Sheet Layout:**
| Sheet | Chart Type | Key Fields |
|-------|------------|------------|
| Revenue Trend | Line | Date(Day), SUM(Total), City(Color) |
| Product Performance | Bar (Stacked) | Product line, SUM(Total), City(Color) |
| Customer Analysis | Stacked Bar | Customer type, SUM(Total), Product line(Color) |
| Hourly Activity | Bar | Hour, COUNT(Invoice ID), City(Color) |
| City Comparison | Side-by-side Bar | City, SUM(Total)/AVG(Rating)/SUM(Qty) |
| Rating Distribution | Histogram | Rating(bins=1), COUNT |

**Dashboard Size:** 1200 x 900 fixed
**Color Palette:** Naypyitaw=Green, Yangon=Blue, Mandalay=Orange

### Stage 6: Sintesis Insight & Rekomendasi
**Output:** Laporan Tahap 6 (2-3 pages)

**Required:**
- Answer main business question with specific numbers
- 3 concrete recommendations backed by data
- Limitations analysis
- Future research questions

**Key Findings to Include:**
1. Naypyitaw highest revenue (AOV $337) despite fewer transactions
2. Peak hour 19:00 = 12.3% daily revenue
3. F&B top category (17.38%, rating 7.11)
4. Member +3% AOV but slightly lower satisfaction
4. No correlation between Total and Rating (R-squared approximately 0)
5. Cash & Ewallet dominant (~34.5% each)

**3 Recommendations (Priority):**
1. P1: Optimasi jam operasional - tambah staf 18:30-20:00, Happy Hour promo 17:00-18:00
2. P1: Tingkatkan program Member - tiered membership, referral, target 60% Member
3. P2: Strategi produk per cabang - Naypyitaw -> F&B, Yangon -> Home & Lifestyle
4. P2: Investigasi rating Mandalay (6.82 terendah)
5. P3: Promosi Credit Card (diskon 2%)

---

## OUTPUT REQUIREMENTS

### 1. Tableau Packaged Workbook (.twbx)
- Location: `luaran/Supermarket_Sales_Dashboard.twbx`
- Contains: All 6 sheets + dashboard + data source
- Must open in Tableau Desktop without external dependencies

### 2. Written Report (.docx)
- Max 20 pages excluding appendix
- Structure: Cover -> Bab 1-6 -> Daftar Pustaka -> Lampiran
- 13 screenshots embedded at correct locations

### 3. Presentation Slides (.pptx)
- Max 15 slides
- Structure: Cover -> Background -> Dataset -> Business Q -> Process -> Cleaning -> 3 Findings -> CF -> Dashboard Demo -> Recommendations -> Conclusion -> Q&A
- Presenter notes per slide

---

## EXECUTION COMMANDS

```bash
# Recommended: run the complete local pipeline
cd /path/to/this/repository
python3 run_all.py

# Manual alternative if step-by-step execution is needed:

# 1. Validate data (verify AI recalculates correctly)
python3 scripts/validate_data.py
python3 scripts/validation_verify.py

# 2. Generate .twb XML
python3 twb_generator.py

# 3. Generate report
python3 report_generator.py

# 4. Generate slides
python3 slides_generator.py

# 5. Manual: Open .twb in Tableau, verify, export .twbx
```

---

## SUCCESS CRITERIA

- [ ] All 6 stages documented in report
- [ ] 4 cleaning screenshots captured
- [ ] 8+ analysis screenshots captured
- [ ] Dashboard screenshot captured
- [ ] .twbx file generated and opens correctly
- [ ] Report <= 20 pages, Slides <= 15
- [ ] All calculations match validation script output
- [ ] All 7 calculated fields created in Tableau
- [ ] 2 Quick Filters, 1 Filter Action, 1 Parameter working
