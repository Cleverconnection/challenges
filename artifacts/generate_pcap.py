from scapy.all import *
pkts=[]
# Root bridge BPDU
bpdu1 = Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:55")/LLC(dsap=0x42, ssap=0x42)/Raw(load=b"BPDU Root=32768.00:11:22:33:44:55 Cost=0")
# Bridge secundária assume root
bpdu2 = Dot3(dst="01:80:C2:00:00:00", src="00:11:22:33:44:66")/LLC(dsap=0x42, ssap=0x42)/Raw(load=b"BPDU Root=32768.00:11:22:33:44:66 Cost=4")
pkts.extend([bpdu1,bpdu2])
wrpcap("weaving_the_tree.pcap", pkts)
print("✅ weaving_the_tree.pcap criado com 2 BPDUs STP")
