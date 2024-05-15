
from selenium import webdriver #selenum 터미널에 설치필요
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager #webdriver_manager 터미널에 설치필요

import pandas as pd #터미널에 설치필요
import time
import pyautogui #터미널에 설치필요
import pyperclip

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

#불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches",['enabell-logging'])

service = Service(executable_path=ChromeDriverManager().install())

# Chrome 웹 드라이버 실행
#driver_path = r"C:\Users\강문성\Documents\파이썬 코드\chromedriver\chromedriver.exe"
#service = Service(executable_path=driver_path)
# 에브리타임 홈페이지 열기

driver = webdriver.Chrome(service=service, options=chrome_options)


#웹페이지 해당 주소로 이동
driver.get('https://everytime.kr/login')

#5초 딜레이
driver.implicitly_wait(5)

#화면 최대화
driver.maximize_window()

# 로그인 (아이디와 비밀번호를 입력해주세요)
id = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div > form > div.input > input[type=text]:nth-child(1)")
id.click()
#id.send_keys("에타 자기꺼 아이디 입력") 오류나기 쉽다
pyperclip.copy("에타 아이디 입력")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

password = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div > form > div.input > input[type=password]:nth-child(2)")
password.click()
#password.send_keys("에타 자기꺼 비번 입력")
pyperclip.copy("에타 비번 입력")  #복사
pyautogui.hotkey("ctrl","v")   #붙여넣기
time.sleep(2)  #2초간 쉬기

#로그인 버튼

#login_btn =driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div > form > input[type=submit]")   #작동안됨 ㅜㅜ
#login_btn.click()   #작동안됨 ㅜㅜ

pyautogui.press('enter')
time.sleep(5)
pyautogui.press('enter')


import requests
from bs4 import BeautifulSoup #BeautifulSoup 터미널에 설치 필요

# 에브리타임 게시판 URL
url = 'https://everytime.kr/382389'

# 페이지 내용 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 게시글 제목 추출
title_element = soup.select_one('.large > h2')
if title_element:
    title = title_element.get_text()
    print(f"게시글 제목: {title}")

# 게시글 내용 추출
content_element = soup.select_one('.large > .articles > .article > .text')
if content_element:
    content = content_element.get_text()
    print(f"게시글 내용:\n{content}")










'''

body > div:nth-child(2) > div > form > div.input > input[type=text]:nth-child(1)
body > div:nth-child(2) > div > form > div.input > input[type=password]:nth-child(2)
body > div:nth-child(2) > div > form > input[type=submit]
# 자유게시판 페이지로 이동
#driver.get('https://everytime.kr/382389')

# 전자과의 모든것 게시판으로 이동
driver.get('https://everytime.kr/414454')

# 게시글 텍스트 가져오기 (예: 첫 번째 게시글)
post_text = driver.find_element_by_css_selector('.articles .text').text
print(f"게시글 텍스트: {post_text}")

# 웹 드라이버 종료
driver.quit()

dictionary = {}  # 크롤링한 정보를 담기 위한 dictionary

#https://everytime.kr/414454/v/341742124


# 게시판 글 링크 요소를 찾아서 텍스트를 추출합니다.
link_elements = driver.find_elements_by_css_selector('.article > a')
for link_element in link_elements:
    link_text = link_element.text
    print(link_text)

# 브라우저 종료
driver.quit()
'''