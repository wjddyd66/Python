#기본 데이터 타입
a=10;
print(type(a),a);
a=10.25
print(type(a),a);
a=True;
print(type(a),a);
a=None;
print(type(a),a);
a="10"
print(type(a),a);
#Python은 대소문자를 구별한다.
A=5;
print(type(a),a,type(A),A);
#복소수
a=10+5j;
print("실수부분은 ",a.real,"허수부분은 ",a.imag)
'''
결과
<class 'int'> 10
<class 'float'> 10.25
<class 'bool'> True
<class 'NoneType'> None
<class 'str'> 10
<class 'str'> 10 <class 'int'> 5
실수부분은  10.0 허수부분은  5.0
'''

#문자열 포멧팅
ss="이름: %s 나이: %d"%("황정용",26)
print(ss);#이름: 황정용 나이: 26

#문자열 메소드
#str.join()
s = ','.join(['황정용',"26",'Programmer']);
# ',': 문자열을 합칠때 넣어주는 문자열
print(s);#황정용,26,Programmer

#str.split()
s = '황정용,26,Programmer'.split(',');
print(type(s),s); #<class 'list'> ['황정용', '26', 'Programmer']

#str.partition()
s1,s2,s3 = '황정용,26,Programmer'.partition(',');
print(type(s1),s1);
print(type(s2),s2);
print(type(s3),s3);
'''
<class 'str'> 황정용
<class 'str'> ,
<class 'str'> 26,Programmer
'''

#str.format()
s="Name:{0},Age:{1},Job:{2}".format('황정용','26','Programmer')
print(s);#Name:황정용,Age:26,Job:Programmer

#연산자

#산술 연산자
a=5;
print(a%2); #1
print(a/2); #2.5

#비교 연산자
if a ==5:
    print('참');
else:
    print('거짓');
#참

#할당 연산자
a *=10
print(a)#50

#논리 연산자
if a==50 and a<100:
    print('참');
else:
    print('거짓');
#참

#Bitwise 연산자
a=10;
b=11;
c = a&b; #&: and, |: or
d = a^b; #^: XOR
print(c) # 10
print(d) # 1

#멤버쉽 연산자
a = [1,2,3,4]
b= 1 in a
print(b) # True

#Identity 연산자
a = "ABC"
b=a;
print(a is b);#True
