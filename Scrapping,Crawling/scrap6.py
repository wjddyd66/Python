from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def processFunc(url):
    try:
        html = urlopen(url)
        print(html)
    except Exception as e:
        return None    
    
    try: 
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
        print("연습1 : 자식과 자손태그의 차이 -----")
        #for child in bsObj.find("table", {"id":"giftList"}).children:
        for child in bsObj.find("table", {"id":"giftList"}).descendants:
            # children과 descendants는 차이가 있다.
            print("child: ", child)
        
               
        print("\n연습2 : 형제태그 -----")    
        for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
            print(sibling)
            
        print("\n연습3 : 부모(이전) 태그 -----")    
        print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
            
    except Exception as err:
        return None    
    
    return title

title = processFunc("https://www.pythonscraping.com/pages/page3.html")
if title == None:
    print("처리 실패")
    
else:
    print(title)    