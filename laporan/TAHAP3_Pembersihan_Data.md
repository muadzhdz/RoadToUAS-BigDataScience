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
