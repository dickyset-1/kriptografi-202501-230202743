# Laporan Praktikum Kriptografi
Minggu ke-: 3   
Topik: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)    
Nama: Dicky Setiawan    
NIM: 230202743  
Kelas: 5 IKRB   

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Cipher klasik adalah algoritma enkripsi yang digunakan sebelum era komputer modern, beroperasi dengan dua teknik dasar: substitusi (mengganti satu unit teks terang dengan unit lain, misalnya Caesar Cipher) atau transposisi (mengubah urutan unit teks terang). Tujuannya adalah mengubah teks terang (pesan asli) menjadi teks tersandi (bentuk terenkripsi) menggunakan suatu kunci rahasia. Keamanan cipher ini sepenuhnya bergantung pada kerahasiaan kuncinya, bukan pada kerumitan algoritmanya.

Aritmetika modular adalah sistem matematika yang melibatkan bilangan bulat, di mana bilangan 'melingkar' (wrap around) setelah mencapai nilai tertentu yang disebut modulus ($n$). Inti konsepnya adalah kekongruenan modulo $n$ (ditulis $a \equiv b \pmod{n}$), yang berarti $a$ dan $b$ memiliki sisa yang sama ketika dibagi dengan $n$. Dalam kriptografi klasik, konsep ini sangat fundamental. Misalnya, untuk mengimplementasikan pergeseran pada alfabet 26 huruf (A=0 hingga Z=25), operasi aritmetika selalu dilakukan modulo 26. Ini memastikan hasil operasi, seperti penambahan kunci (pergeseran), selalu berada dalam rentang indeks alfabet (0 sampai 25).

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
