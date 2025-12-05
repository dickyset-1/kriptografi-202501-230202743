# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Deffie Hellman Key Exchange 
Nama: Dicky Setiawan  
NIM: 230202743  
Kelas: 5 IKRB

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).


---

## 2. Dasar Teori
Diffie-Hellman (DH) Key Exchange adalah metode kriptografi fundamental yang memungkinkan dua pihak, sebut saja Alice dan Bob, untuk menetapkan kunci rahasia bersama melalui saluran komunikasi yang tidak aman atau publik. Prinsip kerjanya didasarkan pada kesulitan matematis dari Masalah Logaritma Diskrit (DLP), yaitu fungsi satu arah di mana perhitungan maju (eksponensiasi modulo) mudah dilakukan, tetapi sangat sulit untuk dibalik (menemukan eksponen privat) oleh pihak ketiga, bahkan jika mereka mengetahui semua variabel publik yang dipertukarkan. Proses dimulai dengan kesepakatan publik atas dua bilangan: bilangan prima besar ($p$) dan generator ($g$).Proses pertukaran kunci DH melibatkan empat langkah. Pertama, Alice dan Bob masing-masing secara rahasia memilih bilangan privat ($a$ dan $b$). Kedua, mereka menghitung nilai publik mereka masing-masing ($A = g^a \pmod{p}$ dan $B = g^b \pmod{p}$) dan kemudian saling menukarkan nilai publik tersebut melalui saluran yang tidak aman. Ketiga, setelah menerima nilai publik lawan, masing-masing pihak menggunakan nilai publik lawan dan kunci privat mereka sendiri untuk menghitung kunci rahasia bersama. Alice menghitung $S = B^a \pmod{p}$, dan Bob menghitung $S = A^b \pmod{p}$.Hasilnya, kedua perhitungan tersebut secara matematis akan selalu menghasilkan nilai $S$ yang sama, karena $S = g^{ab} \pmod{p}$. Nilai $S$ inilah yang menjadi kunci simetris rahasia bersama yang kemudian dapat mereka gunakan untuk mengenkripsi dan mendekripsi pesan mereka selanjutnya. Meskipun sangat efektif untuk menghasilkan kunci secara rahasia, DH Key Exchange secara mendasar tidak memberikan otentikasi identitas, sehingga rentan terhadap serangan Man-in-the-Middle (MITM). Oleh karena itu, dalam penerapan modern, DH selalu digabungkan dengan sertifikat digital atau tanda tangan untuk memverifikasi identitas.  )

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
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
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
1. Diffie-Hellman (DH) memungkinkan pertukaran kunci rahasia di saluran komunikasi yang tidak aman (publik) berkat properti matematika yang disebut Masalah Logaritma Diskrit (DLP). Prinsip kerjanya adalah setiap pihak, Alice dan Bob, memilih bilangan rahasia pribadi ($a$ dan $b$) dan kemudian mengombinasikannya dengan bilangan publik ($g$ dan $p$) untuk menghasilkan nilai publik parsial ($A = g^a \pmod p$ dan $B = g^b \pmod p$). Kedua nilai parsial ini kemudian dipertukarkan. Ketika Alice menerima $B$, ia mengangkatnya dengan rahasianya $a$, dan Bob melakukan hal yang sama dengan $A$ dan $b$. Hasil akhirnya selalu sama, yaitu kunci rahasia bersama $K = g^{ab} \pmod p$.Seorang penyadap yang mengamati semua nilai publik ($A, B, g, p$) tidak dapat dengan mudah menghitung nilai rahasia $a$ atau $b$, yang diperlukan untuk mendapatkan kunci bersama $K$. Kesulitan komputasi ini, di mana mencari eksponen ($a$) ketika basis ($g$), hasil ($A$), dan modulus ($p$) diketahui sangat sulit, inilah yang menjadi landasan keamanan DH. Protokol ini berhasil membuat kunci bersama tanpa pernah mengirimkan nilai rahasia pribadi secara langsung, menjadikannya solusi fundamental untuk negosiasi kunci di internet.

