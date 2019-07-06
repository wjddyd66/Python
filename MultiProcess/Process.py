# Process: Pool과는 달리, 하나의 프로세스를 하나의 함수에 할당해주는 방식 (건너건너X)

import os
from multiprocessing import Process

def func():
    print("멀티 처리를 하고 싶은 내용 기술")
    
def doubler(num):
    result = num + 10
    func()
    proc = os.getpid()
    print("num:{}, result:{}, process:{}".format(num, result, proc))    
    
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    procs = []    
    
    for i, number in enumerate(nums):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()
        
    for proc in procs:
        proc.join()

'''
num:1, result:11, process:8160
num:5, result:15, process:12584
멀티 처리를 하고 싶은 내용 기술
num:2, result:12, process:4952
멀티 처리를 하고 싶은 내용 기술
num:3, result:13, process:13444
멀티 처리를 하고 싶은 내용 기술
num:4, result:14, process:32
'''