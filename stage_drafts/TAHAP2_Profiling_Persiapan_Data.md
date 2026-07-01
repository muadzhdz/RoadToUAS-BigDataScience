# Tahap 2: Profiling dan Persiapan Data
## Supermarket Sales Analysis

---

## 1. Kondisi Dasar Dataset

| Metrik | Nilai |
|--------|-------|
| **Jumlah Baris** | 1.000 transaksi |
| **Jumlah Kolom** | 17 field |
| **Rentang Waktu** | 1 Januari 2019 – 9 Maret 2019 (89 hari) |
| **Rentang Jam** | 10:00 – 20:59 |
| **Total Pendapatan** | $322,966.75 |
| **Total HPP (COGS)** | $307,587.38 |
| **Total Gross Income** | $15,379.37 |
| **Sumber Data** | Kaggle — Supermarket Sales Dataset |

---

## 2. Deskripsi Setiap Field

| # | Nama Field | Tipe Data | Makna dalam Konteks Bisnis |
|---|------------|-----------|---------------------------|
| 1 | **Invoice ID** | String (Text) | Nomor unik setiap transaksi — identifier utama |
| 2 | **Branch** | String (Kategorikal) | Kode cabang supermarket: A (Yangon), B (Mandalay), C (Naypyitaw) |
| 3 | **City** | String (Kategorikal) | Kota lokasi cabang |
| 4 | **Customer type** | String (Kategorikal) | Tipe pelanggan: Member (terdaftar) atau Normal (umum) |
| 5 | **Gender** | String (Kategorikal) | Jenis kelamin pelanggan: Male / Female |
| 6 | **Product line** | String (Kategorikal) | Kategori produk yang dibeli (6 kategori) |
| 7 | **Unit price** | Numerik (Decimal) | Harga satuan per produk (dalam USD) |
| 8 | **Quantity** | Numerik (Integer) | Jumlah unit produk yang dibeli |
| 9 | **Tax 5%** | Numerik (Decimal) | Pajak 5% dari total transaksi |
| 10 | **Total** | Numerik (Decimal) | Total nilai transaksi setelah pajak |
| 11 | **Date** | Date (Tanggal) | Tanggal transaksi |
| 12 | **Time** | Time (Waktu) | Jam transaksi |
| 13 | **Payment** | String (Kategorikal) | Metode pembayaran: Cash, Ewallet, Credit card |
| 14 | **cogs** | Numerik (Decimal) | Cost of Goods Sold — Harga pokok penjualan |
| 15 | **gross margin percentage** | Numerik (Decimal) | Persentase margin kotor (4.76% konstan) |
| 16 | **gross income** | Numerik (Decimal) | Pendapatan kotor (Total - cogs) |
| 17 | **Rating** | Numerik (Decimal) | Rating kepuasan pelanggan (1-10) |

---

## 3. Pengecekan Tipe Data

### 3.1. Ringkasan Pengecekan

| Field | Tipe Saat Ini (CSV) | Seharusnya | Perlu Diubah? |
|-------|--------------------|------------|:---:|
| Invoice ID | String | String | [NO] Tidak |
| Branch | String | String (Kategorikal) | [NO] Tidak |
| City | String | String (Kategorikal) | [NO] Tidak |
| Customer type | String | String (Kategorikal) | [NO] Tidak |
| Gender | String | String (Kategorikal) | [NO] Tidak |
| Product line | String | String (Kategorikal) | [NO] Tidak |
| Unit price | Numerik | Number (Decimal) | [NO] Tidak |
| Quantity | Numerik | Number (Integer) | [NO] Tidak |
| Tax 5% | Numerik | Number (Decimal) | [NO] Tidak |
| Total | Numerik | Number (Decimal) | [NO] Tidak |
| **Date** | **String (M/D/YYYY)** | **Date** | **[OK] WAJIB — Parse ke Date** |
| **Time** | **String (HH:MM)** | **Time** | **[OK] WAJIB — Parse ke Time** |
| Payment | String | String (Kategorikal) | [NO] Tidak |
| cogs | Numerik | Number (Decimal) | [NO] Tidak |
| gross margin percentage | Numerik | Number (Decimal) | [NO] Tidak |
| gross income | Numerik | Number (Decimal) | [NO] Tidak |
| Rating | Numerik | Number (Decimal) | [NO] Tidak |

### 3.2. Pengecekan Missing Values