2. Kelemahan utama dari protokol Diffie-Hellman murni adalah kurangnya otentikasi identitas antara pihak yang berkomunikasi. Protokol ini dirancang hanya untuk menukarkan parameter kunci secara kriptografis, tetapi tidak memiliki mekanisme bawaan untuk memverifikasi siapa sebenarnya yang berada di ujung komunikasi. Alice tidak dapat memastikan bahwa nilai yang dia terima benar-benar berasal dari Bob, dan sebaliknya. Kurangnya verifikasi identitas inilah yang membuka celah keamanan terbesar pada DH murni.Celah ini membuat Diffie-Hellman murni rentan terhadap Serangan Man-in-the-Middle (MITM). Dalam serangan MITM, penyerang dapat mencegat pertukaran kunci, bertindak sebagai Alice bagi Bob, dan bertindak sebagai Bob bagi Alice. Penyerang melakukan dua pertukaran DH terpisah, satu dengan Alice dan satu dengan Bob, dan berhasil membuat dua kunci rahasia terpisah—satu dengan Alice dan satu dengan Bob. Akibatnya, penyerang dapat mendekripsi pesan dari satu pihak, membacanya, dan mengenkripsi ulang menggunakan kunci yang lain sebelum meneruskannya, tanpa diketahui oleh Alice maupun Bob.

3. Cara paling efektif untuk mencegah Serangan Man-in-the-Middle (MITM) pada protokol Diffie-Hellman adalah dengan mengintegrasikan otentikasi dan integritas ke dalam proses pertukaran. Hal ini dilakukan dengan meminta pihak yang berkomunikasi untuk memberikan bukti identitas mereka. Mekanisme utama yang digunakan adalah Tanda Tangan Digital (Digital Signatures). Setelah Alice dan Bob menghitung nilai publik DH parsial mereka, mereka menggunakan kunci privat mereka masing-masing untuk menandatangani nilai tersebut sebelum mengirimkannya.Tanda tangan digital ini diverifikasi oleh pihak penerima menggunakan kunci publik yang tepercaya, seringkali diverifikasi melalui Sertifikat Digital yang diterbitkan oleh Otoritas Sertifikat (CA). Dengan cara ini, penyerang yang mencoba memalsukan nilai DH tidak dapat membuat tanda tangan digital yang valid yang sesuai dengan identitas palsu tersebut. Dalam praktik modern, DH diimplementasikan dalam protokol yang lebih besar seperti TLS/SSL, di mana otentikasi server (dan opsional klien) melalui tanda tangan digital dan sertifikat adalah langkah wajib untuk menjamin bahwa pertukaran kunci dilakukan dengan entitas yang sah.
---

## 8. Kesimpulan
Praktikum ini berhasil mensimulasikan protokol Diffie-Hellman menggunakan Python, menunjukkan secara empiris bahwa dua pihak (Alice dan Bob) dapat berhasil menyepakati kunci rahasia bersama ($K = g^{ab} \pmod p$) melalui pertukaran nilai publik, membuktikan prinsip logaritma diskrit sebagai dasar keamanannya. Simulasi kemudian dilanjutkan dengan analisis keamanan, di mana kelemahan utama protokol murni terekspos melalui demonstrasi serangan Man-in-the-Middle (MITM); penyerang berhasil membuat dua kunci rahasia terpisah dengan masing-masing pihak tanpa terdeteksi otentikasi. Secara keseluruhan, kegiatan ini memenuhi tujuan pembelajaran dengan menghasilkan program fungsional dan analisis yang kuat, mengonfirmasi perlunya penambahan mekanisme otentikasi (seperti Tanda Tangan Digital) dalam protokol DH untuk implementasi yang aman di dunia nyata.

---

## 9. Daftar Pustaka

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Dicky Setiawan <email>
Date:   2025-12-05

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
