# 스레드를 이용한 날짜, 시간 출력
import time
from _ast import Or
now = time.localtime()
print(now)

print("현재는 {}년 {}월 {}일 {}시 {}분 {}초".format(now.tm_year, \
        now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, \
        now.tm_sec))

import threading

def showClock():
    now = time.localtime()
    print("현재는 {}년 {}월 {}일 {}시 {}분 {}초".format(now.tm_year, \
        now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, \
        now.tm_sec))
    
def my_run():
    while True: 
        showClock() 
        time.sleep(1)
    
th = threading.Thread(target=my_run)    
th.start()
th.join()

print("Bye^0*")
'''
time.struct_time(tm_year=2019, tm_mon=7, tm_mday=6, tm_hour=17, tm_min=29, tm_sec=7, tm_wday=5, tm_yday=187, tm_isdst=0)
현재는 2019년 7월 6일 17시 29분 7초
현재는 2019년 7월 6일 17시 29분 7초
현재는 2019년 7월 6일 17시 29분 8초
현재는 2019년 7월 6일 17시 29분 9초
현재는 2019년 7월 6일 17시 29분 10초
현재는 2019년 7월 6일 17시 29분 11초
현재는 2019년 7월 6일 17시 29분 12초
현재는 2019년 7월 6일 17시 29분 13초
...
'''