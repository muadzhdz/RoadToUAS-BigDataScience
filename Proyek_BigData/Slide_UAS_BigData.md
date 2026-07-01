# Slide Presentasi UAS Big Data Science
## Supermarket Sales Analysis

**Anggota Kelompok:** Mu'adz Hudzaifah (24903460014), Alhaq Sabilil Izati (24903460012), Arfan Ghifari (24903460016)
**Tools:** Tableau Desktop

---

Catatan: file ini adalah draft konten presentasi maksimal 15 slide. Masukkan screenshot dashboard final dan rapikan visual di PowerPoint/Canva.

---
﻿# [SLIDES] KONTEN PRESENTASI SIAP PAKAI — 15 SLIDE
## Supermarket Sales Analysis — Big Data Science

---

> **CARA PAKAI:**
> - Kolom **Slide** = desain visual
> - Kolom **Narasi** = apa yang lo omongin (hafalin, jangan dibaca)
> - **Bold** = kata kunci yang harus lo tekankan
> - ⏱ = estimasi waktu per slide

---

## SLIDE 1 — COVER (⏱ 30 detik)

**Slide:**
```
┌─────────────────────────────────────────┐
│                                         │
│   [DATA] ANALISIS DATA PENJUALAN           │
│     SUPERMARKET MENGGUNAKAN TABLEAU     │
│                                         │
│   BIG DATA SCIENCE — UAS               │
│                                         │
│   Mu'adz Hudzaifah — [NIM]                     │
│   Alhaq Sabilil Izati — [NIM]                     │
│   Arfan Ghifari (24903460016) — [NIM]                     │
│                                         │
│   Dosen: [Nama Dosen]                  │
│   [Universitas]                        │
│   [Tahun Akademik]                     │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Assalamualaikum wr wb / Selamat pagi. Kami dari kelompok [X] akan mempresentasikan analisis data penjualan supermarket menggunakan Tableau. Dataset yang kami gunakan adalah Supermarket Sales dari Kaggle."

---

## SLIDE 2 — LATAR BELAKANG (⏱ 1 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  LATAR BELAKANG                         │
├─────────────────────────────────────────┤
│                                         │
│  [DASHBOARD] Big Data di Industri Ritel         │
│     - Ribuan transaksi per hari         │
│     - Data = aset strategis             │
│                                         │
│  [LIST] Tujuan Analisis:                   │
│     Identifikasi faktor penjualan       │
│     & kepuasan pelanggan               │
│                                         │
│  [TOOLS] Tools: Tableau Desktop             │
│                                         │
│  [CUSTOMER] Stakeholder:                       │
│     Manajer Regional, Cabang,          │
│     Tim Marketing, Tim Keuangan        │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Di era Big Data, supermarket menghasilkan ribuan transaksi setiap hari. Sayangnya, data ini sering hanya menjadi arsip. Padahal, data tersebut bisa memberikan insight berharga — seperti produk apa yang paling laris, jam berapa toko paling ramai, dan bagaimana kepuasan pelanggan. Analisis ini bertujuan mengidentifikasi faktor-faktor yang mempengaruhi penjualan dan kepuasan pelanggan menggunakan Tableau."

---

## SLIDE 3 — DATASET OVERVIEW (⏱ 1 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  DATASET SUPERMARKET SALES              │
├─────────────────────────────────────────┤
│                                         │
│  [OUTPUT] Sumber: Kaggle                     │
│  [DATA] 1.000 transaksi | 17 kolom        │
│                                         │
│  ┌──────────────┬─────────────┐        │
│  │ Metrik       │ Nilai       │        │
│  ├──────────────┼─────────────┤        │
│  │ Periode      │ Jan-Mar 2019│        │
│  │ Revenue      │ $322,966    │        │
│  │ Cabang       │ 3 (A/B/C)   │        │
│  │ Produk       │ 6 kategori  │        │
│  │ Pelanggan    │ 50% Member  │        │
│  │ Avg Rating   │ 6.97/10     │        │
│  └──────────────┴─────────────┘        │
│                                         │
│  [Ikon: 3 kota, 6 produk, 3 payment]   │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Dataset ini berasal dari Kaggle — mencatat 1.000 transaksi dari 3 cabang supermarket di Yangon, Mandalay, dan Naypyitaw selama Januari hingga Maret 2019. Total revenue mencapai hampir $323.000 dengan rata-rata rating 6.97 dari 10. Dataset mencakup 6 kategori produk dan 3 metode pembayaran. Komposisi pelanggan hampir seimbang — 50% member dan 50% normal."

---

## SLIDE 4 — PERTANYAAN BISNIS (⏱ 1 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  PERTANYAAN BISNIS                      │
├─────────────────────────────────────────┤
│                                         │
│  [QUESTION] UTAMA:                              │
│  Faktor apa yang mempengaruhi          │
│  penjualan & kepuasan pelanggan?       │
│                                         │
│  [POINT] SUB-PERTANYAAN:                    │
│  1. Tren penjualan harian?             │
│  2. Produk paling berkontribusi?       │
│  3. Member vs Normal?                  │
│  4. Korelasi rating dengan transaksi?  │
│  5. Preferensi metode bayar?           │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Pertanyaan utama analisis kami adalah: faktor apa yang paling mempengaruhi penjualan dan kepuasan pelanggan? Kami menjabarkannya ke dalam 5 sub-pertanyaan: (1) bagaimana tren penjualan harian? (2) produk apa yang paling berkontribusi? (3) apa bedanya member dan normal? (4) apakah rating berkorelasi dengan nominal transaksi? (5) bagaimana preferensi metode bayar?"

---

## SLIDE 5 — TAHAPAN ANALISIS (⏱ 30 detik)

**Slide:**
```
┌─────────────────────────────────────────┐
│  TAHAPAN ANALISIS                       │
├─────────────────────────────────────────┤
│                                         │
│  [SOURCE] Kaggle — Sumber Data               │
│         ↓                              │
│  [CHECK] Profiling & Persiapan             │
│         ↓                              │
│  [CLEAN] Pembersihan Data (0 missing!)     │
│         ↓                              │
│  [DATA] Analisis Eksploratif              │
│         ↓                              │
│  [DASHBOARD] Dashboard Interaktif (Tableau)    │
│         ↓                              │
│  [NOTES] Sintesis & Rekomendasi            │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Analisis kami melalui 6 tahap: mulai dari pengumpulan data dari Kaggle, dilanjutkan profiling dan persiapan, pembersihan data, analisis eksploratif di Tableau, pembuatan dashboard interaktif, dan terakhir sintesis rekomendasi."

