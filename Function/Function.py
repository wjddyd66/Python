#Function

#내장함수: 이미 지정되어있는 함수
import math
print(math.ceil(1.2), math.ceil(1.7)) #2 2 ceil(): 올림
print(math.floor(1.2), math.floor(1.7)) #1 1 floor(): 내림

#사용자 정의함수: def 키워드를 사용하여 정의한다.
def DoFunc1():
    print("DoFunc1 처리")
DoFunc1()    

#파이썬 함수에서 입력 파라미터는 Pass by Assignment에 의해 전달된다. 
#즉, 호출자(Caller)는 입력 파라미터 객체에 대해 레퍼런스를 생성하여 레퍼런스 값을 복사하여 전달
def DoFunc2(arg1, arg2):
    DoFunc3()
    return arg1+arg2

def DoFunc3():
    print("함수가 함수를 호출 가능")
    
aa = DoFunc2(1,2)
print(aa)   
aa = DoFunc2("대한","민국")
print(aa)   
print("DoFunc2의 객체주소: ", id(DoFunc2))
'''
DoFunc1 처리
함수가 함수를 호출 가능
3
함수가 함수를 호출 가능
대한민국
DoFunc2의 객체주소:  2011568618488
'''

#Default Parameter: 입력파라미터 중 호출자가 전달되지 않으면
#Default로 지정된 값을 사용할 수 있다.
def calc(i, j, factor = 1):
    return i * j * factor
 
result = calc(10, 20)
print(result) #200 factor가 1로서 Default값이 들어감

#Named Parameter: Parameter에 이름을 주어서 파라미터의 순서에 상관없이
#값을 줄 수 있다. => 가독성이 높아진다.
def report(name, age, score):
    print(name, score)
 
report(age=10, name="Kim", score=80) #Kim 80

#가변길이 파라미터: 0~N개의 파라미터를 받아들일 수 있는 표현방법
# *: List, **:Dict이다. 

#List 받기
def test_var_args(f_arg, *args):
    print("first normal arg:", f_arg)
    for arg in args:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
'''
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
'''
#Dict 받기
def greet_me(**kwargs):
    print(kwargs.items())
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
        
greet_me(name="yasoob", school="snu")
'''
dict_items([('name', 'yasoob'), ('school', 'snu')])
name = yasoob
school = snu
'''

#변수의 생존범위: Scope Rule
#변수 영역 및 접근 순서: 1) Local 2)Enclosing Function 3) Global 4) Built-in
a=10; b=20; c=30
print("실행1) a:{}, b:{}, c:{}".format(a, b, c))
def func1():
    a=40
    b=50
    def func2():
            global c
            nonlocal b
            print("실행2) a:{}, b:{}, c:{}".format(a, b, c))   
            c=60
            b=70
    func2()
    print("실행3) a:{}, b:{}, c:{}".format(a, b, c))   
func1()
print("실행4) a:{}, b:{}, c:{}".format(a, b, c))  
'''
실행1) a:10, b:20, c:30
실행2) a:40, b:50, c:30
실행3) a:40, b:70, c:60
실행4) a:10, b:20, c:60
'''