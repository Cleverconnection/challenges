FROM debian:11
RUN apt-get update && apt-get install -y bridge-utils tcpdump iproute2 && \
    brctl addbr br0 && brctl stp br0 on && ip link set br0 up && \
    echo "Execute: tcpdump -i br0 ether proto 0x0026 -vvv"
CMD ["/bin/bash"]
