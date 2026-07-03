---
marp: true
theme: gaia
class: lead
paginate: true
---

<!-- _class: lead -->

# **Analisis Data Penjualan Supermarket Menggunakan Tableau**
### Laporan UAS Big Data Science

**Disusun oleh:**
Mu'adz Hudzaifah (24903460014) · Alhaq Sabilil Izati (24903460012) · Arfan Ghifari (24903460016)

**Dosen Pengampu:** Nur Choiriyati, S.Kom., M.T.
Politeknik Digital Boash Indonesia — TA 2026/2027

---

<!-- _class: default -->

## **Latar Belakang**

- Era Big Data: supermarket menghasilkan ribuan transaksi POS setiap hari — data ini aset strategis
- Data transaksi mencakup: produk, harga, pembayaran, kepuasan pelanggan
- **Masalah:** Data jarang dianalisis secara sistematis untuk pengambilan keputusan
- **Solusi:** Gunakan **Tableau** untuk visualisasi & dashboard interaktif — tanpa coding!
- Pendekatan **Big Data 5V**: Volume, Velocity, Variety, Veracity, Value
- Dataset: **Supermarket Sales (Kaggle)** — 1.000 transaksi, 3 cabang, 6 produk

---

## **Dataset Overview**

| Metrik | Nilai |
|--------|-------|
| **Sumber** | Kaggle — Aung Pyae Ap |
| **Jumlah Transaksi** | 1.000 baris, 17 kolom |
| **Periode** | Januari — Maret 2019 (89 hari) |
| **Cabang** | 3 (Yangon, Mandalay, Naypyitaw) |
| **Total Revenue** | **$322,966.75** |
| **Rata-rata Rating** | **6.97 / 10** |
| **Pelanggan Member** | 50.1% |

---

## **Pertanyaan Bisnis**

**Utama:** Faktor apa yang paling mempengaruhi total penjualan dan kepuasan pelanggan?

**Sub-Pertanyaan:**

1. **Tren Penjualan** — Bagaimana pola harian/mingguan penjualan per cabang?
2. **Performa Produk** — Kategori apa paling berkontribusi? Ada preferensi per cabang?
3. **Analisis Pelanggan** — Seberapa efektif program Member vs Normal?
4. **Analisis Korelasi** — Apakah rating berkorelasi dengan nominal transaksi?
5. **Demografi** — Metode bayar apa yang dominan tiap segmen?

---

## **Metodologi — 6 Tahap Analisis**

```
┌─────────────┐
│ Pemahaman   │  Identifikasi stakeholder & pertanyaan bisnis
│ Masalah     │
└──────┬──────┘
       ↓
┌─────────────┐
│ Profiling   │  Analisis struktur data, tipe data, 5V Big Data
│ Data        │
└──────┬──────┘
       ↓
┌─────────────┐
│ Pembersihan │  Missing values, duplikasi, outlier, standarisasi tipe
│ Data        │
└──────┬──────┘
       ↓
┌─────────────┐
│ EDA         │  Visualisasi distribusi, tren, korelasi, segmentasi
│ (Tableau)   │
└──────┬──────┘
       ↓
┌─────────────┐
│ Dashboard   │  6 sheet → 1 dashboard interaktif + filter actions
│ Interaktif  │
└──────┬──────┘
       ↓
┌─────────────┐
│ Sintesis &  │  Kesimpulan & rekomendasi strategis
│ Rekomendasi │
└─────────────┘
```

---

## **Data Profiling — Analisis 5V**

| V | Konsep | Realisasi Dataset |
|---|--------|-------------------|
| **Volume** | Jumlah data besar | 1.000 baris × 17 kolom — representatif untuk ritel skala menengah |
| **Velocity** | Kecepatan data masuk | Timestamp per transaksi, rentang jam 10:00–20:59 |
| **Variety** | Keragaman tipe data | Numerik, kategorikal, temporal, tekstual |
| **Veracity** | Kualitas data | 0 missing values, 0 duplikasi, sintetis → konsisten tinggi |
| **Value** | Nilai bisnis | Rekomendasi strategis: stok, member, pricing, kepuasan |

---

## **Data Cleaning — Bersih Sempurna!**

![width:700px](assets/Data-Quality.jpg)

