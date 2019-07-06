from socket import *

clientSock = socket(AF_INET, SOCK_STREAM) #소켓의 종류와 유형 선언, 가장 일반적인 모습
clientSock.connect(("127.0.0.1", 9999))
clientSock.sendall("안녕!".encode(encoding="utf-8", errors="strict"))
clientSock.close()

