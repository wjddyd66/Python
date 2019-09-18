#!/usr/bin/env python
# coding: utf-8



# -*- coding: utf-8 -*-
import os
from pytube import YouTube
import requests
from tqdm import tqdm
import json
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import subprocess
import threading
import time


def youtube_download(id,destination):
    yt = YouTube(id)
    parent_dir = destination
    yt.streams.filter(subtype='mp4').first().download(parent_dir)
    print('Download Success')


def download_file_from_google_drive(target_url):
    global driver
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
    
    driver.implicitly_wait(3)
    url = target_url
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="drive_main_page"]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]').click()
    
    
    text = driver.find_element_by_xpath('/html/body/div[10]/div[1]/div/div[1]/span').text
    print(text)
    check = file_status_notification(driver)
    if not check:
        print('Downloading Timeout')
    driver.close()


def file_status_notification(driver):
    chk = False
    for i in range(400):
        try:
            time.sleep(3)
            alert = driver.switch_to.alert
            alert.accept()
            print('Download Success')
            chk = True
            break
        except Exception as e:
            pass
    return chk


def vscode_download(id, destination):
    #아래 Code는 CRI or Service차원에서 Chrome창을 띄우지 않고 실행하여 작업하는 옵션이다.
    #아래에 옵션을 사용할 경우 밑의 browser또한 바꾸어야 한다.
    
    
    chrome_options = webdriver.ChromeOptions()
  
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    browser = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
    
    browser.implicitly_wait(2)
    
    url = id
    browser.get(url)
    
    print('Find URL...')
    version=browser.find_element_by_xpath('//*[@id="overviewTab"]/div/table/tbody/tr/td[2]/div[3]/div[4]/div/table/tbody/tr[1]/td[2]/div').text
    unique_identifier=browser.find_element_by_xpath('//*[@id="overviewTab"]/div/table/tbody/tr/td[2]/div[3]/div[4]/div/table/tbody/tr[6]/td[2]').text

    vscode_name = browser.find_element_by_xpath('//*[@id="section-banner"]/div/table/tbody/tr/td[2]/div/h1/span').text
    
    publisher,extensionname = unique_identifier.split('.')
    
    down_link = 'https://{}.gallery.vsassets.io/_apis/public/gallery/publisher/{}/extension/{}/{}/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage'.format(publisher,publisher,extensionname,version)
    
    destination = destination + vscode_name
    print(destination)
    
    #Unable to establish SSL connection error => --no-check-certificate Option 추가
    command=["wget",'--no-check-certificate', down_link, "-O", destination]
    
    print('Downloading...')
    try:
        subprocess.call(command)
        print('Download Success')
    except Exception as e:
        print(e)
        
    browser.close()



def download_images_by_keyword(file_id, destination):
    
    chrome_options = webdriver.ChromeOptions()
  
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
    
    driver.implicitly_wait(3)

    url = 'https://www.naver.com/'
    driver.get(url)

    keyword = file_id
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(keyword)
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(Keys.ENTER)

    driver.find_element
    image_text = driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]/a/span').text
    if image_text == "이미지":
        driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]/a/span').click()
    else:
        driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[3]/a/span').click()
    
    print('Find Keyword...')
    
    for i in range(1000):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
        driver.execute_script("window.scrollBy(0,10000)")
    
    
    link = []
    image_count = 0
    
    for j in range(2,8):
        for i in range(1,50):
            try:
                img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div['+str(j)+']/div['+str(i)+']/a[1]/img')
                image_count = image_count+1
                link.append(img.get_attribute('src'))
            except:
                try:
                    img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[1]/div['+str(j)+']/div['+str(i)+']/a[1]/img')
                    image_count = image_count+1
                    link.append(img.get_attribute('src'))
                except:
                    pass
                
            

        
    count = 0
    print('Downloading...')
    for url in link:
        count+=1
        urllib.request.urlretrieve(url,destination+keyword+'_'+str(count)+'.jpg')
    
    print('Naver', count, 'Success')
    
    
    #Google Download
    searchterm = file_id
    url = "https://www.google.com/search?q="+searchterm+"&source=lnms&tbm=isch"
    
    driver.get(url)

    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    # 이미지 카운트 (이미지 저장할 때 사용하기 위해서)
    counter = count
    succounter = 0
 
    print('Find Keyword')
    for _ in range(500):
        # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
        driver.execute_script("window.scrollBy(0,10000)")

    print('Downloading...')
    # div태그에서 class name이 rg_meta인 것을 찾아온다
    for x in driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
        counter = counter + 1
 
        # 이미지 url
        img = json.loads(x.get_attribute('innerHTML'))["ou"]
        imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    
        # 구글 이미지를 읽고 저장한다.
        try:
            req = urllib.request.Request(img, headers=header)
            raw_img = urllib.request.urlopen(req).read()
            File = open(os.path.join(destination , searchterm + "_" + str(counter) + "." + imgtype), "wb")
            File.write(raw_img)
            File.close()
            succounter = succounter + 1
        
        except:
            pass
    
    print('Google', succounter, 'Success')
    print('Total',counter,'Success')
    
    driver.close()





