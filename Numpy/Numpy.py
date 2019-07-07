import numpy as np

ss = ['tom', 'james', 'oscar']
print(ss,' ', type(ss))
ss2 = np.array(ss)
print(ss2,' ', type(ss2))

li = list(range(1, 11))
print(li)
print(id(li[0]), id(li[1]))

for i in li:
    print(i * 10, end = " ")
    
num_arr = np.array(li)
print(num_arr)
print(id(num_arr[0]), id(num_arr[1]))
print(num_arr * 10)

for i in li:
    print(i * 10, end = " ")
    
num_arr = np.array(li)
print(num_arr)
print(id(num_arr[0]), id(num_arr[1]))
print(num_arr * 10)

a = np.array([1,2,3])
print(a)
print(type(a))
print(a.dtype)
print(a.shape)
print(a.ndim)
print(a.size)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)

a = np.zeros((2,2))
print(a)
b = np.ones((2,2))
print(b)
c = np.full((2,2), 7)
print(c)
d = np.eye(3)
print(d)

np.random.seed(0)
print(np.random.rand(5))
print(np.random.randn(5))

f = {i:np.random.randn() for i in range(5)}
print(f)

# Slicing
a = np.array([1,2,3,4,5])
print(a[1:5:2]) # start:end:stack

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[:])
print(a[1:])

# Sub Array
b = a[:2, 1:3]
print(b)
print(b[0, 0])
print(a[0, 1])

b[0,0] = 77
print(b[0, 0])
print(a[0, 1])
print(a)

x = np.array([[1,2],[3,4]])
print(x.dtype)
x = np.array([[1,2],[3,4]], dtype=np.float64)
print(x.dtype)

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[1,2],[3,4]], dtype=np.float64)
z = y.astype(np.int32) # 형변환
print(x,y,z)
print(x.dtype, y.dtype, z.dtype)

print(x+y)
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))
v = np.array([9, 10])
w = np.array([11, 12])
print(v.dot(w))
print(np.dot(v,w))
print(x)
print(v)
print(x.dot(v))
print(np.dot(x,v))

#내장함수
print(x)
print(np.sum(x))
print(np.sum(x, axis=0)) #열에 대한 합
print(np.sum(x, axis=1)) #행에 대한 합
print(np.argmax(x))
print(np.cumsum(x))
print(np.cumprod(x))

names = np.array(["tom","james","tom","oscar"])
names2 = np.array(["tom","page","john"])
print(np.unique(names)) #중복없이
print(np.intersect1d(names, names2)) #교집합
print(np.intersect1d(names, names2, assume_unique=True))
# assume_unique=True -> 중복을 허용하는 옵션
print(np.union1d(names, names2)) #합집합

print(x)
print(x.T)

print(x.transpose())
print(x.swapaxes(0,1))

arr = np.arange(1,16).reshape((3,5))
print(arr)
print(arr.T)

print(np.dot(arr.T, arr))

print(v)
print(v.T)

print(x)
np.save("test1", x) # 바이너리 데이터로 저장
np.savez("test2", x) 
np.savetxt("text3", x) # 텍스트 파일로 저장

mydatas = np.load("test1.npy")
print(mydatas)

mydatas2 = np.loadtxt("text3")
print(mydatas2)

aa = np.eye(3) #단위행렬
print(aa)

bb = np.c_[aa, aa[2]]
print(bb)

cc = np.r_[aa, [aa[2]]]
print(cc)

x = np.array([1,2,3])
y = np.array([4,5,6])
conditionData = np.array([True, False, True])
result = np.where(conditionData, x, y)
print(result)

print("\n")
aa = np.where(x>=2) #인덱스 출력
print(aa)
print(x[aa])

print(np.where(x>=2),"T","F")
print(np.where(x>=2),x,x+100)

print("\n")
testData = np.random.randn(4,4)
print(testData)
print(np.where(testData > 0, 2, testData))
print(np.where(testData > 0, testData, testData * -1))