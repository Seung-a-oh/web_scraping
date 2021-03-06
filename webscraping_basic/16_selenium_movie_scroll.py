import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Accept-Language":"ko-KR, ko"
    # 한국어에 대한 페이지를 줘!
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

browser.get(url)
# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크로 내리기
# browser.execute_script("window.scrollTo(0,1080)")

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 현재 문서 높이와 기존 문서 높이가 같다면 중단
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")