---

## SLIDE 6 — PEMBERSIHAN DATA (⏱ 1 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  PEMBERSIHAN DATA                       │
├─────────────────────────────────────────┤
│                                         │
│  [OK] Missing Values: 0 (dari 17 kolom)  │
│  [OK] Duplikasi: 0 (COUNT=COUNTD=1000)   │
│  [OK] Inkonsistensi: 0 (format konsisten)│
│  [OK] Outlier: Tidak ada ekstrem         │
│                                         │
│  [PROCESS] Konversi:                          │
│     Date: String → Date               │
│     Time: String → Hour (CF)          │
│                                         │
│  [INFO] Dataset SUPER BERSIH               │
│     (tidak perlu cleaning besar)       │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Untungnya, dataset ini sangat bersih. Kami tidak menemukan missing values, duplikasi, atau inkonsistensi format. Satu-satunya perubahan yang kami lakukan adalah mengkonversi Date dari string ke date, dan mengekstrak jam dari kolom Time. Ini menunjukkan bahwa dataset sudah siap analisis tanpa perlu pembersihan besar-besaran."

**[TIP] TIP:** Tunjukin screenshot Box Plot di slide ini biar lebih meyakinkan.

---

## SLIDE 7 — TEMUAN: TREN PENJUALAN (⏱ 1.5 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  TEMUAN 1: TREN PENJUALAN               │
├─────────────────────────────────────────┤
│                                         │
│  [LINE CHART: 3 garis warna]           │
│                                         │
│  [TOP] NAYPYITAW: $110,568 (REVENUE       │
│     TERTINGGI! meski 328 transaksi)    │
│                                         │
│  [2] Yangon: $106,200 (340 transaksi)   │
│  [3] Mandalay: $106,197 (332 transaksi) │
│                                         │
│  ⭐ AOV Naypyitaw: $337 vs $312        │
│     (8% lebih tinggi dari Yangon!)     │
│                                         │
│  [TIME] PEAK HOUR: 19:00 (113 transaksi)   │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Temuan pertama dan paling menarik: **Naypyitaw** mencatat revenue tertinggi — $110.568 — meskipun jumlah transaksinya paling sedikit! Ini karena Average Order Value di Naypyitaw mencapai **$337**, sementara Yangon hanya $312. Artinya, pelanggan Naypyitaw belanja lebih banyak setiap kali berkunjung. Kami juga menemukan bahwa **jam 19:00** adalah golden hour — 113 transaksi dengan revenue hampir $40.000 dalam satu jam saja."

