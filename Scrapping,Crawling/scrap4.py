# 뷰티플숲으로 크롤링하기 -> 파이썬에서 가장 많이 사용하는 방법

import requests
from bs4 import BeautifulSoup

def go():
    base_url = "http://www.naver.com/index.html"

    #storing all the information including headers in the variable source code
    source_code = requests.get(base_url)
    print(source_code)

    #sort source code and store only the plaintext
    plain_text = source_code.text
    #print(plain_text)

    #converting plain_text to Beautiful Soup object so the library can sort thru it
    convert_data = BeautifulSoup(plain_text, 'lxml')
    print(type(convert_data)) #BeautifulSoup 객체가 생성된 것을 확인할 수 있다.

    #sorting useful information
    #for link in convert_data.findAll('a', {'class': 'h_notice'}):
    for link in convert_data.findAll('a'): # "a" 태그가 걸려있는 요소들을 전부 읽어들인다.
        href = base_url + link.get('href')  #Building a clickable url
        print(href)                          #displaying href
        
go()

'''
<Response [200]>
<class 'bs4.BeautifulSoup'>
http://www.naver.com/index.html#news_cast
http://www.naver.com/index.html#themecast
http://www.naver.com/index.html#time_square

...

http://www.naver.com/index.html/policy/spamcheck.html
http://www.naver.com/index.htmlhttps://help.naver.com/
http://www.naver.com/index.htmlhttps://www.navercorp.com/
'''