from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# browser.maximize_window()   # 크롬 창 오픈 시 최대화

url = "https://flight.naver.com/"
browser.get(url)    # url로 이동

# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

try:
    # 성공했을때 동작 수행
    elem = WebDriverWait(browser, 10).util (EC.presence_of_all_elements_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[2]/button/b")))
finally:
    # 실패시 브라우저 종료
    browser.quit()

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[2]/button/b").click()
# browser.find_elements_by_link_text("12")[0].click()
# browser.find_elements(By.LINK_TEXT, "18")[1].click()
# browser.find_element(By.CLASS_NAME, "sc-dIsUp jEEywD num").click()

