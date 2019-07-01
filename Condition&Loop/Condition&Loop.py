#조건문
var=1
if var>=3:
    print("크구나")
    if var > 1:
        print("크네...")
else: 
    print("작네...")
#작네...

jumsu=int(input("점수입력: "))
if jumsu>=90:
    print("우수")
elif jumsu>=70:
    print("보통")
else:
    print("미달")


if 90<=jumsu<=100:
    print("우수2")
elif 70<=jumsu<90:
    print("보통2")
else:
    print("미달2")
   
#자바에서는  90<=jumsu<=100가 불가능 하지만, Python은 가능하다
'''
input(): 값을 키보드로서 입력받는 함수
점수입력: 90
우수
우수2
'''

#반복문
#While
colors=['red', 'green', 'blue']
a=0

while a<len(colors):
    print(colors[a], end=' ')
    a+=1
print()
print(colors, len(colors))    

while colors:
    print(colors.pop()) #pop(): 추출하여 값을 삭제한다.
print(colors, len(colors))      

'''
red green blue 
['red', 'green', 'blue'] 3
blue
green
red
[] 0
'''

#for 구문 - 구구단 2,3단 출력
for n in [2,3]:
    print("--{}단--".format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(n, i, n*i))
'''
--2단--
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
--3단--
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
'''
        
#for 구문 - 구구단 range()사용
for i in range(2,10):
    for j in range(1,10):
        print("{} * {} = {} ".format(i, j, i * j), end="\n")

