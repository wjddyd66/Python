#Class
def func():
    print("함수입니다.")
    
class TestClass:
    aa = 1 #멤버변수 (전역)
    
    def __init__(self):
        print("생성자")
        
    def __del__(self):
        print("소멸자")    
        
    def myMethod(self):
        name = "tom" #지역변수
        print(name)
        print(self.aa) #클래스 내의 멤버를 호출할 때는 self를 통해 호출.
        
    def abc(self):    
        self.myMethod()
        
test = TestClass() #생성자 호출(init 호출). 객체(instance) 생성
print(test.aa)
test.myMethod() #Bound Method Call
#객체변수가 알아서 아규먼트를 타고 들어간다.

print()
print(TestClass.aa) #원형클래스의 멤버 호출
TestClass.myMethod(test) #Unbound Method Call
#바운드 메소드 콜과는 다르게, 객체변수를 아규먼트로 직접 주어야한다.

print()
print(type(1))
print(type(1.5))
print(type(test)) #type: TestClass

print()
print(id(TestClass))
print(id(test))
'''
생성자
1
tom
1

1
tom
1

<class 'int'>
<class 'float'>
<class '__main__.TestClass'>

1856097037400
1856129974512
소멸자
'''

'''
인스턴스, 원형클래스, Method Call
'''

#Class Car 선언
class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def showData(self):
        km = "킬로미터" 
        msg = "속도: " + str(self.speed) +km
        return msg

#Car1 인스턴스 생성
car1 = Car("tom", 10)
#Car1 속성 추가
car1.color="검정"

print(car1.handle, " ", car1.name, " ", car1.speed) #0   tom   10
print("car1.color: ", car1.color) #car1.color:  검정

#Car2 인스턴스 생성
car2 = Car("jamez", 20)
print(car2.handle, " ", car2.name, " ", car2.speed) #0   jamez   20

print("주소: ", Car, car1, car2)
print("주소: ", id(Car), id(car1), id(car2))
print("각 객체멤버: ", car1.__dict__)
print("각 객체멤버: ", car2.__dict__)
'''
주소:  <class '__main__.Car'> <__main__.Car object at 0x00000218F82C3278> <__main__.Car object at 0x00000218F82C3240>
주소:  2306231774296 2306266116728 2306266116672
각 객체멤버:  {'name': 'tom', 'speed': 10, 'color': '검정'}
각 객체멤버:  {'name': 'jamez', 'speed': 20}
'''

#Bound Method Call
print(car1.showData()) #속도: 10킬로미터
#Unbound Method Call
print(Car.showData(car1)) #속도: 10킬로미터


#상속
from pack.PohamCar import PohamCar

tom = PohamCar("tom")
tom.TurnHandle(20)
print(tom.ownerName+"의 회전량은 "+tom.turnShow+str(tom.handle.quantity))
tom.TurnHandle(-30)
print(tom.ownerName+"의 회전량은 "+tom.turnShow+str(tom.handle.quantity))
oscar = PohamCar("oscar")
oscar.TurnHandle(0)
print(oscar.ownerName+"의 회전량은 "+oscar.turnShow+str(oscar.handle.quantity))
'''
tom의 회전량은 우회전20
tom의 회전량은 좌회전-30
oscar의 회전량은 직진0
'''

#Method 오버로딩
class Animal():

    def __init__(self, name):
        self.name = name

    def walk(self):
        print('{} walk'.format(self.name))

    def eat(self):
        print('{} eat'.format(self.name))

    def greet(self):
        print('{} greet'.format(self.name))

class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def bark(self):
        print('{} bark to you for greeting'.format(self.name))

    def greet(self): # Animal Method 오버로딩
        self.bark()


animal = Animal('my_animal') # Animal 인스턴스 생성
my_dog = Dog('Puppy') # Dog 인스턴스를 생성
animal.greet() # Animal 인스턴스의 greet 메소드를 호출
my_dog.greet() # Dog 인스턴스의 greet 메소드를 호출

animal.walk() # Animal 인스턴스의 walk 메소드를 호출
my_dog.walk() # Dog 인스턴스의 walk 메소드를 호출

'''
my_animal greet
Puppy bark to you for greeting
my_animal walk
Puppy walk
'''

#소멸자