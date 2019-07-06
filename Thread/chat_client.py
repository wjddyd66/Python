# 멀티 채팅 프로그램용 서버
import socket
import threading
import sys

def handle(socket):
    while True:
        data = socket.recv(1024)
        if not data:continue
        print(data)

sys.stdout.flush() #flush(): 깨끗하게 비운다.

name = input("채팅에 사용 할 아이디를 입력하세요: ")
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(("127.0.0.1", 7777))
cs.send(name.encode("utf-8"))

th = threading.Thread(target=handle, args=(cs,))
th.start()

while True:
    msg = input()
    sys.stdout.flush()
    if not msg:continue
    cs.send(msg.encode("utf-8"))
    
cs.close()    
