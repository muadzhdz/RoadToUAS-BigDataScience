# [SLIDES] TEMPLATE PRESENTASI — UAS Big Data
## Supermarket Sales Analysis

**Format:** PowerPoint / Google Slides
**Maksimal:** 15 Slide
**Durasi Presentasi:** 10-15 menit

---

## Slide-by-Slide

### Slide 1: COVER
**Judul:** Analisis Data Penjualan Supermarket Menggunakan Tableau
**Subjudul:** Big Data Science — UAS
**Nama Kelompok:** [Anggota 1 — NIM], [Anggota 2 — NIM], [Anggota 3 — NIM]
**Dosen:** [Nama Dosen]
**Logo Universitas** (jika ada)

---

### Slide 2: LATAR BELAKANG
**Judul:** Latar Belakang
**Poin:**
- Big Data telah mengubah cara ritel mengambil keputusan
- Supermarket membutuhkan insight dari data transaksi harian
- Dataset: 1.000 transaksi dari 3 cabang (Jan-Mar 2019)
- Tujuan: Identifikasi faktor yang mempengaruhi penjualan & kepuasan
- Tools: Tableau Desktop

**Visual:** Logo Tableau + gambar supermarket

---

### Slide 3: DATASET OVERVIEW
**Judul:** Dataset Supermarket Sales
**Tabel:**
| Metrik | Nilai |
|--------|-------|
| Baris | 1.000 transaksi |
| Kolom | 17 field |
| Cabang | Yangon, Mandalay, Naypyitaw |
| Produk | 6 kategori |
| Periode | 1 Jan – 9 Mar 2019 |
| Total Revenue | $322,966.75 |
| Avg Rating | 6.97 / 10 |

**Visual:** Ikon dataset + screenshot preview data

---

### Slide 4: PERTANYAAN BISNIS
**Judul:** Pertanyaan Bisnis
**Pertanyaan Utama:**
> Faktor apa yang mempengaruhi total penjualan dan kepuasan pelanggan?

**5 Sub-Pertanyaan:**
1. Bagaimana tren penjualan harian per cabang?
2. Produk apa yang paling berkontribusi?
3. Member vs Normal — apa bedanya?
4. Apakah rating berkorelasi dengan nilai transaksi?
5. Bagaimana preferensi metode bayar?

**Visual:** Ikon tanya jawab / mind map

---

### Slide 5: TAHAPAN ANALISIS
**Judul:** Tahapan Analisis (Data Lifecycle)
**Diagram:**
```
Sumber Data (Kaggle)
    ↓
Profiling & Persiapan
    ↓
Pembersihan Data (0 missing, 0 duplikat)
    ↓
Analisis Eksploratif (15 visualisasi)
    ↓
Dashboard Interaktif (Tableau)
    ↓
Sintesis & Rekomendasi
```

**Visual:** Flowchart horizontal

---

### Slide 6: PEMBERSIHAN DATA
**Judul:** Pembersihan Data
**Poin:**
- [OK] Missing Values: **0** dari 1.000 baris
- [OK] Duplikasi: **0** — Setiap Invoice ID unik
- [OK] Inkonsistensi: **0** — Semua format konsisten
- [OK] Outlier: Tidak ada outlier ekstrem
- Konversi: Date (String → Date), Hour (calculated field)

**Visual:** 2-3 screenshot kecil: missing value check, duplicate check

---

### Slide 7: TEMUAN — TREN PENJUALAN
**Judul:** Temuan 1: Tren Penjualan
**Poin:**
- **Naypyitaw** → Revenue tertinggi: $110,568 (meski transaksi paling sedikit)
- Yangon: $106,200 | Mandalay: $106,197
- AOV Naypyitaw: **$337.10** vs $312.35 (Yangon)
- **Peak Hour:** 19:00 (113 transaksi, $39,699)

**Visual:** Line Chart tren per cabang + Bar Chart jam sibuk

---

### Slide 8: TEMUAN — PRODUK
**Judul:** Temuan 2: Analisis Produk
**Poin:**
| Produk | Revenue | Rating |
|--------|:-------:|:------:|
| [1] Food & Beverages | $56,144 | 7.11 |
| [2] Sports & Travel | $55,122 | 6.92 |
| [3] Electronic Acc. | $54,337 | 6.92 |
| Health & Beauty | $49,193 | 7.00 |

- Distribusi merata → diversifikasi berjalan baik
- Naypyitaw dominan F&B, Yangon dominan Home & Lifestyle

**Visual:** Bar chart revenue + Heatmap produk per cabang

---

### Slide 9: TEMUAN — PELANGGAN
**Judul:** Temuan 3: Analisis Pelanggan
**Poin:**
- **Member** spend +3% lebih tinggi ($327.79 vs $318.12)
- 501 Member : 499 Normal → Hampir 50:50
- Rating Member justru **sedikit lebih rendah** (6.94 vs 7.01)
- Cash & Ewallet dominan (~34.5% masing-masing)

