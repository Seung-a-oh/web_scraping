# selenium: 웹 자동화 도구
# pip install selenium
# chrome://version
# 크롬 드라이버 다운

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")

elem = browser.find_element("link_login")
elem
elem.click()

browser.back()
browser.forward()

elem = browser.find_element("query")
elem
elem.send_keys("셀레니움 공부")
elem.send_keys(Keys.ENTER)

# elem2 = browser.find_element("a") 
# print(elem2)
# for e in elem2:
#     elem2.get_attribute("href")