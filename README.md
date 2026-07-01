# Proyek Analisis Data Penjualan Supermarket (UAS Big Data Science)
## Hasil Akhir & Dokumentasi Alur Kerja Agen AI Otomatis

Selamat datang di repositori hasil akhir Proyek UAS Big Data Science yang berfokus pada analisis data transaksi penjualan supermarket (1.000 baris, 17 kolom) di 3 cabang utama yaitu A (Yangon), B (Mandalay), dan C (Naypyitaw) untuk periode Januari - Maret 2019.

Proyek ini diselesaikan secara eksperimental menggunakan **Alur Kerja Agen AI Pengkodean Otomatis (Advanced Agentic AI Coding Workflow)**. Eksperimen ini mendemonstrasikan bagaimana agen AI (seperti Kiro-CLI dan Antigravity) dapat berkolaborasi dengan mahasiswa secara interaktif untuk melakukan profil data, pembersihan data, pengujian validasi, pembentukan calculated fields, injeksi schema XML Tableau secara langsung, hingga penyusunan laporan dan slide presentasi yang terstruktur rapi.

### Identitas Kelompok:
*   **Mu'adz Hudzaifah** (NIM: 24903460014)
*   **Alhaq Sabilil Izati** (NIM: 24903460012)
*   **Arfan Ghifari**
*   **Dosen Pengampu**: Nur Choiriyati, S.Kom., M.T.

---

### Struktur Repositori (Dua Branch Utama)
Untuk memisahkan proses eksperimen otomatis dan hasil akhir yang bersih untuk pengumpulan, repositori ini dibagi menjadi dua cabang (*branch*):
1.  **Branch `hasil` (Branch Saat Ini)**: Berisi luaran akhir yang bersih, siap dikumpulkan dan diserahkan kepada dosen.
2.  **Branch `flow`**: Berisi seluruh naskah kode pemrograman (Python), spesifikasi JSON/YAML, berkas *draft* laporan per tahap, panduan teknis, dan catatan riwayat interaksi AI (`conversation.md`).

---

### Daftar File & Folder di Branch `hasil` (Final Deliverables)
*   📁 **`Proyek_BigData/`**: Folder utama pengumpulan UAS sesuai format dari dosen.
    *   📊 **`Supermarket_Sales_Dashboard.twbx`**: Berkas Tableau Packaged Workbook yang sudah dikemas secara penuh. Berisi data ekstrak, 10 worksheet visualisasi yang rapi, dashboard interaktif dengan filter action & parameter, serta siap dijalankan secara portabel tanpa dependensi eksternal.
    *   📝 **`Laporan_UAS_BigData.md`**: Laporan lengkap Tahap 1-6 (sebanyak ~20 halaman) dalam format markdown yang terstruktur rapi dan memiliki seluruh gambar screenshot tersemat.
    *   📊 **`Slide_UAS_BigData.md`**: Draft slide presentasi UAS (~15 slide) lengkap dengan catatan presenter (*presenter notes*).
    *   📁 **`assets/`**: Kumpulan 11 screenshot penting yang merekam pembuktian pembersihan data (ketiadaan missing value, ketiadaan duplikat, box plot outlier) dan visualisasi chart Tableau.
*   📁 **`datasets/retail/supermarket_sales.csv`**: Sumber data transaksi retail asli yang digunakan dalam analisis ini.

---

### Penjelasan Alur Kerja AI (AI Agent Workflow)
Bagaimana proyek UAS ini diselesaikan secara otomatis? Berikut tahapan eksperimen alur kerja agen AI yang tersimpan di branch `flow`:

#### Tahap 1: Pemahaman Konteks & Spesifikasi (Problem Definition)
Agen AI menganalisis berkas spesifikasi dan instruksi dosen untuk menyusun pertanyaan bisnis utama dan sub-pertanyaan, serta merumuskan analisis Big Data berbasis 5V (Volume, Velocity, Variety, Veracity, Value).

#### Tahap 2: Validasi & Profiling Data (Python & Pandas)
Skrip validasi mengeksekusi pemeriksaan tipe data, rentang nilai numerik wajar, ketiadaan data kosong (*missing values*), serta keunikan kunci primer (`Invoice ID`). Hasil validasi matematika ini dicatat dalam laporan untuk memastikan akurasi data 100% sebelum masuk ke Tableau.

#### Tahap 3: Modifikasi XML Tableau secara Terprogram
Alih-alih membuat visualisasi dari nol secara manual di GUI, agen AI memodifikasi kode XML berkas `.twb` Tableau secara langsung melalui skrip Python. Skrip ini secara otomatis:
1.  Menginjeksi **7 Calculated Fields** (Hour, Day of Week, Month, Revenue per Unit, Rating Category, Transaction Size, Week Number).
2.  Menginjeksi **1 Parameter** (`Top N Products` berupa range 1-6).
3.  Membangun **10 Lembar Kerja (Worksheets)** lengkap dengan 2 quick filter (City dan Product line) di setiap sheet.
4.  Membangun **2 Sheet Box Plot Outlier** (`Box Plot Total` dan `Box Plot Rating`) dengan men-disagregatkan data (`Circle` mark class) agar ketiadaan outlier data dapat dibuktikan secara visual.
5.  Menyusun layout dashboard 8 zona berdimensi 1200x900 piksel dengan urutan tag XML yang sesuai dengan skema ketat Tableau 2026.2.

#### Tahap 4: Penggabungan Laporan Otomatis (Report Generator)
Setiap bab laporan yang disusun secara terpisah digabungkan secara otomatis menggunakan skrip generator. Skrip update menyisipkan tautan path gambar screenshot dari folder aset secara dinamis ke dalam dokumen Markdown laporan, sehingga dokumen siap pakai tanpa perlu penyuntingan manual.

---

### Cara Menggunakan & Membuka Hasil Proyek:
1.  **Membuka Dashboard**: Buka [Supermarket_Sales_Dashboard.twbx](file:///C:/Users/adzhd/OneDrive/Documents/My%20Tableau%20Repository/Workbooks/RoadToUAS-BigDataScience/Proyek_BigData/Supermarket_Sales_Dashboard.twbx) menggunakan Tableau Desktop. Karena ini merupakan berkas *packaged workbook*, koneksi data dan visualisasi akan langsung ter-load dengan benar.
2.  **Membaca Laporan**: Buka [Laporan_UAS_BigData.md](file:///C:/Users/adzhd/OneDrive/Documents/My%20Tableau%20Repository/Workbooks/RoadToUAS-BigDataScience/Proyek_BigData/Laporan_UAS_BigData.md) menggunakan pembaca Markdown seperti VS Code, Obsidian, atau ekspor langsung ke Word menggunakan Pandoc untuk diubah menjadi PDF.
