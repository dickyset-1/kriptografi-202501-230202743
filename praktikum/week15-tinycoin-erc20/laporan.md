# Laporan Praktikum Kriptografi
Minggu ke-: 15  
Topik: TinyCoin ERC20  
Nama: Dicky Setiawan  
NIM: 230202743  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3. Menyusun laporan teknis hasil proyek akhir.
---

## 2. Dasar Teori
TinyCoin berbasis ERC-20 dapat dipahami melalui teori dasar token standar pada blockchain Ethereum. ERC-20 adalah spesifikasi teknis yang mendefinisikan aturan bagaimana sebuah token dibuat, dipindahkan, dan dikelola di jaringan Ethereum melalui smart contract. Standar ini memastikan token seperti TinyCoin kompatibel dengan dompet digital, bursa kripto, dan aplikasi terdesentralisasi (dApps). Fungsi inti ERC-20 meliputi transfer, approve, transferFrom, serta pencatatan balanceOf dan totalSupply, yang memungkinkan pengelolaan saldo dan transaksi token secara transparan di blockchain.

Secara konseptual, TinyCoin sebagai token ERC-20 tidak memiliki blockchain sendiri, melainkan berjalan di atas infrastruktur Ethereum. Keamanan dan validitas transaksi dijamin oleh mekanisme konsensus Ethereum serta kriptografi kunci publik. Smart contract TinyCoin menyimpan logika terkait jumlah suplai token, mekanisme distribusi, dan aturan transaksi. Karena seluruh kode tersimpan di blockchain, sifatnya transparan, tidak mudah diubah (immutable), dan dapat diaudit. Namun, keamanan tetap bergantung pada kualitas kode smart contract; kesalahan logika dapat menyebabkan kerentanan seperti eksploitasi kontrak.

Dari sisi teori ekonomi digital, TinyCoin ERC-20 dapat berfungsi sebagai alat tukar, token utilitas, atau representasi aset dalam ekosistem tertentu. Nilainya dipengaruhi oleh suplai, permintaan, serta kegunaan token dalam sistem yang mendukungnya, misalnya untuk pembayaran layanan, reward, atau akses fitur khusus. Model tokenomics—seperti pembatasan suplai, mekanisme burning, atau staking—sering diterapkan untuk menjaga stabilitas nilai dan insentif pengguna. Dengan memanfaatkan standar ERC-20, TinyCoin memperoleh interoperabilitas tinggi sekaligus fondasi teknis yang telah teruji dalam ekosistem blockchain global.

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
1. Membuat file `tinycoin-erc20.py` di folder `praktikum/week15-tinycoin-erc20/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python tinycoin-erc20.py`.)

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
1. Fungsi utama ERC-20 dalam ekosistem blockchain adalah sebagai standar teknis yang menyamakan cara pembuatan dan pengelolaan token di jaringan Ethereum, sehingga semua token yang 
    mengikuti standar ini dapat saling kompatibel dengan dompet, bursa kripto, dan aplikasi terdesentralisasi. Dengan adanya aturan fungsi dasar seperti pencatatan saldo dan transfer, ERC-20 memudahkan integrasi, meningkatkan interoperabilitas, dan mempercepat pengembangan ekosistem aset digital tanpa perlu membangun sistem dari nol.

2. Mekanisme transfer token dalam kontrak ERC-20 bekerja melalui pemanggilan fungsi pada smart contract. Fungsi transfer digunakan untuk mengirim token langsung dari pemilik ke 
    alamat lain, sedangkan approve dan transferFrom memungkinkan pihak ketiga memindahkan token atas izin pemilik, misalnya pada sistem marketplace atau DeFi. Setiap transaksi dicatat di blockchain, saldo diperbarui secara otomatis, dan peristiwa transfer (event) disiarkan agar dapat dipantau oleh aplikasi lain.

3. Risiko utama implementasi smart contract meliputi bug logika, celah keamanan seperti reentrancy, kesalahan perhitungan, serta kesalahan pengelolaan hak akses. Karena kontrak 
    bersifat sulit diubah setelah diterbitkan, kesalahan kecil bisa berakibat kerugian besar. Mitigasinya mencakup audit kode oleh pihak independen, pengujian menyeluruh, penggunaan pustaka standar yang sudah teruji, penerapan pola keamanan (misalnya checks-effects-interactions), serta mekanisme upgrade atau fail-safe untuk mengurangi dampak jika terjadi kerentanan.
---

## 8. Kesimpulan


---

## 9. Daftar Pustaka


---

## 10. Commit Log

commit abc12345
Author: Dicky Setiawan <dicky.settt@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