| Aspek | Status | Detail |
|-------|--------|--------|
| **Missing Values** | ✅ Bersih | 0 null dari 17 kolom, 1.000 baris lengkap |
| **Duplikasi** | ✅ Bersih | COUNT = COUNTD = 1.000 — tidak ada duplikat |
| **Inkonsistensi Format** | ✅ Bersih | Semua kategorikal konsisten |
| **Outlier** | ✅ Bersih | Tidak ada outlier ekstrem (Box Plot valid) |
| **Konversi Date** | ✅ Selesai | String → Date (M/D/YYYY) |
| **Konversi Time** | ✅ Selesai | String → Time → Hour extracted |

---

## **Outlier Analysis — Box Plot**

![width:700px](assets/Box-Plot-Total.jpg)

**Box Plot Total per City:**
- Nilai Total: **$10.68 – $1,042.65**
- Tidak ada outlier signifikan per cabang
- Sebaran data sehat, tidak ada data perlu dibuang

![width:700px](assets/Box-Plot-Rating.jpg)

**Box Plot Rating per Product Line:**
- Rating 4.0–10.0, tidak ada outlier ekstrem
- Sebaran normal, data valid untuk analisis

---

## **Calculated Fields (7 Field)**

| No | Nama Field | Formula | Kegunaan |
|:--:|------------|---------|----------|
| 1 | **Hour** | `INT(LEFT([Time], 2))` | Ekstrak jam untuk peak hours |
| 2 | **Day of Week** | `DATENAME('weekday', [Date])` | Pola mingguan |
| 3 | **Revenue per Unit** | `[Total] / [Quantity]` | Harga rata-rata per unit |
| 4 | **Rating Category** | `IF [Rating] >= 9 THEN "High"...` | Kategorisasi rating |
| 5 | **Transaction Size** | `IF [Quantity] >= 7 THEN "Large"...` | Ukuran transaksi |
| 6 | **Month** | `DATENAME('month', [Date])` | Analisis bulanan |
| 7 | **Week Number** | `DATEPART('week', [Date])` | Tren mingguan |

---

## **Temuan 1: Tren Penjualan**

![width:700px](assets/Revenue-Trend.jpg)

| Kota | Transaksi | Total Revenue | Avg Transaction |
|------|:---------:|:------------:|:---------------:|
| **Naypyitaw** | 328 | **$110,568.71** 🏆 | **$337.10** 🏆 |
| Yangon | 340 | $106,200.37 | $312.35 |
| Mandalay | 332 | $106,197.67 | $319.87 |

**Key Insight:** Naypyitaw unggul meski transaksi paling sedikit — AOV tertinggi!

---

## **Temuan 1b: Jam Sibuk (Peak Hour)**

![width:700px](assets/Hourly-Activity.jpg)

| Jam | Transaksi | Total Revenue | Insight |
|:---:|:---------:|:-------------:|---------|
| **19:00** 🏆 | **113** | **$39,699.51** | **Golden hour — puncak aktivitas!** |
| 13:00 | 103 | $34,723.23 | Lonjakan siang hari |
| 15:00 | 102 | $31,179.51 | Stabil tinggi |
| 20:00 | 75 | $22,969.53 | Menjelang tutup |

**Rekomendasi:** Tambah staf kasir di **18:30–20:00**, Happy Hour promo jam 17:00–18:00

---

## **Temuan 2: Performa Produk**

![width:700px](assets/Product-Performance.jpg)

| Product Line | Revenue | % Kontribusi | Avg Rating |
|-------------|:------:|:-----------:|:---------:|
| **Food & Beverages** 🏆 | **$56,145** | **17.38%** | **7.11** 🏆 |
| Sports & Travel | $55,123 | 17.07% | 6.92 |
| Electronic Accessories | $54,338 | 16.82% | 6.92 |
| Fashion Accessories | $54,306 | 16.81% | 7.03 |
| Home & Lifestyle | $53,862 | 16.68% | 6.84 |
| Health & Beauty | $49,194 | 15.23% | 7.00 |

**Insight:** Distribusi merata (15–17%) — diversifikasi produk berjalan baik

---

## **Temuan 2b: Preferensi Produk per Cabang**

![width:700px](assets/City-Comparison.jpg)

