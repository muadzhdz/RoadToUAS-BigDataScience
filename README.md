# Proyek Analisis Data Penjualan Supermarket (UAS Big Data Science)
## Dokumentasi Hasil Akhir Proyek (Branch hasil)

Repositori ini menyimpan hasil akhir dari Proyek UAS Big Data Science yang berfokus pada analisis transaksi penjualan supermarket (1.000 baris, 17 kolom) di 3 cabang utama (Yangon, Mandalay, Naypyitaw) untuk periode Januari - Maret 2019.

Proyek ini diselesaikan secara eksperimental menggunakan pendekatan Alur Kerja Agen AI Pengkodean Otomatis (Advanced Agentic AI Coding Workflow) yang terbagi menjadi dua cabang utama:
1.  Branch hasil (Branch Saat Ini): Berisi luaran akhir yang bersih, bebas dari naskah kode pemrograman dan siap dikumpulkan.
2.  Branch flow: Berisi alur kerja otomatisasi lengkap, kode sumber Python, spesifikasi teknis, dokumen panduan, dan draft laporan per tahapan.

### Identitas Kelompok:
*   Mu'adz Hudzaifah (NIM: 24903460014)
*   Alhaq Sabilil Izati (NIM: 24903460012)
*   Arfan Ghifari (NIM: 24903460016)
*   Dosen Pengampu: Nur Choiriyati, S.Kom., M.T.

---

### Teknologi AI yang Digunakan (AI Tech Stack)
Eksperimen penyusunan proyek ini memanfaatkan kolaborasi beberapa model dan peralatan AI mutakhir:
*   **Codex**: Digunakan untuk pemahaman logika pemrograman dan validasi dataset berbasis kode.
*   **OpenCode**: Digunakan untuk pemetaan calculated fields dan debugging awal skema database.
*   **Kiro-CLI**: Asisten AI berbasis terminal yang mengeksekusi profil data awal, pembersihan data, serta membangun draf pertama workbook Tableau (.twb).
*   **Antigravity CLI**: Agen AI tingkat lanjut yang melakukan pembersihan total visualisasi, perbaikan kesalahan validasi skema XML Tableau 2026.2, pemecahan masalah Box Plot Outlier Tahap 3, serta kompilasi akhir seluruh luaran.

---

### Struktur Berkas Branch hasil

Berikut adalah berkas pengumpulan akhir yang terdapat pada branch hasil:

*   **Proyek_BigData/**: Folder utama pengumpulan proyek analisis:
    *   **Supermarket_Sales_Dashboard.twbx**: Berkas Tableau Packaged Workbook utuh. Berisi data ekstrak retail supermarket, 10 worksheet visualisasi yang rapi (termasuk visualisasi Box Plot Outlier untuk melengkapi Tahap 3), parameter Top N Products, filter action interaktif berdasarkan kota, dan siap dibuka secara portabel di komputer dosen.
    *   **Laporan_UAS_BigData.md**: Laporan akademis komprehensif berisi Tahap 1 sampai Tahap 6 sesuai panduan UAS, lengkap dengan analisis statistik deskriptif dan visualisasi data.
    *   **Slide_UAS_BigData.md**: Ringkasan presentasi proyek UAS sebanyak 15 slide yang siap dipindahkan ke PowerPoint atau Canva.
    *   **assets/**: Kumpulan 11 screenshot penting yang merekam visualisasi Tableau dan pembuktian pembersihan data (tidak ada data kosong, tidak ada duplikasi kunci primer, serta visualisasi box plot sebaran data).
*   **dataset/**: Menyimpan berkas data pendukung:
    *   **supermarket_sales.csv**: File dataset transaksi penjualan supermarket.
    *   **sumber_dataset.txt**: Penjelasan ringkas metadata dan keaslian sumber dataset supermarket.

---

### Petunjuk Penggunaan

1.  **Membuka Dashboard**: Unduh file Supermarket_Sales_Dashboard.twbx di dalam folder Proyek_BigData/, lalu klik dua kali untuk membukanya menggunakan Tableau Desktop.
2.  **Membaca Laporan**: Buka file Laporan_UAS_BigData.md menggunakan editor markdown pilihan Anda (seperti VS Code atau Obsidian) untuk membaca versi terstruktur dengan gambar tersemat. Anda juga dapat mengekspor file ini ke format PDF atau DOCX menggunakan Word.
