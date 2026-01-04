# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: Secret Sharing (Shamir’s Secret Sharing)  
Nama: Dicky Setiawan  
NIM: 230202743  
Kelas: 5 IKRB  

---

## 1. Tujuan
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Shamir's Secret Sharing (SSS) adalah algoritma kriptografi yang dirancang oleh Adi Shamir pada tahun 1979 untuk membagi sebuah rahasia (seperti kata sandi atau kunci enkripsi) menjadi beberapa bagian yang disebut sebagai shares. Tujuan utamanya adalah untuk menghindari risiko kehilangan rahasia jika hanya disimpan oleh satu pihak (titik kegagalan tunggal) atau risiko pencurian. Dalam skema ini, rahasia tersebut didistribusikan kepada sekelompok partisipan sedemikian rupa sehingga rahasia tersebut hanya dapat direkonstruksi jika sejumlah minimum partisipan tertentu menggabungkan bagian yang mereka miliki.

Inti dari mekanisme ini terletak pada konsep Ambang Batas (Threshold), yang sering dinotasikan sebagai $(k, n)$. Dalam skema ini, rahasia dibagi menjadi $n$ bagian, namun hanya dibutuhkan minimal $k$ bagian (di mana $k \le n$) untuk mengungkap kembali rahasia asli. Jika jumlah bagian yang terkumpul kurang dari $k$ (misalnya hanya $k-1$ bagian), maka secara matematis tidak mungkin untuk mendapatkan informasi apa pun tentang rahasia tersebut. Hal ini memberikan keseimbangan antara keamanan (mencegah akses tidak sah) dan ketersediaan (rahasia tetap bisa diakses meskipun beberapa bagian hilang atau rusak).

Secara teknis, Shamir's Secret Sharing bekerja berdasarkan prinsip interpolasi polinomial dalam matematika. Rahasia yang ingin dilindungi diletakkan sebagai titik potong-$y$ (konstanta $a_0$) dari sebuah polinomial acak berderajat $k-1$. Setiap share yang diberikan kepada partisipan sebenarnya adalah sebuah titik $(x, y)$ pada kurva polinomial tersebut. Karena diperlukan setidaknya $k$ titik untuk menentukan secara unik sebuah polinomial berderajat $k-1$, maka hanya pemegang $k$ bagian yang dapat menghitung ulang koefisien polinomial tersebut dan menemukan nilai konstanta $a_0$ yang merupakan rahasia aslinya.
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
1. Membuat file `secret-sharing.py` di folder `praktikum/week11-secret-sharing/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python secret-sharing.py`.)

---

## 5. Source Code
import random
import binascii

# --- 1. Fungsi Konversi Teks ke Angka ---
def text_to_int(text):
    hex_str = binascii.hexlify(text.encode()).decode()
    return int(hex_str, 16)

def int_to_text(number):
    hex_str = hex(number)[2:]
    if len(hex_str) % 2 != 0: hex_str = '0' + hex_str
    return binascii.unhexlify(hex_str).decode()