**Hasil: TIDAK ADA missing values (0 null) di seluruh 17 kolom.** Semua 1.000 baris memiliki data lengkap. Data sudah bersih dari sisi kelengkapan.

### 3.3. Pengecekan Duplikasi

**Hasil: TIDAK ADA data duplikat.** Setiap Invoice ID unik — 1.000 nilai unik dari 1.000 baris.

---

## 4. Standardisasi Tipe Data

### 4.1. Konversi Date (String → Date)

**Sebelum:** `Date` bertipe String dengan format `M/D/YYYY` (contoh: `1/5/2019`, `3/8/2019`)

**Di Tableau:**
1. Setelah import CSV, buka tab **Data Source**
2. Klik ikon tipe data pada kolom `Date`
3. Pilih **Date**
4. Pastikan Tableau membaca format tanggal sebagai **M/D/YYYY**

**Screenshot:**

![Konfigurasi Tipe Data dan Kolom di Tableau](assets/Data-Source.png)

### 4.2. Konversi Time (String → Time)

**Sebelum:** `Time` bertipe String dengan format `HH:MM` (contoh: `13:08`, `10:29`)

**Di Tableau:**
1. `Time` dapat dibaca sebagai teks oleh default
2. Rekomendasi praktis: biarkan `Time` sebagai teks dan buat calculated field `Hour`

**Rekomendasi:** Buat **Calculated Field** baru:
```
Hour = INT(LEFT([Time], 2))
```
Ini memudahkan analisis tren per jam.

### 4.3. Verifikasi Numerik

Semua field numerik (Unit price, Quantity, Tax 5%, Total, cogs, gross margin percentage, gross income, Rating) sudah dalam format numerik yang benar:

| Field | Range | Valid |
|-------|-------|:-----:|
| Unit price | 10.08 – 99.96 | [OK] |
| Quantity | 1 – 10 | [OK] |
| Total | $10.68 – $1,042.65 | [OK] |
| Rating | 4.0 – 10.0 | [OK] |
| gross income | $0.51 – $49.65 | [OK] |

---

## 5. Field Utama untuk Analisis

Berdasarkan pertanyaan bisnis dan sub-pertanyaan analitik, berikut field utama yang akan digunakan:

| Prioritas | Field | Peran dalam Analisis |
|:---------:|-------|---------------------|
| [PRIMER] **Primer** | **Total** | Metrik utama — nilai penjualan |
| [PRIMER] **Primer** | **Date** | Dimensi waktu — tren penjualan |
| [PRIMER] **Primer** | **City / Branch** | Dimensi cabang — perbandingan antar kota |
| [SEKUNDER] **Sekunder** | **Product line** | Dimensi produk — performa kategori |
| [SEKUNDER] **Sekunder** | **Rating** | Metrik kepuasan — korelasi dengan penjualan |
| [SEKUNDER] **Sekunder** | **Customer type** | Segmen pelanggan — analisis member vs normal |
| [BLUE] **Tersier** | **Payment** | Metode bayar — preferensi pembayaran |
| [BLUE] **Tersier** | **Quantity** | Volume — jumlah item per transaksi |
| [BLUE] **Tersier** | **Time** | Waktu — jam sibuk |
| [PENDUKUNG] **Pendukung** | **Gender** | Demografi — filter tambahan |

---

## 6. Persiapan di Tableau

### Langkah-langkah:

1. **Import CSV** ke Tableau (Connect → Text File)
2. **Verifikasi tipe data** otomatis:
   - `Date` → Date (M/D/YYYY)
   - `Time` → Text (akan dibuatkan `Hour` sebagai calculated field)
   - Semua numerik → Number
   - Sisanya → Text (kategorikal)
3. **Buat Calculated Field** untuk memperkaya analisis:
   - `Hour` = `INT(LEFT([Time], 2))` — jam transaksi
   - `Day of Week` = `DATENAME('weekday', [Date])` — nama hari
   - `Month` = `DATENAME('month', [Date])` — bulan
   - `Revenue per Unit` = `[Total] / [Quantity]` — harga rata-rata per item
4. **Data siap** untuk tahap analisis selanjutnya

### Catatan:
Tidak ada perubahan struktur data yang signifikan karena dataset sudah dalam kondisi baik. Semua langkah di atas bersifat standarisasi format untuk memudahkan visualisasi dan kalkulasi di Tableau.

---

*Lanjut ke **Tahap 3: Pembersihan Data** setelah dokumen ini disetujui.*
