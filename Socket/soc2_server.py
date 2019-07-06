#echo server 사용
import socket
import sys

HOST = ""
PORT = 8888

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serverSock.bind((HOST, PORT))
    #HOST에 IP를 별도로 주지 않는다면 동적이 된다.
    print("서버 서비스 중입니다.")
    serverSock.listen(5) # 동시 최대 접속 수=5
    
    #서버는 무한루프에 빠져있다.
    while True:
        conn, addr = serverSock.accept()
        print("client info: ", addr[0], addr[1])
        #IP주소와 포트번호를 따로 받겠다는 의미
        print("from client message: ", conn.recv(1024).decode())
        
        #송신
        conn.send(("from server: " + str(addr[1]) + \
                   "너도 잘 지내라").encode("utf-8"))
                    # \ -> 명령이 계속 이어진다는 의미
    
except Exception as e:
    print("err: ", e)
    sys.exit() #프로그램 강제종료
finally:
    serverSock.close()    
    conn.close()
