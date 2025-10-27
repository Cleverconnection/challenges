FROM debian:11
RUN apt-get update && apt-get install -y bridge-utils tcpdump net-tools iproute2 && \
  brctl addbr br0 && brctl addbr br1 && \
  brctl addif br0 eth0 && brctl addif br1 eth1 && \
  brctl stp br0 on && brctl stp br1 on && \
  echo "Two bridges active. Connect eth0<->eth1 to test loop recovery."
CMD ["/bin/bash"]
