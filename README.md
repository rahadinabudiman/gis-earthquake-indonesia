# SEBARAN GEMPA BUMI NEGARA REPUBLIK INDONESIA TAHUN 2018 - 2023

Gempa di Indonesia - Analisis Data Gempa Bumi

## Daftar Isi

- [Deskripsi](#deskripsi)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)

## Deskripsi

Proyek ini bertujuan untuk menganalisis data gempa bumi di Indonesia dan menyajikan informasi yang bermanfaat kepada pengguna. Proyek ini mencakup beberapa fitur utama, antara lain:

1. Menampilkan rata-rata magnitudo gempa di Indonesia berdasarkan data yang tersedia.
2. Menampilkan provinsi yang paling sering terkena gempa bumi dengan jumlah gempa terbanyak.
3. Menampilkan informasi tentang gempa terbesar yang terjadi di Indonesia pada periode 2018 hingga 2023.
4. Mengurutkan provinsi-provinsi di Indonesia berdasarkan jumlah gempa yang terjadi, sehingga pengguna dapat melihat provinsi-provinsi yang paling sering terkena gempa.
5. Dengan menggunakan data gempa bumi yang tersedia, proyek ini memberikan pemahaman yang lebih baik tentang aktivitas seismik di Indonesia dan membantu dalam pemantauan serta penanganan dampak gempa bumi di berbagai provinsi.

## Instalasi

1. Clone repositori ini ke lokal Anda.

```bash
https://github.com/rahadinabudiman/gis-earthquake-indonesia.git
```

2. Pindah ke direktori proyek.

```bash
cd gis-earthquake-indonesia
```

3. Instal dependensi dengan menggunakan pip.
4. Jalankan kode dengan perintah berikut.

```bash
python main.py
```

## Penggunaan

Berikut adalah langkah-langkah untuk menggunakan proyek Analisis Data Gempa Bumi di Indonesia:

1. Pastikan Anda telah mengikuti langkah instalasi yang tercantum di atas.
2. Dapatkan data gempa bumi dari sumber yang dapat diakses, misalnya situs USGS (United States Geological Survey) yang menyediakan data gempa bumi. Unduh file CSV yang berisi data gempa di Indonesia pada periode yang diinginkan (misalnya, 2018 hingga 2023).
3. Letakkan file CSV gempa di folder proyek ini dan ubah nama file menjadi "Gempa.csv". Pastikan format dan struktur file CSV sesuai dengan contoh yang ada.
4. Jika ingin menggunakan data provinsi yang berbeda, Anda dapat mengganti file CSV "daftar-nama-daerah.csv" dengan data provinsi yang Anda inginkan. Pastikan format dan struktur file CSV tersebut sesuai dengan contoh yang ada.
5. Buka file "main.py" pada editor Python atau lingkungan pengembangan yang Anda gunakan.
6. Sesuaikan kode jika diperlukan. Anda dapat menyesuaikan parameter seperti nama file, kolom yang digunakan, atau menambahkan filter berdasarkan periode waktu tertentu.
7. Jalankan kode "main.py".

```bash
python main.py
```

8. Setelah kode selesai dieksekusi, Anda akan melihat hasil analisis data gempa yang ditampilkan di konsol.
9. Anda dapat menyesuaikan atau memodifikasi kode ini sesuai kebutuhan Anda, misalnya menambahkan visualisasi data atau menyimpan hasil analisis ke dalam file lain.