**[TIP] TIP:** Tunjuk chart dan arahin ke garis Naypyitaw.

---

## SLIDE 8 — TEMUAN: PRODUK (⏱ 1.5 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  TEMUAN 2: ANALISIS PRODUK              │
├─────────────────────────────────────────┤
│                                         │
│  [BAR CHART: Revenue per Product Line]  │
│                                         │
│  [1] Food & Beverages: $56,144 (17.4%)  │
│  [2] Sports & Travel: $55,122 (17.1%)   │
│  [3] Electronic Acc: $54,337 (16.8%)    │
│                                         │
│  ⭐ RATING TERTINGGI:                  │
│     F&B = 7.11 [TOP]                      │
│     Home & Lifestyle = 6.84 (terendah) │
│                                         │
│  [HEATMAP: Produk per Cabang]          │
│  Naypyitaw → F&B ($23,767!)            │
│  Yangon → Home & Lifestyle ($22,417)   │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Untuk analisis produk, Food & Beverages menjadi juara di dua kategori sekaligus: revenue tertinggi dan rating tertinggi. Ini adalah produk unggulan. Yang menarik, distribusi revenue antar 5 kategori teratas hampir identik — semuanya di kisaran $54.000. Artinya diversifikasi produk berjalan baik. Tapi yang paling menarik adalah **heatmap produk per cabang**: Naypyitaw sangat kuat di F&B, sementara Yangon unggul di Home & Lifestyle. Setiap cabang punya karakteristik berbeda!"

**[TIP] TIP:** Tunjuk heatmap dan kasih contoh spesifik.

---

## SLIDE 9 — TEMUAN: PELANGGAN (⏱ 1 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  TEMUAN 3: ANALISIS PELANGGAN           │
├─────────────────────────────────────────┤
│                                         │
│  [BAR CHART: Member vs Normal]         │
│                                         │
│  [CUSTOMER] MEMBER: $327.79 per transaksi      │
│     (+3% dari Normal = $318.12)        │
│                                         │
│  [PAYMENT] PREFERENSI PEMBAYARAN:             │
│  Cash   34.4% │ Ewallet 34.5%          │
│  Credit Card 31.1% │ Rating 7.00 [TOP]   │
│                                         │
│  [WARNING] Rating Member: 6.94               │
│     Rating Normal: 7.01                │
│     (Member puas? perlu diimprove!)    │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Member menghabiskan **$9.67 lebih banyak** per transaksi dibanding pelanggan normal — atau sekitar 3% lebih tinggi. Ini menunjukkan program member sudah cukup efektif. Tapi yang menarik, rating member justru **sedikit lebih rendah** dibanding normal. Kemungkinan karena ekspektasi mereka lebih tinggi. Untuk metode bayar, Cash dan Ewallet mendominasi ~34.5% masing-masing, sementara Credit card masih yang paling jarang digunakan."

---

## SLIDE 10 — TEMUAN: KORELASI (⏱ 1 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  TEMUAN 4: ANALISIS KORELASI            │
├─────────────────────────────────────────┤
│                                         │
│  [SCATTER PLOT: Total vs Rating]       │
│  Trend line hampir datar!              │
│                                         │
│  [NO] TIDAK ADA KORELASI                  │
│  antara Total transaksi & Rating       │
│  antara Quantity & Rating              │
│                                         │
│  [INFO] ARTINYA:                           │
│  Kepuasan TIDAK tergantung             │
│  nominal belanja!                      │
│  Kualitas layanan & produk             │
│  lebih penting!                        │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Ini temuan yang paling penting secara strategis: **tidak ada korelasi** antara nilai transaksi dengan kepuasan pelanggan. Lihat scatter plot ini — penyebarannya acak. Pelanggan yang belanja $10 bisa kasih rating 10, dan yang belanja $1.000 bisa kasih rating 5. **Kesimpulannya**: kepuasan pelanggan tidak ditentukan oleh seberapa banyak mereka belanja. Faktor yang lebih penting adalah kualitas layanan dan kualitas produk."

**[TIP] TIP:** Ini slide paling penting! Tekankan dengan suara lo.

