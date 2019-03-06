import socket
import time
udpsever=udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpsever.bind(("127.0.0.1",8848))
while True:
    data,addr=udpsever.recvfrom(1024)
    print(addr,data)
    sendata=(data.decode("utf-8")+str(time.time())).encode("utf-8")
    udpsever.sendto(sendata,addr)