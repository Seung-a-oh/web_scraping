import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://naver.com")

e = browser.find_element_by_class_name("link_login")
e.click()

# id, pw 입력
browser.find_element_by_id("id").send_keys("id")
browser.find_element_by_id("pw").send_keys("password")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# id 다시 입력 
# 아이디가 기존 입력한 아이디에 이어써지는 것을 방지하기 위해 clear()
browser.find_element_by_id("id").send_keys("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
browser.close()     # 탭만 종료
browser.quit()      # 웹 종료