# Analisis Data Penjualan Supermarket — UAS Big Data Science

**Politeknik Digital Boash Indonesia** — [pdbi.ac.id](https://pdbi.ac.id)  
Program Studi Teknologi Rekayasa Multimedia

Analisis data transaksi penjualan supermarket menggunakan **Tableau Desktop** dan **Python** dengan pendekatan Big Data 5V. Dataset mencakup 1.000 transaksi dari 3 cabang (Yangon, Mandalay, Naypyitaw) selama periode Januari -- Maret 2019.

## Identitas Kelompok

| Nama | NIM |
|------|-----|
| Mu'adz Hudzaifah | 24903460014 |
| Alhaq Sabilil Izati | 24903460012 |
| Arfan Ghifari | 24903460016 |

**Dosen Pengampu:** Nur Choiriyati, S.Kom., M.T.

## Struktur Proyek

```
├── Proyek_BigData/
│   ├── Supermarket_Sales_Dashboard_final.twbx   ← Dashboard Tableau
│   └── assets/                                   ← Screenshot visualisasi
│       ├── Data-Source.jpg
│       ├── Data-Quality.jpg
│       ├── Box-Plot-Total.jpg
│       ├── Box-Plot-Rating.jpg
│       ├── Revenue-Trend.jpg
│       ├── Product-Performance.jpg
│       ├── Customer-Analysis.jpg
│       ├── Hourly-Activity.jpg
│       ├── City-Comparison.jpg
│       ├── Rating-Distribution.jpg
│       ├── Payment-Analysis.jpg
│       └── Dashboard.jpeg
├── auto-laporan/                                 ← Pipeline cetak laporan PDF
│   ├── Laporan_Akademik.md                       ← Naskah laporan
│   ├── cover.md                                  ← Halaman sampul + kata pengantar
│   ├── template.latex                            ← Template LaTeX
│   ├── logo-boash.jpg                            ← Logo institusi
│   └── build.sh                                  ← Satu perintah → PDF
├── dataset/
│   ├── supermarket_sales.csv                     ← Data transaksi
│   └── sumber_dataset.txt                        ← Metadata dataset
├── Scripts/
│   └── fix_twbx_extract.py                       ← Konversi .twbx ke extract Tableau Public
├── Laporan_UAS_BigData.pdf                       ← Laporan final PDF
└── README.md
```

## Dashboard

Dashboard interaktif mencakup 7 komponen visualisasi: KPI (Total Revenue, Transactions, Products Sold, Customer Rating, Gross Income), Revenue Trend, Product Performance, Customer Analysis, Payment Analysis, Hourly Activity, dan City Comparison. Dilengkapi 6 quick filter (Day of Date, Product line, City, Payment, Hour, Customer type) serta fitur cross-filtering dan parameter (Top N Products).

## Laporan Akademik

Laporan dicetak secara otomatis dari Markdown ke PDF melalui pipeline Pandoc + LaTeX:

```bash
cd auto-laporan && ./build.sh
# Output: ../Laporan_UAS_BigData.pdf
```

## Sumber Data

Dataset: [Supermarket Sales Dataset](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales) — Kaggle, dikoleksi oleh Aung Pyae Ap.
