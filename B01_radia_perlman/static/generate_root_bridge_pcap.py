"""Gerador de PCAP para o desafio Guardiã das Árvores Digitais.

Execute em um ambiente com Scapy instalado para criar o arquivo
"guardian_tree.pcap" contendo BPDUs e tráfego de fundo simulando
uma coleta em campo.
"""
from scapy.all import (
    Dot3,
    LLC,
    Raw,
    wrpcap,
    Ether,
    ARP,
    IP,
    UDP,
    TCP,
    ICMP,
    DNS,
    DNSQR,
)


def build_spanning_tree_sequence():
    """Constrói BPDUs que contam a história do root bridge legítimo."""
    frames = []

    # Estado inicial: alpha mantém a raiz.
    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:55")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=4096.00:11:22:33:44:55 Cost=0 Port=0x8000")
    )

    # Bridge delta anuncia custo maior, permanece não raiz.
    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:99")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=4096.00:11:22:33:44:55 Cost=4 Port=0x8002")
    )

    # Evento de tensão: beta tenta concorrer com menor MAC.
    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:AA:BB:CC")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=4096.00:11:22:AA:BB:CC Cost=0 Port=0x8003 challenge")
    )

    # Alpha responde mantendo prioridade mais baixa.
    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:55")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=4096.00:11:22:33:44:55 Cost=0 Port=0x8000 defend")
    )

    # Beta recua e informa estado bloqueado para o enlace redundante.
    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:AA:BB:CC")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=4096.00:11:22:33:44:55 Cost=4 Port=0x8003 blocking")
    )

    return frames


def build_background_noise():
    """Adiciona ruído comum de rede para tornar a captura realista."""
    packets = []

    # Conversa ARP entre hosts de laboratório.
    packets.append(
        Ether(src="00:16:3e:10:00:01", dst="ff:ff:ff:ff:ff:ff")
        / ARP(op="who-has", psrc="10.1.0.10", pdst="10.1.0.1")
    )
    packets.append(
        Ether(src="00:16:3e:10:00:aa", dst="00:16:3e:10:00:01")
        / ARP(op="is-at", hwsrc="00:16:3e:10:00:aa", psrc="10.1.0.1", pdst="10.1.0.10")
    )

    # Consulta DNS para acervo histórico de Radia.
    packets.append(
        Ether(src="00:24:8c:20:00:01", dst="ff:ff:ff:ff:ff:ff")
        / IP(src="10.1.0.10", dst="10.1.0.53")
        / UDP(sport=52000, dport=53)
        / DNS(rd=1, qd=DNSQR(qname="radia.perlman.archive"))
    )
    packets.append(
        Ether(src="00:24:8c:20:00:53", dst="00:24:8c:20:00:01")
        / IP(src="10.1.0.53", dst="10.1.0.10")
        / UDP(sport=53, dport=52000)
        / DNS(rd=1, qr=1, qd=DNSQR(qname="radia.perlman.archive"), ancount=0)
    )

    # Batida ICMP.
    packets.append(
        Ether(src="00:11:5c:30:00:01", dst="00:11:5c:30:00:ff")
        / IP(src="10.1.0.20", dst="10.1.0.30")
        / ICMP(type="echo-request", id=0x2222, seq=1)
    )
    packets.append(
        Ether(src="00:11:5c:30:00:ff", dst="00:11:5c:30:00:01")
        / IP(src="10.1.0.30", dst="10.1.0.20")
        / ICMP(type="echo-reply", id=0x2222, seq=1)
    )

    # Handshake TCP curto representando consulta ao painel.
    packets.append(
        Ether(src="00:ff:ee:40:00:01", dst="00:ff:ee:40:00:ff")
        / IP(src="10.1.0.40", dst="10.1.0.50")
        / TCP(sport=8080, dport=443, flags="S", seq=100)
    )
    packets.append(
        Ether(src="00:ff:ee:40:00:ff", dst="00:ff:ee:40:00:01")
        / IP(src="10.1.0.50", dst="10.1.0.40")
        / TCP(sport=443, dport=8080, flags="SA", seq=500, ack=101)
    )
    packets.append(
        Ether(src="00:ff:ee:40:00:01", dst="00:ff:ee:40:00:ff")
        / IP(src="10.1.0.40", dst="10.1.0.50")
        / TCP(sport=8080, dport=443, flags="A", seq=101, ack=501)
        / Raw(load=b"GET /root-bridge-status HTTP/1.1\r\nHost: guardian\r\n\r\n")
    )

    return packets


def main():
    packets = []
    packets.extend(build_spanning_tree_sequence())
    packets.extend(build_background_noise())
    wrpcap("guardian_tree.pcap", packets)
    print(
        "✅ guardian_tree.pcap criado com 5 BPDUs e ruído ARP/DNS/ICMP/TCP para estudo do root bridge"
    )


if __name__ == "__main__":
    main()
