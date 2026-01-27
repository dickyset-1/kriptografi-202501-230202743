# Laporan Praktikum Kriptografi
Minggu ke-: 16  
Topik: Ujian Akhir Semester  
Nama: Dicky Setiawan  
NIM: 230202743  
Kelas: 5 IKRB  

---

## 1. Latar Belakang
Perkembangan teknologi blockchain dan kriptografi modern mendorong lahirnya sistem terdesentralisasi yang mampu menjamin keamanan, transparansi, dan kepercayaan tanpa bergantung pada pihak ketiga. Dalam konteks ini, kriptografi berperan penting sebagai fondasi utama untuk menjaga integritas data, autentikasi pengguna, serta validitas transaksi.

SheepCoin dikembangkan sebagai sistem Web3 berbasis blockchain Ethereum yang bertujuan menjadi media pembelajaran sekaligus simulasi penerapan kriptografi dalam ekosistem aset digital, khususnya melalui penggunaan smart contract dan dompet kripto.

---

## 2. Tujuan
Tujuan utama proyek ini adalah:
1.	Mengimplementasikan token kripto berbasis standar ERC-20.
2.	Mengintegrasikan mekanisme transaksi aman menggunakan kriptografi blockchain.
3.	Mensimulasikan sistem mining, transfer token, dan pencatatan ledger secara terdesentralisasi.
4.	Memberikan pemahaman praktis mengenai peran kriptografi dalam sistem blockchain.

---

## 3. Deskripsi Sistem
SheepCoin merupakan aplikasi Web3 yang berjalan di jaringan Ethereum Sepolia Testnet. Sistem ini memungkinkan pengguna berinteraksi langsung dengan smart contract melalui browser menggunakan dompet digital MetaMask.
Fitur utama sistem meliputi:
•	Koneksi dompet dan autentikasi berbasis kriptografi kunci publik.
•	Mining token secara manual dan otomatis.
•	Transfer token antar pengguna.
•	Pencatatan transaksi global (ledger) yang transparan dan real-time.
Setiap pengguna direpresentasikan oleh satu alamat wallet blockchain, tanpa penyimpanan akun terpusat.

---

## 4. Algoritma dan Protokol Kriptografi yang Digunakan
Sistem SheepCoin tidak mengimplementasikan algoritma kriptografi secara manual, melainkan memanfaatkan kriptografi bawaan blockchain Ethereum, antara lain:
1.	Kriptografi Kunci Publik (Elliptic Curve Cryptography – secp256k1)
    Digunakan untuk:
    - Identitas pengguna (alamat wallet).
    - Penandatanganan transaksi secara digital melalui MetaMask.
2.	Fungsi Hash Kriptografis (Keccak-256)
    Digunakan dalam:
    - Pembentukan hash transaksi.
    - Pengaitan blok dalam blockchain.
    - Menjamin integritas dan keutuhan data transaksi.
3.	Digital Signature
    Setiap transaksi (mining, transfer, pembelian paket) ditandatangani oleh private key pengguna, sehingga menjamin:
    - Autentikasi pengirim.
    - Non-repudiation (transaksi tidak dapat disangkal).
4.	Protokol Konsensus Ethereum (Proof of Stake – Testnet)
    Menjamin validitas dan urutan transaksi tanpa otoritas terpusat.

---

## 5. Uraian Implementasi Komponen Utama
Implementasi sistem dibagi menjadi dua komponen utama:
1.	Smart Contract (Solidity)
    - Mengimplementasikan token ERC-20 SheepCoin (SHP).
    - Mengatur logika mining, auto mining, burn token saat pembelian paket, dan transfer.
    - Menyimpan state penting seperti saldo, waktu mining, dan deadline secara on-chain.
2.	Front End Web3 (HTML, CSS, JavaScript, Ethers.js)
    - Menghubungkan aplikasi dengan MetaMask.
    - engirim transaksi ke smart contract.
    - Menampilkan saldo, status mining, serta histori transaksi secara real-time melalui event Transfer.
Seluruh proses transaksi dilakukan langsung di blockchain tanpa server backend terpusat.

---

## 6. Hasil Pengujian dan Demonstrasi Sistem
Pengujian sistem dilakukan pada jaringan Ethereum Sepolia dengan hasil sebagai berikut:
•	Pengguna berhasil menghubungkan wallet dan diverifikasi melalui tanda tangan kriptografi.
•	Mining manual dan otomatis menghasilkan token SHP sesuai logika smart contract.
•	Transfer token antar alamat berjalan valid dan tercatat di ledger blockchain.
•	Riwayat transaksi dapat dipantau secara real-time melalui event blockchain dan Etherscan.
Hasil ini menunjukkan sistem berfungsi sesuai rancangan dan memanfaatkan mekanisme kriptografi blockchain secara efektif.

---

## 7. Analisis Keeamanan
Dari sisi keamanan, sistem SheepCoin memiliki karakteristik berikut:
Keunggulan Keamanan
•	Tidak menyimpan password atau data sensitif di server.
•	Autentikasi berbasis private key pengguna.
•	Integritas data dijamin oleh hash blockchain.
•	Transparansi penuh melalui ledger publik.
Keterbatasan
•	Belum terdapat mekanisme anti-bot atau pembatasan mining otomatis.
•	Bergantung pada keamanan dompet pengguna (MetaMask).
•	Tidak dirancang untuk penggunaan finansial nyata (hanya simulasi).
Secara keseluruhan, keamanan sistem lebih bergantung pada kekuatan kriptografi dan protokol Ethereum daripada mekanisme aplikasi itu sendiri.

