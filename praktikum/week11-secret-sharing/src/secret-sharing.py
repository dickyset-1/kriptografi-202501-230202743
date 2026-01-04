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