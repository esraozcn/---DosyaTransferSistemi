import socket
import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
import hashlib

# Sunucu ayarları
server_socket = socket.socket()
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("[+] Sunucu başlatıldı, bağlantı bekleniyor...")

conn, addr = server_socket.accept()
print(f"[✓] Bağlantı kuruldu: {addr}")

# RSA anahtar çifti oluştur ve public key gönder
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()
conn.send(public_key)
print("[+] Public key istemciye gönderildi.")

# AES anahtarını al
encrypted_key = conn.recv(256)
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
aes_key_iv = cipher_rsa.decrypt(encrypted_key)
aes_key = aes_key_iv[:16]
aes_iv = aes_key_iv[16:]
print("[✓] AES anahtarı alındı ve çözüldü.")

# Dosya adını ve hash’ini al
filename = conn.recv(1024).decode()
conn.send(b"filename ok")
file_hash = conn.recv(1024).decode()
conn.send(b"hash ok")
print(f"[+] Dosya adı: {filename}")
print(f"[+] Beklenen SHA256: {file_hash}")

# Veriyi al
with open(filename, "wb") as f:
    while True:
        data = conn.recv(4096)
        if not data:
            break
        f.write(data)
print("[✓] Şifreli veri alındı.")

# Şifreyi çöz
with open(filename, "rb") as f:
    encrypted_data = f.read()

cipher_aes = AES.new(aes_key, AES.MODE_CBC, aes_iv)
try:
    decrypted_data = unpad(cipher_aes.decrypt(encrypted_data), AES.block_size)
except ValueError as e:
    print(f"[!] Şifre çözme başarısız: {e}")
    conn.send(b"ERROR: Decryption failed")  # Hata mesajı gönder
    conn.close()
    exit()

with open("decrypted_" + filename, "wb") as f:
    f.write(decrypted_data)

# Hash kontrolü
actual_hash = hashlib.sha256(decrypted_data).hexdigest()
if actual_hash == file_hash:
    print("[✓] Dosya başarıyla alındı ve doğrulandı.")
    conn.send(b"OK: File received and verified")  # Başarı mesajı gönder
else:
    print("[!] Hash uyuşmuyor, dosya bozulmuş!")
    conn.send(b"ERROR: Hash mismatch, file corrupted")  # Hata mesajı gönder

conn.close()
