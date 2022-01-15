from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()   # 크롬 창 오픈 시 최대화

url = "https://flight.naver.com/"
browser.get(url)    # url로 이동

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
# browser.find_element_by_link_text("가는 날").click()

# browser.find_element("15")[1].click()
# browser.find_element("18")[1].click()

