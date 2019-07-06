#스레드를 상속받은 클래스
import threading, time, sys

class MyThread(threading.Thread):
    def run(self):
        for i in range(1, 5):
            print("id:{}==>{}".format(self.getName(), i))
            time.sleep(0.1)
            
ths = []
for i in range(2):
    th = MyThread()
    th.start()            
    ths.append(th)
    
for th in ths:
    th.join()
    
print("Bye")

'''
id:Thread-1==>1
id:Thread-2==>1
id:Thread-1==>2
id:Thread-2==>2
id:Thread-1==>3
id:Thread-2==>3
id:Thread-1==>4
id:Thread-2==>4
Bye
'''