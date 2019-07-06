from socket import *

clientSock = socket(AF_INET, SOCK_STREAM) #소켓의 종류와 유형 선언, 가장 일반적인 모습
clientSock.connect(("127.0.0.1", 8888))
clientSock.sendall("스승의 은혜는 하늘 같아서 . . .".encode(encoding="utf-8", errors="strict"))
#errors="strict" -> 줘도, 안줘도 된다.

re_message = clientSock.recv(1024).decode()
print("수신자료: ", re_message)

clientSock.close()

