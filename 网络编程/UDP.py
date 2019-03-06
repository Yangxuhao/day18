import socket

udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect(("127.0.0.1",8080))
udp.send(str)
