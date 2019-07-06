from bs4 import BeautifulSoup

html_data = """
<html>
<body>
<h1>제목 태그</h1>
<p>뷰티플숲으로 읽기</p>
<p>원하는 자료 추출</p>
</body>
</html>
"""
print(type(html_data)) #<class 'str'>
soup = BeautifulSoup(html_data, "html.parser")
print(type(soup)) # <class 'bs4.BeautifulSoup'>
print()

h1 = soup.html.body.h1
print("h1: ", h1.string) #h1:  제목 태그
p1 = soup.html.body.p
print("p1: ", p1.string) #p1:  뷰티플숲으로 읽기
# 최초의 p 태그를 가져온다.
p2 = p1.next_sibling.next_sibling
print("p2: ", p2.string) # p2:  원하는 자료 추출

#
print("\n ▷ find() 메소드 사용하기 -----")
html_data2 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>뷰티플숲으로 읽기</p>
<p attr="my">원하는 자료 추출</p>
</body>
</html>
"""
soup2 = BeautifulSoup(html_data2, "html.parser")
print("title: "+soup2.find(id="title").string)
print("my: "+soup2.find(attr="my").string)

'''
 ▷ find() 메소드 사용하기 -----
title: 제목 태그
my: 원하는 자료 추출
'''

#
print("\n ▷ find_all() 메소드 사용하기 -----")
html_data3 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>뷰티플숲으로 읽기</p>
<p attr="my">원하는 자료 추출</p>
<div>
    <a href="http://www.naver.com">naver</a><br>
    <a href="http://www.daum.net">daum</a>
</div>
</body>
</html>
"""
soup3 = BeautifulSoup(html_data3, "html.parser")
#print(soup3.prettify()) #html 모양처럼 보기에 편하게 만들어주는 함수
links = soup3.find_all("a") #"a"태그를 전부 잡아온다.
print(links)
for i in links:
    href = i.attrs["href"]
    text = i.string
    print(href, ", ", text)

'''
 ▷ find_all() 메소드 사용하기 -----
[<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>]
http://www.naver.com ,  naver
http://www.daum.net ,  daum
'''

print("\n ▷ 정규표현식 사용하기 -----")
import re
links2 = soup3.find_all(href=re.compile(r"^http://"))
print(links2)
for i in links2:
    print(i.attrs["href"])
    
print()
print(soup3.find_all("p"))    
print(soup3.find_all(["p", "h1"])) # 말 그대로 다 가져온다.
aa = soup3.find_all(string=["제목 태그", "원하는 자료 추출"])
print(aa[0])
print(aa[1])

'''
 ▷ 정규표현식 사용하기 -----
[<a href="http://www.naver.com">naver</a>, <a href="http://www.daum.net">daum</a>]
http://www.naver.com
http://www.daum.net

[<p>뷰티플숲으로 읽기</p>, <p attr="my">원하는 자료 추출</p>]
[<h1 id="title">제목 태그</h1>, <p>뷰티플숲으로 읽기</p>, <p attr="my">원하는 자료 추출</p>]
제목 태그
원하는 자료 추출
'''

print("\n ▷ CSS selector 사용하기 -----")
html_data4 = """
<html>
<body>
    <div id="hello">
        <a href="http://www.naver.com">naver</a><br>
        <ul class="world">
            <li>안녕</li>
            <li>반가워</li>
        </ul>
    </div>
    <div>
        good
    </div>
</body>
</html>
"""
soup4 = BeautifulSoup(html_data4, "lxml")
a = soup4.select_one("div#hello > a").string
#div 태그 중 id=hello인 요소의 직계자손 중 a 태그를 가진 요소를 추출한다.
print("a: ", a)
uls = soup4.select("div#hello > ul.world > li")
for i in uls:
    print("li: ", i.string)

'''
 ▷ CSS selector 사용하기 -----
a:  naver
li:  안녕
li:  반가워
'''
