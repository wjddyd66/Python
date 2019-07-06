import urllib.request
import xml.etree.ElementTree as et
# 웹 이미지 읽기
url = "https://github.com/wjddyd66/wjddyd66.github.io/blob/master/static/img/programmer.png"
save_name = "test1.png"

#다운로드
urllib.request.urlretrieve(url, save_name)
print("다운로드 후 저장 성공")

#다운로드2
save_name = "test2.png"
imsi = urllib.request.urlopen(url).read()

with open(save_name, mode="wb") as f:
    f.write(imsi)
    print("저장완료")