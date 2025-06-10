import socket
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import hashlib

client_socket = socket.socket()
client_socket.connect(('localhost', 12345))
print("[+] Sunucuya bağlanıldı.")

# Public key al
public_key = RSA.import_key(client_socket.recv(2048))
cipher_rsa = PKCS1_OAEP.new(public_key)

# AES anahtarı ve IV oluştur ve şifrele
aes_key = get_random_bytes(16)
aes_iv = get_random_bytes(16)
encrypted_key = cipher_rsa.encrypt(aes_key + aes_iv)
client_socket.send(encrypted_key)
print("[✓] AES anahtarı gönderildi.")

# Dosya hazırla
filename = "testfile.txt"
with open(filename, "rb") as f:
    file_data = f.read()

file_hash = hashlib.sha256(file_data).hexdigest()
client_socket.send(filename.encode())
client_socket.recv(1024)
client_socket.send(file_hash.encode())
client_socket.recv(1024)
print(f"[+] Dosya adı ve hash gönderildi.\n    SHA256: {file_hash}")

# AES ile şifrele ve gönder
cipher_aes = AES.new(aes_key, AES.MODE_CBC, aes_iv)
encrypted_data = cipher_aes.encrypt(pad(file_data, AES.block_size))

# IV'yi şifrelenmiş veriyle birlikte gönder
client_socket.sendall(aes_iv + encrypted_data)
print("[✓] Dosya gönderildi.")

client_socket.close()
print("[✓] Bağlantı kapatıldı.")