# --- 2. Fungsi Matematika (Modular Inverse) ---
def mod_inverse(a, p):
    def extended_gcd(a, b):
        if b == 0: return a, 1, 0
        d, x1, y1 = extended_gcd(b, a % b)
        return d, y1, x1 - (a // b) * y1
    
    d, x, y = extended_gcd(a, p)
    return x % p

# --- 3. Implementasi Shamir Secret Sharing ---
def split_secret(secret_int, k, n, p):
    # f(x) = a0 + a1*x + a2*x^2 ...
    # a0 adalah rahasia
    coeffs = [secret_int] + [random.randint(1, p - 1) for _ in range(k - 1)]
    
    shares = []
    for x in range(1, n + 1):
        # Hitung y = f(x) mod p
        y = 0
        for i, coeff in enumerate(coeffs):
            y = (y + coeff * pow(x, i, p)) % p
        shares.append((x, y))
    return shares

def recover_secret(shares, p):
    # Menggunakan Interpolasi Lagrange
    secret = 0
    for i in range(len(shares)):
        xi, yi = shares[i]
        num, den = 1, 1
        for j in range(len(shares)):
            if i == j: continue
            xj, yj = shares[j]
            num = (num * -xj) % p
            den = (den * (xi - xj)) % p
        
        term = (yi * num * mod_inverse(den, p)) % p
        secret = (secret + term) % p
    return secret

# --- 4. Simulasi Jalannya Program ---

# Konfigurasi
P = 2**256 - 189 # Bilangan prima besar
secret_input = "KriptografiUPB2025"
k, n = 3, 5

print(f"Rahasia Asli: {secret_input}")

# Proses bagi rahasia (Langkah 1 & 2)
secret_num = text_to_int(secret_input)
shares = split_secret(secret_num, k, n, P)

print("\n--- Shares yang dihasilkan (x, y) ---")
for s in shares:
    print(s)

# Proses rekonstruksi (Langkah 3)
# Kita hanya ambil 3 share pertama untuk membuktikan threshold
recovered_num = recover_secret(shares[:3], P)
recovered_final = int_to_text(recovered_num)

print(f"\nRahasia setelah di-rekonstruksi: {recovered_final}")

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
1. Keuntungan utama Shamir's Secret Sharing dibandingkan membagikan salinan kunci secara langsung terletak pada kombinasi antara keamanan tingkat tinggi dan fleksibilitas akses. Jika 
    Anda membagikan salinan kunci langsung kepada beberapa orang, kebocoran satu salinan saja sudah cukup bagi pihak tidak berwenang untuk mengakses rahasia tersebut; sebaliknya, dengan SSS, rahasia dibagi menjadi bagian-bagian (shares) yang secara matematis tidak memberikan informasi apa pun jika berdiri sendiri. Hal ini menghilangkan risiko "titik kegagalan tunggal" (single point of failure), karena meskipun satu atau beberapa pemegang share kehilangan datanya atau bertindak jahat, rahasia tetap aman dan masih bisa dipulihkan selama jumlah minimum pemegang share lainnya tercapai.

2. Peran threshold (k) dalam keamanan secret sharing adalah menentukan tingkat kesulitan akses dan ketahanan sistem terhadap kehilangan data. Nilai $k$ menetapkan jumlah minimum bagian 
    rahasia yang harus dikumpulkan untuk melakukan rekonstruksi menggunakan interpolasi polinomial. Jika jumlah bagian yang terkumpul kurang dari $k$, maka secara matematis rahasia asli tidak mungkin ditemukan, sehingga $k$ berfungsi sebagai penghalang bagi pihak luar yang mencoba mencuri data secara parsial. Selain itu, $k$ memberikan keseimbangan: nilai $k$ yang terlalu rendah meningkatkan risiko kolusi (penyalahgunaan oleh kelompok kecil), sedangkan $k$ yang terlalu tinggi meningkatkan risiko rahasia hilang permanen jika banyak pemegang share tidak dapat dihubungi.

3. Skenario nyata di mana SSS sangat bermanfaat adalah dalam manajemen kunci cadangan (backup) dompet mata uang kripto (cryptocurrency) milik perusahaan atau organisasi. Alih-alih 
    memberikan seluruh kunci privat kepada satu orang CEO yang berisiko kehilangan kunci atau menyalahgunakannya, perusahaan membagi kunci tersebut menjadi 5 bagian (shares) dengan ambang batas (threshold) 3. Dengan skenario ini, transaksi besar atau pemulihan dana hanya dapat dilakukan jika setidaknya 3 dari 5 direktur setuju dan menggabungkan bagian kunci mereka. Hal ini melindungi aset perusahaan dari pencurian internal oleh individu tunggal sekaligus memastikan dana tetap bisa diakses meskipun dua direktur berhalangan atau kehilangan bagian kuncinya.
---

## 8. Kesimpulan
Praktikum ini berhasil mengimplementasikan skema Shamir's Secret Sharing (SSS) menggunakan Python untuk membagi rahasia menjadi $n$ bagian dengan ambang batas $k$, yang membuktikan bahwa rahasia hanya dapat dipulihkan jika jumlah shares memenuhi kuorum yang ditentukan. Melalui simulasi manual berbasis interpolasi polinomial Lagrange, praktikum ini menunjukkan bahwa keamanan data tetap terjaga karena pemegang share yang kurang dari ambang batas tidak mendapatkan informasi apa pun mengenai rahasia asli. Hasil akhirnya menunjukkan bahwa sistem ini sangat efektif untuk manajemen kunci yang aman di dunia nyata, seperti pada perlindungan aset cryptocurrency dan pemulihan kata sandi, karena berhasil menghilangkan risiko single point of failure.

---

## 9. Daftar Pustaka


---

## 10. Commit Log

commit week11-secret-sharing
Author: Dicky Setiawan <dicky.settt@gmail.com>
Date:   2026-01-04

    week11-secret-sharing: Secret Sharing (Shamir’s Secret Sharing)
```
