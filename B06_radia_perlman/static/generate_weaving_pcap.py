"""Gerador de PCAP sintético para o desafio Weaving the Tree.

Execute em um ambiente local com Scapy instalado para produzir o arquivo
"weaving_the_tree.pcap" contendo BPDUs de eleição e tráfego de fundo para
simular uma captura realista.
"""
from scapy.all import (
    Dot3,
    LLC,
    Raw,
    wrpcap,
    Ether,
    IP,
    ICMP,
    UDP,
    TCP,
    ARP,
    DNS,
    DNSQR,
)


def build_bpdu_frames():
    """Monta uma sequência de quadros BPDU demonstrando a troca de root."""
    frames = []

    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:55")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=32768.00:11:22:33:44:55 Cost=0 Port=0x8000")
    )
    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:66")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=32768.00:11:22:33:44:55 Cost=4 Port=0x8001")
    )
    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:66")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=32768.00:11:22:33:44:66 Cost=0 Port=0x8001 takeover")
    )
    frames.append(
        Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:55")
        / LLC(dsap=0x42, ssap=0x42)
        / Raw(load=b"BPDU Root=32768.00:11:22:33:44:66 Cost=4 Port=0x8000 blocking")
    )
    return frames


def build_background_noise():
    """Adiciona tráfego genérico para dar contexto à captura."""
    packets = []

    # ARP who-has entre duas pontas do laboratório.
    packets.append(
        Ether(src="00:11:22:aa:bb:01", dst="ff:ff:ff:ff:ff:ff")
        / ARP(op="who-has", psrc="10.0.0.10", pdst="10.0.0.1")
    )

    # Resposta ARP.
    packets.append(
        Ether(src="00:11:22:aa:bb:ff", dst="00:11:22:aa:bb:01")
        / ARP(op="is-at", hwsrc="00:11:22:aa:bb:ff", psrc="10.0.0.1", pdst="10.0.0.10")
    )

    # Consulta DNS simulada para documentação de Radia.
    packets.append(
        Ether(src="00:de:ad:be:ef:01", dst="ff:ff:ff:ff:ff:ff")
        / IP(src="10.0.0.10", dst="10.0.0.53")
        / UDP(sport=53000, dport=53)
        / DNS(rd=1, qd=DNSQR(qname="radia.perlman.lab"))
    )

    # Resposta DNS enxuta.
    packets.append(
        Ether(src="00:de:ad:be:ef:53", dst="00:de:ad:be:ef:01")
        / IP(src="10.0.0.53", dst="10.0.0.10")
        / UDP(sport=53, dport=53000)
        / DNS(rd=1, qr=1, qd=DNSQR(qname="radia.perlman.lab"), ancount=0)
    )

    # Ping de monitoramento.
    packets.append(
        Ether(src="00:24:8c:11:00:01", dst="00:24:8c:11:00:ff")
        / IP(src="10.0.0.20", dst="10.0.0.30")
        / ICMP(type="echo-request", id=0x1111, seq=1)
    )

    # Resposta ICMP.
    packets.append(
        Ether(src="00:24:8c:11:00:ff", dst="00:24:8c:11:00:01")
        / IP(src="10.0.0.30", dst="10.0.0.20")
        / ICMP(type="echo-reply", id=0x1111, seq=1)
    )

    # Fluxo TCP curto em porta administrativa.
    packets.append(
        Ether(src="00:16:3e:01:10:01", dst="00:16:3e:01:10:ff")
        / IP(src="10.0.0.40", dst="10.0.0.41")
        / TCP(sport=2200, dport=80, flags="S", seq=1000)
    )
    packets.append(
        Ether(src="00:16:3e:01:10:ff", dst="00:16:3e:01:10:01")
        / IP(src="10.0.0.41", dst="10.0.0.40")
        / TCP(sport=80, dport=2200, flags="SA", seq=5000, ack=1001)
    )
    packets.append(
        Ether(src="00:16:3e:01:10:01", dst="00:16:3e:01:10:ff")
        / IP(src="10.0.0.40", dst="10.0.0.41")
        / TCP(sport=2200, dport=80, flags="A", seq=1001, ack=5001)
        / Raw(load=b"GET /radia-status HTTP/1.1\r\nHost: lab\r\n\r\n")
    )

    return packets


def main():
    packets = []
    packets.extend(build_bpdu_frames())
    packets.extend(build_background_noise())
    wrpcap("weaving_the_tree.pcap", packets)
    print(
        "✅ weaving_the_tree.pcap criado com 4 BPDUs STP e tráfego ARP/DNS/ICMP/TCP para análise contextual"
    )


if __name__ == "__main__":
    main()
