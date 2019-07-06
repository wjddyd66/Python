#스레드 (Thread)

import threading, time

def run(id):
    for i in range(1, 5):
        print("id={}-->{}".format(id, i))
        time.sleep(0.5)
        
# 스레드를 사용하지 않은 경우: 순차적으로 수행
#run(1)
#run(2)

# 스레드를 사용한 경우: 병렬처리
th1 = threading.Thread(target=run, args=("1", ))
th2 = threading.Thread(target=run, args=("2", ))
th1.start()
th2.start()
th1.join()
th2.join()
print("프로그램 종료")
'''
id=1-->1
id=2-->1
id=1-->2
id=2-->2
id=1-->3
id=2-->3
id=2-->4
id=1-->4
프로그램 종료
'''