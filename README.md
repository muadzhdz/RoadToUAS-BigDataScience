# Proyek Analisis Data Penjualan Supermarket (UAS Big Data Science)
## Dokumentasi Alur Kerja Agen AI Otomatis (Branch flow)

Repositori ini menyimpan seluruh rancangan alur kerja eksperimental otomatis berbasis Agen AI (seperti Codex, OpenCode, Kiro-CLI, dan Antigravity CLI) untuk menyelesaikan tugas UAS Big Data Science yang berfokus pada analisis transaksi penjualan supermarket (1.000 baris, 17 kolom).

Branch flow ini didesain khusus untuk menyimpan naskah kode pemrograman (Python), spesifikasi teknis, dokumen panduan, dan draft laporan per tahapan analisis secara terstruktur dan terorganisir.

### Identitas Kelompok:
*   Mu'adz Hudzaifah (NIM: 24903460014)
*   Alhaq Sabilil Izati (NIM: 24903460012)
*   Arfan Ghifari (NIM: 24903460016)
*   Dosen Pengampu: Nur Choiriyati, S.Kom., M.T.

---

### Struktur Direktori dan Fungsi File

Berikut adalah pembagian folder dan berkas pada branch flow:

*   **Scripts/**: Berisi naskah kode pemrograman Python untuk otomatisasi alur kerja:
    *   **validation_verify.py**: Melakukan pengecekan dan validasi statistik dasar pada dataset untuk memastikan data bebas dari inkonsistensi sebelum dimasukkan ke Tableau.
    *   **twb_generator.py**: Generator XML otomatis untuk menyusun pondasi dasar workbook Tableau (.twb) menggunakan spesifikasi JSON/YAML.
    *   **build_with_boxplot.py**: Menyusun ulang dan menginjeksi calculated fields, parameter, layout dashboard, serta visualisasi Box Plot disagregat pada berkas workbook (.twb) agar lolos validasi skema XML Tableau 2026.2.
    *   **final_audit.py**: Skrip audit internal untuk memastikan seluruh spesifikasi workbook Tableau (jumlah sheet, parameter, filter, dashboard zone, dan ketiadaan error schema) telah terpenuhi.
    *   **report_generator.py**: Menggabungkan seluruh draft dokumen markdown per tahap menjadi satu kesatuan laporan lengkap.
    *   **slides_generator.py**: Menggabungkan draft materi presentasi markdown menjadi satu file slide presentasi siap pakai.

*   **markdown/**: Folder berkas dokumentasi spesifikasi dan panduan pengerjaan:
    *   **scenario.md**: Dokumen panduan utama Agen AI berisi pertanyaan bisnis, alur pengerjaan Tahap 1-6, serta kriteria keberhasilan proyek.
    *   **dashboard_spec.json**: Definisi layout, koordinat visual, sheet, parameter, dan filter action untuk dashboard Tableau.
    *   **data_spec.yaml**: Spesifikasi field dataset, tipe data asal, tipe data target, serta calculated fields yang harus dibuat.
    *   **PANDUAN_TABLEAU_LENGKAP.md / TABLEAU_WORKFLOW.md**: Dokumentasi detail langkah-langkah teknis di Tableau.
    *   **SCREENSHOT_GUIDE.md**: Panduan letak dan penamaan screenshot penting yang wajib diambil.
    *   **REPORT_READY.md / SLIDE_READY.md**: Konten draft akhir laporan dan slide presentasi.
    *   **TEMPLATE_LAPORAN.md / TEMPLATE_SLIDE.md**: Kerangka dasar laporan dan slide presentasi UAS.
    *   **PROJECT_AUDIT.md / PYTHON_SCRIPT.md**: Catatan kelengkapan audit proyek dan referensi teknis pemrograman.

*   **stage_drafts/**: Folder berisi berkas tulisan draft laporan markdown terpisah untuk masing-masing tahap (Tahap 1 s.d. Tahap 6) sesuai dengan format penilaian dari dosen.

*   **dataset/**: Menyimpan data mentah dan dokumentasi sumbernya:
    *   **supermarket_sales.csv**: File dataset transaksi supermarket yang dianalisis.
    *   **sumber_dataset.txt**: Penjelasan mengenai metadata dan asal usul dataset supermarket sales tersebut.

*   **output_drafts/**: Folder kosong yang ditracking menggunakan file .gitkeep. Folder ini berfungsi sebagai penampung sementara ketika pipeline dijalankan secara lokal di komputer pengguna.

*   **run_all.py**: Skrip pelari utama (runner script) yang terletak di root repositori untuk mengeksekusi seluruh pipeline otomatis (validasi data, pembentukan workbook .twb, dan penggabungan laporan/slide) secara berurutan.

---

### Cara Kerja Otomatisasi (Pipeline Execution)

1.  Pastikan dependensi python seperti Pandas dan PyYAML telah terinstal di komputer.
2.  Buka terminal pada root direktori proyek, lalu jalankan perintah:
    ```bash
    python run_all.py
    ```
3.  Skrip tersebut akan secara otomatis memanggil modul validasi, menyusun workbook Tableau, dan mengompilasi draf laporan serta slide ke dalam folder output_drafts/.
