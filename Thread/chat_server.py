# 멀티 채팅 프로그램용 서버
import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(("127.0.0.1", 7777))
ss.listen(5) 
print("채팅 서비스를 시작합니다.")

users=[] #유저를 담는 리스트

def ChatUser(conn):
    name = conn.recv(1024)
    data = "^_^ "+name.decode("utf-8")+"님 입장^^"
    print(data)
    
    try:
        for p in users:
            p.send(data.encode("utf-8"))
            
        while True:
            msg = conn.recv(1024)    
            data = name.decode("utf-8") + "님 메시지: " + msg.decode("utf-8")
            print("수신 결과: ", data)
            for p in users:
                p.send(data.encode("utf-8"))
    
    except:
        users.remove(conn)
        data = "ㅠ_ㅠ"+name.decode("utf-8")+"님 퇴장"
        print(data)
        if users:
            for p in users:
                p.send(data.encode("utf-8"))
        else: 
            print("EXIT")
            
while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target=ChatUser, args=(conn,))
    th.start()
    
                
                
        
