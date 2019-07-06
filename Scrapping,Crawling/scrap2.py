# 기상청 날씨정보 스크래핑 
import urllib.request
import xml.etree.ElementTree as et

try:
    webdata = urllib.request.urlopen("http://www.kma.go.kr/XML/weather/sfc_web_map.xml")
    #print(webdata)
    webxml = webdata.read() #binary 데이터로 읽어온다.
    webxml = webxml.strip().decode()
    # 바이너리를 문자열로 변환하는 작업이 필요하다.
    # 정해져있는 틀이기 때문에 항상 이런 식의 작업을 반복하게 될 것이다.
    #print(webxml)
    webdata.close()
    
    with open("ftest.xml", mode="w", encoding="utf-8") as f:
        f.write(webxml)
    
except Exception as e:
    print("err: ", e)
    
print("읽기 성공")

xmlfile = et.parse("ftest.xml")    
root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)

children = root.findall("{current}weather")
print(children)

for i in children:
    y = i.get("year")
    m = i.get("month")
    d = i.get("day")
    h = i.get("hour")
    print(str(y)+"년 "+str(m)+"월"+str(d)+"일"+str(h)+"시 현재")
    
datas = []
for child in root:
    print(child.tag)
    for i in child:
        #print(i.tag)
        local_name =i.text
        re_ta = i.get("ta")
        re_desc = i.get("desc")
        datas+=[[local_name, re_ta, re_desc]]
        print(local_name+", 온도: "+str(re_ta)+" "+re_desc) 
print("건 수: ", len(datas))

print("*"*50)
'''
읽기 성공
{current}current
{current}weather
[<Element '{current}weather' at 0x000002837D3EE6D8>]
2019년 07월06일18시 현재
{current}weather
속초, 온도: 24.0 구름많음
북춘천, 온도: 30.0 맑음

...

산청, 온도: 29.8 구름조금
거제, 온도: 25.8 맑음
남해, 온도: 28.6 구름조금
건 수:  96
**************************************************
'''
