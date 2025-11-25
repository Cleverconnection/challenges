"""Gerador de PCAP sintético para o desafio Weaving the Tree.

Execute em um ambiente local com Scapy instalado para produzir o arquivo
"weaving_the_tree.pcap" contendo dois BPDUs representando a eleição de root.
"""
from scapy.all import Dot3, LLC, Raw, wrpcap


def build_packets():
    """Monta uma pequena sequência de quadros BPDU."""
    bpdu1 = Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:55") / LLC(dsap=0x42, ssap=0x42) / Raw(
        load=b"BPDU Root=32768.00:11:22:33:44:55 Cost=0"
    )
    bpdu2 = Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:66") / LLC(dsap=0x42, ssap=0x42) / Raw(
        load=b"BPDU Root=32768.00:11:22:33:44:66 Cost=4"
    )
    return [bpdu1, bpdu2]


def main():
    packets = build_packets()
    wrpcap("weaving_the_tree.pcap", packets)
    print("✅ weaving_the_tree.pcap criado com 2 BPDUs STP")


if __name__ == "__main__":
    main()
