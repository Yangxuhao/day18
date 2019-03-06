import socket

clientTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientTCP.connect(("127.0.0.1",9888))
while True:
    data=input("input:")
    clientTCP.send(data.encode("utf-8"))
    data=clientTCP.recv(1024)
    print(data.decode("utf-8"))
clientTCP.close()