# Algeo02-19051

### Anggota Kelompok
- Yudi Alfayat (13519051)                         
- Mgs. Tabrani (13519122)
- Muhammad Zubair (13519172)

### Deskripsi Singkat
Program ini diberi nama "Mesin Pencari Sederhana". Program dibuat dengan framework Django. Library yang digunakan meliputi library Sastrawi, stop-word dan Bootstrap. Program memanfaatkan prinsip cosine similarity untuk menentukan kecocokan query dengan dokumen yang ada.

### Setup Environment
- Python versi 3.7 ke atas
- Install Django
```
pip install Django
```

### Instalasi Library yang Diperlukan
- Instal library sastrawi
```
pip install Sastrawi
```
- Instal library stopword
```
pip install stop-words
```

### Menjalankan server
Arahkan ke file manage.py
```
python manage.py runserver
```

### Cara kerja mesin: 
- Unggah dokumen yang ingin diketahui similaritasnya dengan query
- Masukkan query yang ingin dicari
- Klik cari
- Kemudian, akan muncul similaritas masing-masing dokumen beserta tabel vektor masing-masing dokumen
- Dokumen yang sudah diunggah akan disimpan di server
- Dokumen yang ada di server bisa dihapus

### Spesifikasi Dokumen
- Dokumen disimpan di dalam file dengan format .txt
- Dalam penamaan file, tidak boleh ada spasi dan dapat diganti dengan tanda underscore
- Baris pertama adalah judul dari dokumen tersebut, dan pada awal judulnya diberi tanda "#"
- Baris kedua adalah kalimat pertama dari dokumen tersebut
- Baris selanjutnya adalah sisa dari isi dokumen

### Lampiran 
- Halaman Utama
![Alt text](test/screenshoot-program/home.png?raw=true "Halaman Utama")
- Halaman Perihal
![Alt text](test/screenshoot-program/perihal.png?raw=true "Perihal")
- Hasil Pencarian (1)
![Alt text](test/screenshoot-program/search1.png?raw=true "Halaman Utama(1)")
- Hasil Pencarian (2)
![Alt text](test/screenshoot-program/search2.png?raw=true "Halaman Utama(2)")
- Halaman Dokumen
![Alt text](test/screenshoot-program/halaman-dokumen.png?raw=true "Halaman Dokumen")
