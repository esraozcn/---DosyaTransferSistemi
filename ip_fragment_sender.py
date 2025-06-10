
from scapy.all import IP, ICMP, fragment, send
import random

target_ip = "127.0.0.1"
payload = "X" * 4000  # 4000 baytlık veri
id_value = random.randint(0, 65535)

# Büyük paketi oluştur
packet = IP(dst=target_ip, id=id_value)/ICMP()/payload

# Paketi fragmentlere ayır
fragments = fragment(packet, fragsize=1400)

# Fragmentleri sırayla gönder
for i, frag in enumerate(fragments):
    send(frag)
    print(f"[+] Fragment {i+1} gönderildi: {frag.summary()}")
