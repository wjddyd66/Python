'''
Module: 함수나 변수 또는 클래스를 모아놓은 파일이다.
소스코드의 재사용이 가능하게 하며, 코드를 하나의 이름 공간으로 구분하고 관리 가능하다.
파이썬은 모듈단위로 저장되며, 확장자 .py를 가진다.
모듈의 종류
1. 표준모듈(이미 저장되어있는 Module)
2. 사용자 모듈(사용자가 재사용을 목적으로 만든 Module)
3. 제3자 모듈(제 3자가 재사용을 목적으로 만든 Module)
제 3자Module은 Python > Lib > site-package에 파일을 삽입해야 한다.
'''

'''
표준 모듈
1. import 하여 불러오기
2. from Module면 import 멤버명: 모듈명을 부르지 않고 바로 멤버 불러 사용 가능
3. 
'''
import sys
print(sys.path) #현재 모듈의 경로를 보여준다. ['C:\\Work\\pysou\\Python\\pack', ...

import math
print(math.pi) #파이값 출력 3.141592653589793
print(math.sin(math.radians(30))) #sin30˚의 값 0.49999999999999994

'''
사용자 모듈
mymod 라는 이름의 외부 Module 호출
'''
kor = 100
print("kor: ", kor)

import pack.mymod
print(pack.mymod.num)

list1 = [1, 3]
list2 = [2, 4, 5]
pack.mymod.ListPrint(list1, list2)
pack.mymod.Kbs()

def abc():
    print("응용프로그램 시작")
    
if __name__ == "__main__":
    print("여기가 최상위 모듈입니다.")
    abc()
'''
대한민국 대표방송
현재 모듈명:  pack.mymod
여기가 최상위 모듈입니다.
응용프로그램 시작
'''

#제 3자 Module(pygame)
import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("안녕")

windowSurface.fill((255,255,255))
pygame.display.update()

pygame.draw.circle(windowSurface, (255, 255, 0), (250, 50), 50, 0)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()