| Produk | Mandalay | Naypyitaw | Yangon |
|--------|:-------:|:---------:|:-----:|
| Electronic accessories | $17,051 | $18,969 | $18,317 |
| Fashion accessories | $16,413 | **$21,560** | $16,333 |
| Food & Beverages | $15,215 | **$23,767** | $17,163 |
| Health & Beauty | $19,981 | $16,615 | $12,598 |
| Home & Lifestyle | $17,549 | $13,896 | **$22,417** |
| Sports & Travel | $19,988 | $15,762 | $19,373 |

**Tiap cabang punya karakteristik unik!** → Strategi produk per cabang

---

## **Temuan 3: Analisis Pelanggan**

![width:700px](assets/Customer-Analysis.jpg)

| Metrik | Member | Normal | Selisih |
|--------|:-----:|:------:|:-------:|
| **Jumlah Transaksi** | 501 | 499 | +2 |
| **Total Revenue** | $164,223 | $158,743 | **+$5,480** |
| **Avg Spend** | **$327.79** 🏆 | $318.12 | **+$9.67 (+3%)** |
| **Avg Rating** | 6.94 | 7.01 | -0.07 |

**Insight:** Member spend lebih tinggi, rating sedikit lebih rendah (ekspektasi tinggi)

---

## **Temuan 3b: Metode Pembayaran**

![width:700px](assets/Payment-Analysis.jpg)

| Metode | Transaksi | Total Revenue | Avg Rating |
|--------|:----------:|:------------:|:---------:|
| **Cash** | 344 (34.4%) | **$112,207** | 6.97 |
| **Ewallet** | 345 (34.5%) | $109,993 | 6.95 |
| **Credit Card** | 311 (31.1%) | $100,767 | **7.00** 🏆 |

**Insight:** Cash & Ewallet dominan. Credit card paling sedikit tapi rating tertinggi!

---

## **Temuan 4: Korelasi — Tidak Ada!**

**Scatter Plot: Total vs Rating**
- Trend line hampir **datar**
- **Tidak ada korelasi** antara nilai transaksi dengan rating
- Pelanggan $10 bisa rating 10, pelanggan $1,000 bisa rating 5
- Jumlah item (Quantity) juga **tidak berkorelasi** dengan rating

```
Rating
10 │  ·  ··   · ··  ·· ·  · ·  ··· ··   ·
 9 │  ·  ··   · ···· ··· · · · ···· ···  ·
 8 │  ·· ···  ··························  ·
 7 │  ·· ···  ··························  ·
 6 │  ·· ···  ··························  ·
 5 │  ·  ··   · ···· ··· · · · ···· ···  ·
 4 │  ·  ··   · ··  ·· ·  · ·  ··· ··   ·
   └─────────────────────────────────────
    $10                        $1,042  Total
```

**⚠️ Kepuasan TIDAK tergantung nominal belanja — fokus pada KUALITAS LAYANAN!**

---

## **Dashboard Interaktif — Tableau**

```
┌──────────────────────────────────────────────────┐
│  SUPERMARKET SALES DASHBOARD — Jan-Mar 2019       │
├──────────────────┬───────────────────────────────┤
│  REVENUE TREND   │  PRODUCT PERFORMANCE           │
│  (Line Chart)    │  (Bar Chart)                  │
├──────────────────┼───────────────────────────────┤
│  CUSTOMER        │  HOURLY ACTIVITY               │
│  ANALYSIS (Bar)  │  (Bar Chart)                  │
├──────────────────┼───────────────────────────────┤
│  CITY COMPARISON │  RATING DISTRIBUTION           │
│  (Side-by-side)  │  (Histogram)                  │
└──────────────────┴───────────────────────────────┘
```

**10 Worksheets dalam .twbx:**
Revenue Trend · Product Performance · Customer Analysis · Hourly Activity
City Comparison · Rating Distribution · Payment Analysis · Data Quality
Box Plot Total · Box Plot Rating

---

## **Fitur Interaktif Dashboard**

### Quick Filters:
- ✅ **City** — Pilih satu atau semua cabang
- ✅ **Product Line** — Fokus kategori produk
- ✅ **Customer Type** — Member / Normal

### Filter Action:
- 🔗 Klik cabang di Revenue Trend → semua sheet terfilter otomatis