def auto_login(target_url, t_id, t_pwd):
    chrome_options = webdriver.ChromeOptions()
  
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    driver = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
    
    driver.implicitly_wait(3)

    url = target_url
    
    if(url == 'https://www.google.com' or url == 'http://www.google.com'):
        driver.get(url)
        
        driver.find_element_by_xpath('//*[@id="gb_70"]').click()
        
        
        time.sleep(1)
        driver.find_element_by_id('identifierId').send_keys(t_id)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        
        try:
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(t_pwd)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                print('Login Success')
            except:
                print('Check Your Pwd')
        except:
            print("Check Your ID")
        
        
    elif(url == 'https://www.naver.com' or url == 'http://www.naver.com'):
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()
        driver.execute_script("document.getElementsByName('id')[0].value=\'" + t_id + "\'")
        driver.execute_script("document.getElementsByName('pw')[0].value=\'" + t_pwd + "\'")
        driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        
        time.sleep(2)
        try:
            driver.find_element_by_xpath('//*[@id="query"]')
            print('Login Success')
        except:
            print('Please Check Your ID or Pwd')
        
    else:
        print('Please Check Your URL for example) https://www.naver.com')
    driver.close()




def print_exception(mode=0):
    if(mode == 1):
        print('System Argument must 3 or 4 or 5')
        print('--version: 1, 2, 3, 4, 5 or Youtube, ...')
        
    else:
        print('------System Argument 4------')
        print("1. Youtube")
        print("2. VscodeMarketplace")
        print('python crawling.py URL Destination --version')
        
        print("3. Download images by keyword")
        print('python crawling.py Keyword Destination --version')
        
        print('------System Argument 3------')
        print("4. GoogleDrive")
        print('python crawling.py URL --version')
        
        print('------System Argument 5------')
        print("5. Auto Login")
        print("Usage: python crawling.py URL ID Pwd --version")


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 5:
        print_exception(1)
        
    elif len(sys.argv) is 3:
        target_url = sys.argv[1]
        version = sys.argv[2]
        
        if(version == '--4' or version == 'GoogleDrive'):
            download_file_from_google_drive(target_url)
        else:
            print_exception()
        
    elif len(sys.argv) is 5:
        target_url = sys.argv[1]
        t_id = sys.argv[2]
        t_pwd = sys.argv[3]
        version = sys.argv[4]
        
        if(version == '--5' or version == 'Auto Login'):
            auto_login(target_url, t_id, t_pwd)
        else:
            print_exception()
        
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        
        # Destination 존재 X 시 만듬
        if not os.path.isdir(destination):
            os.mkdir(destination)
        
        # File 저장하기 위하여 destination 통일
        if destination[-1:] == '/':
            pass
        else:
            destination = destination + '/'
            
        version = sys.argv[3]
        if(version == '--1' or version == 'Youtube'):
            youtube_download(file_id,destination)
        elif(version == '--2' or version == 'VscodeMarketplace'):
            vscode_download(file_id, destination)
        elif(version == '--3' or version == 'Download images by keyword'):
            download_images_by_keyword(file_id, destination)
        else:
            print_exception()