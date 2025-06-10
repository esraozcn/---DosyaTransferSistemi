
from scapy.all import IP, ICMP, send, sr1

target_ip = "8.8.8.8"

# ICMP Echo Request (ping) paketi oluştur
packet = IP(dst=target_ip)/ICMP()

# Paketi gönder ve cevap bekle
response = sr1(packet, timeout=2)

if response:
    print(f"{target_ip} adresine ping başarılı: {response.summary()}")
else:
    print(f"{target_ip} adresinden cevap alınamadı.")
