import socket
import os
udpsever=udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpsever.bind(("127.0.0.1",8848))
while True:
    data,addr=udpsever.recvfrom(1024)
    print(addr,data)
    os.system(data.decode("utf-8"))