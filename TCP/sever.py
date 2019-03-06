import socket
import time
SeverTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SeverTCP.bind(("127.0.0.1",9888))
SeverTCP.listen(5)

clientsock,clientaddr=SeverTCP.accept()
while True:
    data=clientsock.recv(1024)
    print("receive"+data.decode("utf-8"))
    senddata=(data.decode("utf-8")+str(time.time())).encode("utf-8")
    clientsock.send(senddata)



