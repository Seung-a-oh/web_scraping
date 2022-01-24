from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True     # 웹 페이지를 보이지 않게 백그라운드에서 실행
options.add_argument("window-size=1920x1080") # 백그라운드에서 동작하는 크기 명시적으로 지정

browser = webdriver.Chrome(options=options)
browser.get("https://naver.com")

e = browser.find_element(By.XPATH, "//*[@id='NM_FAVORITE']/div[1]/ul[2]/li[8]/a")
e.click()

url = browser.current_url
print
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

cartoon = soup.find("li", attrs={"class":"rank01"}).find("a").get_text()
print("현재 1위 인기 웹툰: ",cartoon)