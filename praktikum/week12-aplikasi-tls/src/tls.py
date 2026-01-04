import ssl
import socket
import json
from datetime import datetime

def inspeksi_keamanan_ecommerce(hostname):
    """
    Fungsi untuk menganalisis sertifikat digital dan protokol keamanan 
    pada website e-commerce. (Langkah 1 & 2 Praktikum)
    """
    print(f"\n{'='*60}")
    print(f" ANALISIS KEAMANAN TLS: {hostname}")
    print(f"{'='*60}")

    # Konfigurasi konteks SSL default
    context = ssl.create_default_context()
    
    try:
        # Membuat koneksi ke port 443 (HTTPS)
        with socket.create_connection((hostname, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                
                # 1. Mengambil Informasi Sertifikat (Langkah 1)
                cert = ssock.getpeercert()
                
                # Mengurai Issuer (Certificate Authority)
                issuer = dict(x[0] for x in cert['issuer'])
                ca_name = issuer.get('commonName') or issuer.get('organizationName')
                
                # Mengurai Masa Berlaku
                # Format tanggal SSL: 'Jan  4 23:59:59 2026 GMT'
                fmt = '%b %d %H:%M:%S %Y %Z'
                not_before = datetime.strptime(cert['notBefore'], fmt)
                not_after = datetime.strptime(cert['notAfter'], fmt)
                
                # 2. Analisis Teknologi Enkripsi (Langkah 2)
                cipher_info = ssock.cipher()
                protocol_version = ssock.version()

                # --- OUTPUT LAPORAN ---
                print(f"[+] Versi Protokol : {protocol_version}")
                print(f"[+] Issuer CA      : {ca_name}")
                print(f"[+] Masa Berlaku   :")
                print(f"    - Terbit       : {not_before}")
                print(f"    - Kadaluwarsa  : {not_after}")
                
                print(f"\n[+] Detil Enkripsi (Cipher Suite):")
                print(f"    - Algoritma    : {cipher_info[0]}")
                print(f"    - Protokol TLS : {cipher_info[1]}")
                print(f"    - Kekuatan Bit : {cipher_info[2]} bits")
                
                # Analisis Sederhana
                if "AES" in cipher_info[0]:
                    print("\n[INFO] Website menggunakan standar enkripsi AES (Sangat Aman).")
                if "RSA" in cipher_info[0]:
                    print("[INFO] Pertukaran kunci menggunakan algoritma RSA.")

    except socket.timeout:
        print(f"[!] Error: Koneksi ke {hostname} waktu habis (Timeout).")
    except ssl.SSLError as e:
        print(f"[!] Error SSL pada {hostname}: {e}")
    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")

# --- DAFTAR TARGET ANALISIS (Langkah 1) ---
target_ecommerce = [
    "www.tokopedia.com",
    "www.shopee.co.id",
    "www.bukalapak.com"
]

if __name__ == "__main__":
    for site in target_ecommerce:
        inspeksi_keamanan_ecommerce(site)
    
    print(f"\n{'='*60}")
    print(" ANALISIS SELESAI")
    print(" Gunakan output di atas untuk mengisi laporan.md")
    print(f"{'='*60}")