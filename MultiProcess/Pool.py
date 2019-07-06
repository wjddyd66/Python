# <Multi Processing을 지원하는 'Pool', 'Process'로 멀티태스킹 구현>
from multiprocessing import Pool
import time
import os

def func(x):
    print("값", x, "에 대한 작업 pid=", os.getpid())
    time.sleep(1)
    return x * x

if __name__ == "__main__":
    p = Pool(3)
    startTime = int(time.time())
    """
    for i in range(0, 10):
        print(func(i))
    """    
    print(p.map(func, range(0, 10)))
    
    endTime = int(time.time())
    print("총 작업시간: ", (endTime - startTime))
    
'''
값 0 에 대한 작업 pid= 7656
값 1 에 대한 작업 pid= 13364
값 2 에 대한 작업 pid= 9436
값 3 에 대한 작업 pid= 7656
값 4 에 대한 작업 pid= 13364
값 5 에 대한 작업 pid= 9436
값 6 에 대한 작업 pid= 7656
값 7 에 대한 작업 pid= 13364
값 8 에 대한 작업 pid= 9436
값 9 에 대한 작업 pid= 7656
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
총 작업시간:  4 
'''