**Visual:** Bar chart Member vs Normal + Stacked bar preferensi bayar

---

### Slide 10: TEMUAN — KORELASI
**Judul:** Temuan 4: Analisis Korelasi
**Poin:**
- **Tidak ada korelasi** antara Total transaksi dan Rating
- **Tidak ada korelasi** antara Quantity dan Rating
- Scatter plot acak → R² mendekati 0
- **Kesimpulan:** Kepuasan tidak ditentukan oleh nominal belanja, tapi kualitas layanan & produk

**Visual:** Scatter plot Total vs Rating (tunjukkan trend line datar)

---

### Slide 11: CALCULATED FIELDS
**Judul:** Calculated Fields
**Tabel:**
| Field | Formula |
|-------|---------|
| Hour | INT(LEFT([Time], 2)) |
| Day of Week | DATENAME('weekday', [Date]) |
| Revenue per Unit | [Total] / [Quantity] |
| Rating Category | IF [Rating]≥9 THEN "High"... |
| Transaction Size | IF [Quantity]≥7 THEN "Large"... |

**Visual:** Screenshot panel Data di Tableau

---

### Slide 12: DASHBOARD DEMO
**Judul:** Dashboard Interaktif — Tableau
**Fitur:**
- 6 sheet dalam 1 dashboard
- Quick Filter: City, Product line
- Filter Action: Klik cabang → semua sheet terfilter
- Parameter: Top N Products (1-6)

**Visual:** **SCREENSHOT FULL DASHBOARD** (satu halaman penuh)

---

### Slide 13: REKOMENDASI
**Judul:** Rekomendasi Strategis
**P1 [P1] (Prioritas Tinggi):**
1. **Optimasi jam operasional** — Tambah staf 18:30-20:00, promo "Happy Hour" di jam sepi
2. **Tingkatkan program member** — Tiered membership, referral program, target rasio 60%

**P2 (Prioritas Sedang):**
3. **Strategi produk per cabang** — F&B di Naypyitaw, Home & Lifestyle di Yangon
4. **Investigasi rating Mandalay** (6.82 — terendah)

**P3:**
5. Promosi Credit Card (diskon 2%)

---

### Slide 14: KESIMPULAN
**Judul:** Kesimpulan
**Poin:**
- Dataset bersih (0 missing, 0 duplikat) → siap analisis
- Naypyitaw unggul revenue per transaksi
- Food & Beverages paling populer & memuaskan
- Program member efektif (+3%) tapi bisa dioptimasi
- Kepuasan tidak terkait nominal transaksi
- Jam 19:00 = golden hour operasional
- Dashboard siap digunakan manajemen untuk monitoring

---

### Slide 15: TERIMA KASIH
**Judul:** Terima Kasih
**Poin:**
- [TARGET] Pertanyaan?
- [EMAIL] Kontak: [Email kelompok]
- [FOLDER] Dashboard: [Link Tableau Public atau file .twbx]

**Visual:** QR code link ke dashboard (jika di-publish ke Tableau Public)

---

## Tips Presentasi

| Aspek | Tips |
|-------|------|
| **Durasi** | ~1 menit per slide → Total 15 menit |
| **Jangan baca slide** | Slide = pointer, kamu yang jelaskan |
| **Demo dashboard** | Siapkan 2-3 menit untuk demo live |
| **Siapkan backup** | Screenshot dashboard jika koneksi bermasalah |
| **Fokus insight** | Bukan bagaimana cara buat, tapi APA yang ditemukan |
| **Bahasa** | Konsisten (Indonesia / Inggris) |
| **Q&A** | Siapkan jawaban untuk: "Kenapa pilih dataset ini?" "Apa keterbatasannya?" |

---

## Checklist Sebelum Presentasi

```
□ Slide 1: Cover dengan nama & NIM semua anggota
□ Slide 2: Latar belakang jelas
□ Slide 3: Dataset overview
□ Slide 4: Pertanyaan bisnis
□ Slide 5: Tahapan analisis
□ Slide 6: Pembersihan data + screenshot
□ Slide 7: Tren penjualan (chart)
□ Slide 8: Analisis produk (chart)
□ Slide 9: Analisis pelanggan (chart)
□ Slide 10: Korelasi (scatter plot)
□ Slide 11: Calculated fields
□ Slide 12: Dashboard screenshot FULL
□ Slide 13: Rekomendasi
□ Slide 14: Kesimpulan
□ Slide 15: Terima kasih + kontak
□ Total ≤ 15 slide
□ Warna konsisten
□ Font readable (min 24pt judul, 18pt isi)
□ Tidak ada typo
□ Siap demo dashboard
□ File .twbx siap dikumpulkan
```
