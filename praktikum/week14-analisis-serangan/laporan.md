# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Analisis Serangan Kriptografi  
Nama: Dicky Setiawan  
NIM: 230202743  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Analisis serangan kriptografi (cryptanalysis) merupakan cabang dari ilmu kriptografi yang berfokus pada upaya memahami, mengevaluasi, dan menembus sistem pengamanan data tanpa mengetahui kunci rahasia secara langsung. Tujuan utamanya bukan hanya untuk “membobol” sandi, tetapi juga untuk menguji seberapa kuat suatu algoritma kriptografi dalam melindungi kerahasiaan, integritas, dan autentikasi data. Dengan melakukan analisis serangan, peneliti dapat menemukan kelemahan pada algoritma, protokol, atau implementasi sistem, sehingga perbaikan dapat dilakukan sebelum sistem tersebut digunakan secara luas. Oleh karena itu, cryptanalysis justru menjadi bagian penting dalam pengembangan sistem keamanan informasi yang andal.

Secara teori, serangan kriptografi diklasifikasikan berdasarkan informasi yang dimiliki penyerang. Pada ciphertext-only attack, penyerang hanya memiliki data terenkripsi dan berusaha menebak plaintext atau kunci. Pada known-plaintext attack, penyerang mengetahui sebagian pasangan plaintext dan ciphertext untuk menganalisis pola enkripsi. Selanjutnya, chosen-plaintext attack dan chosen-ciphertext attack memberi penyerang kemampuan memilih data yang akan dienkripsi atau didekripsi untuk mengamati respons sistem. Klasifikasi ini membantu dalam memodelkan tingkat ancaman dan menjadi dasar dalam merancang algoritma yang tahan terhadap berbagai skenario serangan.

Selain berdasarkan model akses data, analisis serangan juga ditinjau dari pendekatan yang digunakan, yaitu serangan brute force, kriptanalisis matematis, dan serangan berbasis implementasi. Brute force attack mencoba semua kemungkinan kunci hingga menemukan yang benar, sehingga kekuatan sistem sangat bergantung pada panjang kunci. Kriptanalisis matematis memanfaatkan kelemahan struktur algoritma, seperti pola statistik atau sifat aljabar tertentu. Sementara itu, serangan implementasi seperti side-channel attack mengeksploitasi kebocoran informasi dari aspek fisik sistem, misalnya waktu proses, konsumsi daya, atau radiasi elektromagnetik. Kombinasi pemahaman teoritis dan evaluasi praktis inilah yang membentuk dasar analisis serangan dalam kriptografi modern.

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
1. Membuat file `analisis_serangan.py` di folder `praktikum/week14-analisis_serangan/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python analisis_serangan.py`.)

---

## 5. Source Code


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
1. Banyak sistem lama masih rentan terhadap brute force atau dictionary attack karena dirancang pada masa ketika daya komputasi penyerang masih terbatas, sehingga mekanisme 
    perlindungan seperti pembatasan percobaan login, penggunaan salt, dan algoritma hashing yang lambat belum menjadi standar. Selain itu, sistem warisan (legacy systems) sering tidak diperbarui karena keterbatasan biaya, ketergantungan pada arsitektur lama, atau kekhawatiran gangguan operasional, sehingga tetap menggunakan algoritma usang seperti MD5 atau SHA-1 serta kebijakan password yang lemah.

2. Perbedaan antara kelemahan algoritma dan kelemahan implementasi terletak pada sumber masalahnya. Kelemahan algoritma berasal dari desain matematis kriptografi itu sendiri, 
    misalnya fungsi hash yang rentan collision atau ukuran kunci yang terlalu pendek. Sementara itu, kelemahan implementasi muncul ketika algoritma yang sebenarnya kuat digunakan dengan cara yang salah, seperti penyimpanan kunci dalam plaintext, tidak adanya salt pada hashing password, atau konfigurasi protokol keamanan yang tidak tepat.

3. Agar sistem kriptografi tetap aman di masa depan, organisasi perlu menerapkan pendekatan berkelanjutan seperti pembaruan algoritma sesuai standar terbaru (misalnya rekomendasi 
    NIST), audit keamanan rutin, penerapan patch, serta pemantauan ancaman terkini. Selain itu, desain sistem sebaiknya bersifat kripto-agile, yaitu memungkinkan penggantian algoritma tanpa merombak seluruh sistem, sehingga adaptasi terhadap perkembangan teknologi komputasi dan metode serangan baru dapat dilakukan dengan cepat dan efektif.
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka


---

## 10. Commit Log

commit abc12345
Author: Dicky Setiawan <dicky.settt@gmail.com>
Date:   2026-01-26

    week14-analisis_serangan: Analisis Serangan Kriptografi
```
