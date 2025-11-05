# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)  
Nama: Dicky Setiawan  
NIM: 230202743  
Kelas: 5 IKRB  

---

## 1. Tujuan
1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Cipher Klasik adalah metode enkripsi yang dominan sebelum era komputer, yang mengandalkan manipulasi karakter (huruf) menggunakan pena dan kertas. Metode ini terbagi menjadi dua kategori utama: Substitusi dan Transposisi. Kekuatan cipher ini secara keseluruhan sangat rendah karena mereka rentan terhadap analisis frekuensi dan memiliki ruang kunci (keyspace) yang terbatas, membuatnya mudah dipecahkan dengan komputasi modern.

Kategori Substitusi bekerja dengan mengganti setiap huruf plaintext dengan huruf lain. Contoh paling sederhana adalah Caesar Cipher, sebuah substitusi monoalfabetik yang mengganti setiap huruf dengan pergeseran tetap (kunci $K$), menghasilkan keamanan yang sangat rendah karena hanya memiliki 25 kunci efektif. Peningkatan signifikan adalah Vigenère Cipher, yang menggunakan substitusi polialfabetik (kata kunci yang berulang) untuk menyamarkan frekuensi huruf tunggal. Meskipun Vigenère pernah dianggap tidak dapat dipecahkan, ia tetap rentan terhadap kriptanalisis seperti Uji Kasiski yang dapat menemukan panjang kata kuncinya.

Sementara itu, Cipher Transposisi bekerja dengan mengubah urutan atau posisi huruf plaintext tanpa mengubah identitas huruf itu sendiri. Kunci pada metode ini sering kali berbentuk pola kolom. Kerentanan utamanya adalah bahwa frekuensi huruf tetap dipertahankan dalam ciphertext yang dihasilkan, berbeda dari cipher substitusi. Kriptanalis dapat dengan mudah mencari pola plaintext yang masuk akal dengan menyusun ulang kolom hingga ciphertext menghasilkan teks yang koheren.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
