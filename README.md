# Algeo02-19051

### Anggota Kelompok
- Yudi Alfayat (13519051)                         
- Mgs. Tabrani (13519122)
- Muhammad Zubair (13519172)''

### Deskripsi Singkat
Program ini diberi nama "Mesin Pencari Sederhana". Program dibuat dengan framework Django. Library yang digunakan meliputi library Sastrawi, stop-word dan Bootstrap. Program memanfaatkan prinsip cosine similarity untuk menentukan kecocokan query dengan dokumen yang ada.

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

### Lampiran 
![Alt text](doc/home.png?raw=true "Halaman Utama")
![Alt text](doc/perihal.png?raw=true "Perihal")
![Alt text](doc/search1.png?raw=true "Halaman Utama(1)")
![Alt text](doc/search2.png?raw=true "Halaman Utama(2)")