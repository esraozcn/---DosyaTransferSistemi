
from scapy.all import sniff, IP, Raw
from collections import defaultdict

# Gelen fragmentler burada tutulacak
fragments = defaultdict(dict)

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        ident = ip_layer.id
        offset = ip_layer.frag
        mf_flag = ip_layer.flags.MF

        if ident not in fragments:
            fragments[ident] = {}

        fragments[ident][offset] = bytes(packet[Raw]) if Raw in packet else b''

        print(f"Fragment alındı: ID={ident}, Offset={offset}, MF={mf_flag}")

        if not mf_flag:
            reassemble_packet(ident)

def reassemble_packet(ident):
    parts = fragments[ident]
    data = b''.join([parts[k] for k in sorted(parts)])
    print(f"[✓] Paket ID={ident} başarıyla birleştirildi. Uzunluk: {len(data)} bayt")

# ICMP paketleri filtreleniyor
print("Fragmentleri dinliyorum...")
sniff(filter="ip", prn=packet_callback, store=0, timeout=20)

