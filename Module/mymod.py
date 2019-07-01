#사용자 모듈 선언
num = 123
def ListPrint(*ar):
    print(ar)
    
def Kbs():
    print("대한민국 대표방송")
    print("현재 모듈명: ", __name__)
    if __name__ == "__main__":
        print("kbs만세")
    
def Mbc():
    print("문화방송")