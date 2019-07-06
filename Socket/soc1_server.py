#<컴퓨터 간 접속상태 확인을 위해 1회 접속처리>
from socket import *

# TCP/IP socket
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(("127.0.0.1", 9999))
serverSock.listen(1) #리스너 설정 1~5
print("server service 중 ...")

conn, addr = serverSock.accept()
print("client address: ", addr)
print("from client message: ", conn.recv(1024).decode())

conn.close()
serverSock.close()