### Parameter:
- 🎚️ **Top N Products** — Slider (1–6) untuk menampilkan produk teratas

### Export:
- 📦 Format **.twbx** — data + visualisasi dalam 1 file portabel

---

## **Rekomendasi Strategis**

| # | Rekomendasi | Dampak | Usaha | Prioritas |
|:-:|------------|:------:|:-----:|:---------:|
| 1 | **Optimasi jam operasional** — Tambah staf 18:30–20:00, Happy Hour promo 17:00–18:00 | 🟢 Tinggi | 🔵 Rendah | **P1** |
| 2 | **Tingkatkan program member** — Tiered membership, referral program, target 60% member | 🟢 Tinggi | 🟡 Sedang | **P1** |
| 3 | **Strategi produk per cabang** — Naypyitaw: F&B, Yangon: Home & Lifestyle, Mandalay: Health & Beauty | 🟡 Sedang | 🟡 Sedang | **P2** |
| 4 | **Investigasi rating Mandalay** (6.82) — Survei kepuasan, evaluasi layanan | 🟡 Sedang | 🔵 Rendah | **P2** |
| 5 | **Promosi Credit Card** — Diskon 2%, kerja sama bank untuk cicilan 0% | 🔵 Rendah | 🔵 Rendah | **P3** |

---

## **Kesimpulan (6 Poin Utama)**

| # | Kesimpulan | Detail |
|:-:|-----------|--------|
| 1️⃣ | **Naypyitaw juara revenue** | $110,568 — AOV $337 vs $312 (Yangon) |
| 2️⃣ | **Jam 19:00 golden hour** | 113 transaksi, $39,699.51 dalam 1 jam! |
| 3️⃣ | **F&B produk terbaik** | Revenue & rating tertinggi (7.11) |
| 4️⃣ | **Member +3% lebih tinggi** | $327.79 vs $318.12 per transaksi |
| 5️⃣ | **Kepuasan ≠ nominal** | Scatter plot acak — fokus pada kualitas! |
| 6️⃣ | **Dashboard siap pakai** | 6 sheet, 3 filter, 1 parameter, 1 file .twbx |

---

## **Keterbatasan & Saran**

### Keterbatasan:
- Data hanya **3 bulan** — belum bisa deteksi pola tahunan
- Dataset **sintetis** — perlu validasi data riil
- Tidak ada data **biaya operasional** → belum bisa hitung profitabilitas
- Rating **subjektif** — interpretasi tiap pelanggan berbeda

### Saran Pengembangan:
- ⏱️ Perluas data ke minimal **1 tahun**
- 📊 Tambah data biaya operasional untuk analisis profitabilitas
- 👥 Survei langsung untuk data kualitatif
- 🤖 Analisis **prediktif** — ML untuk prediksi tren
- 📈 Bandingkan dengan **periode tahun berikutnya**

---

## **Call to Action**

### **Repositori Laporan:**
🌐 [github.com/muadzhdz/RoadToUAS-BigDataScience](https://github.com/muadzhdz/RoadToUAS-BigDataScience)

### **Automated Report Generation:**
⚡ [github.com/muadzhdz/laporan-generator](https://github.com/muadzhdz/laporan-generator.git)
> Cetak laporan akademik dari Markdown ke PDF dengan 1 perintah!

### **Dashboard Tableau:**
📦 File `Supermarket_Sales_Dashboard.twbx` — Buka dengan Tableau Desktop

---

<!-- _class: lead -->

# **Terima Kasih**
### 🙏

**Any Questions?**

**Kontak:**
- Mu'adz Hudzaifah — 24903460014
- Alhaq Sabilil Izati — 24903460012
- Arfan Ghifari — 24903460016

---

### **Q&A Preparation**

| Pertanyaan | Jawaban |
|-----------|---------|
| Kenapa pilih dataset ini? | Bersih, lengkap, representatif untuk retail analytics |
| Apa keterbatasan analisis? | Data sintetis, hanya 3 bulan, tidak ada biaya operasional |
| Kenapa pake Tableau? | Fitur interaktif lengkap, drag-and-drop, easy to use |
| Temuan paling menarik? | Kepuasan **tidak berkorelasi** dengan nominal transaksi! |
| Dashboard bisa diakses di mana? | File .twbx — portabel, buka di Tableau Desktop mana pun |
