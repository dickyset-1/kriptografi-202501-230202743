from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, timezone

# 1. Generate Private Key
# Key size 2048 adalah standar keamanan minimum saat ini
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 2. Konfigurasi Identitas (Subject & Issuer)
# Menggunakan u"string" untuk memastikan format unikode
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Jawa Barat"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Bekasi"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"upb-kripto.ac.id"),
])

# 3. Proses Build Sertifikat
# Perbaikan: Menggunakan timezone-aware datetime agar tidak muncul warning
now = datetime.now(timezone.utc)

cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(now)
    .not_valid_after(now + timedelta(days=365))
    .add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True,
    )
    .sign(private_key, hashes.SHA256())
)

# 4. Simpan Sertifikat (Public Key)
with open("sertifikat_digital.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

# 5. Simpan Private Key (Sangat Penting!)
# Menggunakan enkripsi BestAvailableEncryption agar file kunci tidak bisa dibuka sembarang orang
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"password-praktikum"),
    ))

print("✅ Sukses: 'sertifikat_digital.pem' dan 'private_key.pem' telah dibuat.")