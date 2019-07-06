import threading, time

g_count = 0 #복수의 스레드에서 공유 될 변수
lock = threading.Lock()

def threadCount(id, count):
    global g_count
    for i in range(count):
        lock.acquire()
        print("id %s ==> count: %s g_count:%s" %(id, i, g_count))
        g_count = g_count + 1
        lock.release()
        
for i in range(1, 6):
    threading.Thread(target=threadCount, args=(i, 5)).start()
    
time.sleep(1)

print("final g_count: ", g_count)    
print("Bye")
'''
id 1 ==> count: 0 g_count:0
id 1 ==> count: 1 g_count:1
id 1 ==> count: 2 g_count:2
id 1 ==> count: 3 g_count:3
id 1 ==> count: 4 g_count:4
id 2 ==> count: 0 g_count:5
id 2 ==> count: 1 g_count:6
id 2 ==> count: 2 g_count:7

...

final g_count:  25
Bye
'''