---

## SLIDE 11 — CALCULATED FIELDS (⏱ 30 detik)

**Slide:**
```
┌─────────────────────────────────────────┐
│  CALCULATED FIELDS                      │
├─────────────────────────────────────────┤
│                                         │
│  [Screenshot panel Data Tableau]       │
│                                         │
│  1. Hour = INT(LEFT([Time], 2))        │
│  2. Day of Week = DATENAME(...)        │
│  3. Revenue per Unit = Total/Quantity  │
│  4. Rating Category = IF Rating...     │
│  5. Transaction Size = IF Quantity...  │
│  6. Month = DATENAME('month', [Date])  │
│  7. Week Number = DATEPART('week'...)  │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Kami membuat 7 Calculated Fields di Tableau. Yang paling krusial adalah **Hour**, yang mengekstrak jam dari string Time, sehingga kami bisa menganalisis peak hour. Ada juga **Rating Category** untuk mengelompokkan rating menjadi High, Medium, dan Low, serta **Transaction Size** untuk mengkategorikan besar kecilnya transaksi."

---

## SLIDE 12 — DASHBOARD DEMO (⏱ 2 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  DASHBOARD INTERAKTIF — TABLEAU         │
├─────────────────────────────────────────┤
│                                         │
│  [FULL DASHBOARD SCREENSHOT]           │
│                                         │
│  FITUR INTERAKTIF:                     │
│  [TARGET] Quick Filter: City, Product       │
│  [LINK] Filter Action: Klik → Filter      │
│  [SETTING] Parameter: Top N Products         │
│                                         │
│  6 SHEET DALAM 1 DASHBOARD:            │
│  Revenue Trend | Product Performance   │
│  Customer Analysis | Hourly Activity   │
│  City Comparison | Rating Dist.        │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Ini dashboard final kami. Terdiri dari 6 sheet visualisasi dalam satu layout. Ada 3 fitur interaktif utama: **Quick Filter** untuk memilih cabang atau produk, **Filter Action** — klik cabang di chart Revenue Trend dan semua sheet akan terfilter otomatis, dan **Parameter Top N Products** untuk mengatur jumlah produk teratas yang ditampilkan. Dashboard ini bisa digunakan oleh manajer untuk monitoring secara real-time."

**[TIP] TIP:** Kalau bisa, **demo live** di Tableau. Buka file .twbx dan tunjukkin filter action. Ini yang paling impressive buat dosen!

---

## SLIDE 13 — REKOMENDASI (⏱ 1.5 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  REKOMENDASI STRATEGIS                  │
├─────────────────────────────────────────┤
│                                         │
│  [P1] P1: OPTIMASI JAM OPERASIONAL       │
│  • Tambah staf 18:30-20:00             │
│  • Happy Hour promo jam 17:00-18:00    │
│                                         │
│  [P1] P1: TINGKATKAN PROGRAM MEMBER      │
│  • Tiered membership (Silver/Gold/...) │
│  • Referral program                    │
│  • Target: 60% member                  │
│                                         │
│  [POINT] P2: STRATEGI PRODUK PER CABANG     │
│  [POINT] P2: INVESTIGASI RATING MANDALAY    │
│  [POINT] P3: PROMOSI CREDIT CARD            │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Berdasarkan temuan kami, ada 5 rekomendasi. Prioritas utama: **Optimasi jam operasional** — tambah staf di jam 19:00 karena itu golden hour, dan buat promo Happy Hour di jam sepi untuk meratakan traffic. Prioritas kedua: **Tingkatkan program member** — buat tiered membership dan referral program, targetkan 60% member. Ada juga rekomendasi untuk strategi produk per cabang, investigasi rating Mandalay yang paling rendah, dan promosi credit card."

---

## SLIDE 14 — KESIMPULAN (⏱ 1 menit)

**Slide:**
```
┌─────────────────────────────────────────┐
│  KESIMPULAN                             │
├─────────────────────────────────────────┤
│                                         │
│  1️⃣ Naypyitaw juara revenue ($110K)    │
│  2️⃣ Jam 19:00 = golden hour           │
│  3️⃣ F&B = produk terbaik (revenue &    │
│     rating tertinggi)                   │
│  4️⃣ Member +3% lebih tinggi dari Normal│
│  5️⃣ Kepuasan ≠ nominal transaksi       │
│     (fokus pada kualitas layanan!)     │
│  6️⃣ Dashboard siap monitoring          │
│                                         │
│  [DATA] TOTAL REVENUE: $322,966.75         │
│  ⭐ AVG RATING: 6.97/10               │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Kesimpulan dari analisis kami: Naypyitaw adalah cabang dengan performa terbaik. Jam 19:00 adalah waktu paling strategis. Food & Beverages adalah produk unggulan. Program member sudah efektif tapi bisa dioptimasi. Yang paling penting: kepuasan pelanggan tidak terkait nominal belanja — jadi fokus pada kualitas layanan, bukan cuci gudang. Dashboard sudah siap digunakan untuk monitoring."

