# XML 자료처리
import xml.etree.ElementTree as et

# 방법1. 파일읽기 -> string 타입으로 가져온다.
xml_f = open("my.xml", mode="r", encoding="utf-8").read()
print(xml_f)
'''
<?xml version="1.0" encoding="UTF-8"?>
<items>
    <item>
        <name id="ks1">홍길동</name>
        <tel>010-111-1111</tel>
        <exam kor="100" eng="90" />
    </item>
    <item>
        <name id="ks2">고길동</name>
        <tel>010-111-2222</tel>
        <exam kor="88" eng="92" />
    </item>
</items>
'''
print(type(xml_f))#<class 'str'>

root = et.fromstring(xml_f) #str -> ElementTree 객체로 변환한다.
# 이렇게 변환하고 나면 ElementTree가 가지고 있는 명령어를 사용할 수 있다.
print(type(root))#<class 'xml.etree.ElementTree.Element'>
print(root.tag)# items
print(len(root)) #items는 2개의 자식을 가지고 있다.
print("*"*50)

# 방법2. ElementTree 객체로 직접 파싱하기 -> XML이 직접 온다.
xmlfile = et.parse("my.xml")
print(type(xmlfile))#<class 'xml.etree.ElementTree.ElementTree'>

root = xmlfile.getroot()
print(root.tag) #루트 태그를 반환한다. -> items
print(root[0].tag) #루트 태그의 0번째 자식을 반환한다. -> item
print(root[0][0].tag) 
#루트 태그의 0번째 자식의 0번째 자식을 반환한다. -> name
print(root[0][1].tag) # -> tel
print(root[0][0].attrib)  # {'id': 'ks1'}
print(root[0][2].attrib) # {'kor': '100', 'eng': '90'}

print(root[0][2].attrib.keys()) #dict_keys(['kor', 'eng'])
print(root[0][2].attrib.values()) #dict_values(['100', '90'])

print(root[0][2].attrib.get("kor")) #100

imsi = list(root[0][2].attrib.values())
print(imsi[0]+", "+imsi[1]) #100, 90

print("*"*50)
myname = root.find("item").find("name").text
#find() 를 이용해 자식의 요소명을 입력해주면 된다.
mytel = root.find("item").find("tel").text
print(myname+", "+mytel)
#홍길동, 010-111-1111

print("\n ▷ 반복처리하기---")
for child in root:
    print(child.tag)
    for child2 in child:
        print(child2.tag, child2.attrib)
'''
 ▷ 반복처리하기---
item
name {'id': 'ks1'}
tel {}
exam {'kor': '100', 'eng': '90'}
item
name {'id': 'ks2'}
tel {}
exam {'kor': '88', 'eng': '92'}
'''       
print("▷ 특정 요소의 속성값 얻기---")
for a in root.iter("exam"):
    print(a.attrib)
'''
▷ 특정 요소의 속성값 얻기---
{'kor': '100', 'eng': '90'}
{'kor': '88', 'eng': '92'}
'''   
print()
children = root.findall("item") #root 밑의 아이템을 전부 찾는다.
# find(), findall() 둘 다 있으니 적절히 활용할 것.
for chi in children:
    re_id =  chi.find("name").get("id")
    re_name =  chi.find("name").text
    re_tel =  chi.find("tel").text
    print(re_id, re_name, re_tel)
'''
ks1 홍길동 010-111-1111
ks2 고길동 010-111-2222
'''