---

## 8. Kesimpulan
Proyek SheepCoin berhasil mengintegrasikan konsep kriptografi ke dalam sistem blockchain Web3 secara nyata dan fungsional. Sistem ini menunjukkan bagaimana kriptografi digunakan untuk autentikasi, integritas data, dan keamanan transaksi tanpa memerlukan pihak ketiga.

Sebagai media pembelajaran, SheepCoin efektif dalam memperlihatkan hubungan antara teori kriptografi dan implementasinya dalam smart contract dan aplikasi terdesentralisasi. Meskipun masih bersifat simulasi, sistem ini memiliki potensi untuk dikembangkan lebih lanjut dengan fitur keamanan tambahan dan penerapan di jaringan utama.

---

## 9. Lampiran

### a. Slide File Presentasi  
Lampiran terdapat pada folder `lampiran/`.

![Slide 1](lampiran/slide-1.jpg)
![Slide 2](lampiran/slide-2.jpg)
![Slide 3](lampiran/slide-3.jpg)
![Slide 4](lampiran/slide-4.jpg)
![Slide 5](lampiran/slide-5.jpg)
![Slide 6](lampiran/slide-6.jpg)
![Slide 7](lampiran/slide-7.jpg)
![Slide 8](lampiran/slide-8.jpg)
![Slide 9](lampiran/slide-9.jpg)
![Slide 10](lampiran/slide-10.jpg)

---

### b. Bukti Pelaksanaan Presentasi
![Bukti Pelaksanaan Presentasi](lampiran/bukti-presentasi.jpeg) 
![Bukti Pelaksanaan Presentasi](lampiran/bukti-presentasiii.jpeg)

---

### c. Manual Book  
**MANUAL BOOK APLIKASI SHEEPCOIN BLOCKCHAIN**

1. **Gambaran Umum Sistem** SheepCoin adalah aplikasi simulasi blockchain berbasis web yang dibangun menggunakan Python dengan framework Flask dan database SQLite. Sistem ini dirancang untuk meniru konsep dasar mata uang kripto seperti wallet, proses mining, transaksi digital, dan pencatatan blok dalam sebuah rantai blockchain. Identitas pengguna menggunakan alamat wallet dari MetaMask, sehingga pendekatannya menyerupai sistem Web3.  

Aplikasi ini memungkinkan pengguna menambang koin SheepCoin, mengirim koin ke wallet lain, serta melihat riwayat blok dan transaksi. Walaupun masih berupa simulasi terpusat, struktur logikanya sudah mengikuti konsep blockchain seperti hash blok, proof of work, dan reward mining.

2. **Teknologi Sistem** Sistem menggunakan Flask sebagai backend, SQLite sebagai database, MetaMask sebagai identitas wallet, hashing SHA-256 untuk keamanan blok, serta mekanisme Proof of Work untuk proses mining.

3. **Struktur Data Sistem** Data pengguna disimpan berdasarkan alamat wallet. Setiap blok menyimpan nomor blok, waktu pembuatan, nilai proof, serta hash blok sebelumnya. Transaksi mencatat pengirim, penerima, jumlah koin, serta blok pencatatannya. Sistem otomatis membuat Genesis Block saat pertama dijalankan.

4. **Mekanisme Blockchain** Mining dilakukan dengan mencari nilai proof yang memenuhi kesulitan hashing. Jika berhasil, blok baru ditambahkan dan miner menerima reward. Hash setiap blok bergantung pada blok sebelumnya sehingga menjaga integritas rantai.

5. **Panduan Penggunaan** Pengguna login melalui MetaMask, masuk ke dashboard, dapat melakukan mining, mengirim koin, serta melihat rantai blockchain dan transaksi.

6. **Keamanan Sistem** Menggunakan SHA-256 dan Proof of Work, namun masih simulasi sehingga belum memakai tanda tangan digital asli seperti blockchain nyata.

7. **Cara Menjalankan Sistem** Install Flask, jalankan `app.py`, lalu akses melalui browser lokal.

8. **Konsep Blockchain yang Dipelajari** Wallet, transaksi kripto, mining, proof of work, hashing, blok, rantai blok, dan reward system.

---

### d. Tautan
1. Repositori GitHub https://dickyset-1.github.io/sheepcoin/
2. Berkas README (week-16-uas/laporan.md; week-16-uas/sheepcoin/app.py; week-16-uas/sheepcoin/sheepcoin.db; week-16-uas/sheepcoin/requirements.txt; week-16-uas/lampiran)
3. ![Riwayat Commit](lampiran/riwayat-commit.png)

---

### e. Bukti Implementasi
![Eksekusi Program](lampiran/eksekusi.png)  
![Kode Inti Penerapan Kriptografi](lampiran/kode-inti.png)  
![Output Program](lampiran/output.png)

---

### f. Sumbangsih Kontribusi Project
Membantu mencari referensi dan membuat PPT presentasi.

---

## 10. Commit Log

commit abc12345
Author: Dicky Setiawan <dicky.settt@gmail.com>
Date:   2025-09-20

    week16-uas : Ujian Akhir Semester
```