---

## SLIDE 15 — TERIMA KASIH (⏱ 30 detik)

**Slide:**
```
┌─────────────────────────────────────────┐
│                                         │
│         TERIMA KASIH                   │
│                                         │
│    Terima kasih Any Questions?                   │
│                                         │
│    Kontak:                             │
│    Mu'adz Hudzaifah — [NIM] — [IG/WA]         │
│    Alhaq Sabilil Izati — [NIM] — [IG/WA]         │
│    Arfan Ghifari (24903460016) — [NIM] — [IG/WA]         │
│                                         │
│    [FOLDER] Dashboard:                       │
│    [Link Tableau Public / QR Code]     │
│                                         │
│    "Data is the new oil"               │
│                                         │
└─────────────────────────────────────────┘
```

**Narasi:**
> "Terima kasih atas perhatiannya. Kami siap menerima pertanyaan. Untuk teman-teman yang ingin melihat dashboard secara langsung, bisa akses link QR code ini. Sekali lagi, terima kasih."

**[TIP] TIP:** Kalau ada sesi tanya jawab, siapin jawaban untuk pertanyaan-pertanyaan ini:
1. "Kenapa pilih dataset ini?" → Karena bersih, lengkap, cocok untuk retail analytics
2. "Apa keterbatasan analisis?" → Data sintetis, hanya 3 bulan, tidak ada biaya operasional
3. "Kenapa pake Tableau?" → Karena fitur interaktifnya lengkap, drag-and-drop, easy to use
4. "Apa yang paling menarik?" → Bahwa kepuasan tidak berkorelasi dengan nominal transaksi!

---

## RINGKASAN EKSEKUSI PRESENTASI

| Slide | Judul | Durasi | Persiapan |
|:-----:|-------|:------:|-----------|
| 1 | Cover | 30 detik | Siapin nama & NIM |
| 2 | Latar Belakang | 1 menit | Hafalin konteks |
| 3 | Dataset Overview | 1 menit | Hafalin angka |
| 4 | Pertanyaan Bisnis | 1 menit | Hafalin 5 sub-Q |
| 5 | Tahapan Analisis | 30 detik | Hafalin flowchart |
| 6 | Pembersihan Data | 1 menit | Siapin screenshot |
| 7 | Tren Penjualan | 1.5 menit | **Tunjuk chart Naypyitaw** |
| 8 | Analisis Produk | 1.5 menit | **Tunjuk heatmap** |
| 9 | Analisis Pelanggan | 1 menit | Hafalin angka |
| 10 | Korelasi | 1 menit | **SLIDE PALING PENTING** |
| 11 | Calculated Fields | 30 detik | Cukup sebutin |
| 12 | Dashboard Demo | 2 menit | **Live demo / screenshot** |
| 13 | Rekomendasi | 1.5 menit | Hafalin 5 rekomendasi |
| 14 | Kesimpulan | 1 menit | Hafalin 6 poin |
| 15 | Terima Kasih | 30 detik | Siapin Q&A |
| **Total** | | **~15 menit** | **Siap!** [OK] |

---

## TIPS WAJIB SEBELUM PRESENTASI

```
□ Semua anggota paham isi analisis (jangan cuma 1 orang)
□ Slide sudah di-copy ke USB / Google Drive / laptop
□ File .twbx siap untuk demo (atau screenshot cadangan)
□ Latihan 1-2x sebelum presentasi (ukur durasi)
□ Cek proyektor / LCD sebelum maju
□ Siapin jawaban untuk Q&A (lihat slide 15)
□ Font slide readable dari jarak 3 meter (min 24pt judul)
□ Warna kontras (jangan kuning di background putih)
□ Backup: PDF slide di HP kalau laptop bermasalah
```

---

**GOOD LUCK! [TARGET] GASKEUN! [P1]**
