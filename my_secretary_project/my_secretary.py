import requests
import re
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# browser = webdriver.Chrome()
# browser.get("http://naver.com")

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}


# elem = browser.find_element(By.ID, "query")
# elem.send_keys("인천 날씨")
# elem.send_keys(Keys.ENTER)

# try:
#     # 성공했을때 동작 수행
#     elem = WebDriverWait(browser, 10).util (EC.presence_of_all_elements_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[2]/button/b")))
# finally:
#     # 실패시 브라우저 종료
#     browser.quit()

def creat_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def get_weather():
    weather_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8"
    weather_soup = creat_soup(weather_url)

    weather = weather_soup.find("p", attrs={"class":"summary"}).get_text()
    # yesterday = weather_soup.find("p",attrs={"class":""})
    cur_temp = weather_soup.find("div",attrs={"class":"temperature_text"}).get_text().replace(" 현재 온도","")
    lowest = weather_soup.find("span",attrs={"class":"lowest"}).get_text().replace("최저기온","")
    highest = weather_soup.find("span",attrs={"class":"highest"}).get_text().replace("최고기온","")
    rainfall = weather_soup.find("div",attrs={"class":"day_data"}).find_all("span",attrs={"class":"rainfall"})
    micro_dust = weather_soup.find("li",attrs={"class":"item_today level1"}).find("span",attrs={"class":"txt"}).get_text()
    super_micro_dust = weather_soup.find("li",attrs={"class":"item_today level3"}).find("span",attrs={"class":"txt"}).get_text()
    rain_am = rainfall[0].get_text()
    rain_pm = rainfall[1].get_text()

    print("[오늘의 날씨]")
    print(weather)
    # print("현재",cur_temp+"(최저",lowest,"/ 최고",highest+")")
    # print("오전 강수 확률",rain_am, "/ 오후 강수 확률",rain_pm)

    print("현재 {} (최저 {} / 최고 {})".format(cur_temp, lowest, highest))
    print("오전 강수 확률 {} / 오후 강수 확률 {}".format(rain_am, rain_pm))
    print("미세먼지 {} / 초미세먼지 {}".format(micro_dust, super_micro_dust))
    print()


def get_news():
    news_url = "https://news.naver.com/"
    news_soup = creat_soup(news_url)

    # headlines = news_soup.find_all("div",attrs={"class":"cjs_t"})
    headlines = news_soup.find_all("div",attrs={"class":"cjs_journal_wrap _item_contents"}, limit=3)

    print("[헤드라인 뉴스]")

    for index, headline in enumerate(headlines):
        title = headline.find("div", attrs={"class":"cjs_t"}).get_text()
        link = headline.find("a")["href"]

        print("{}. {}".format(index+1, title))
        print("  (링크: {})".format(link))
    print()


def get_it():
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    it_soup = creat_soup(url)

    its = it_soup.find_all("li",attrs={"class":"cluster_item as_line"}, limit=3)

    print("[IT 뉴스]")

    for index, it in enumerate(its):
        title = it.find("a").get_text()
        link = it.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  링크: {}".format(link))
    print()


def get_english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    eng_soup = creat_soup(url)

    # CLASS VERSION
    engs = eng_soup.find_all("span",attrs={"class":"conv_sub"})
    print("[오늘의 영어 회화]")
    print("(영어 지문)")
    for eng in engs[len(engs)//2:]:
        print(eng.get_text().strip())
    print("\n(한글 지문)")
    for eng in engs[:len(engs)//2]:
        print(eng.get_text().strip())

        
    # MY VERSION
    engs = eng_soup.find_all("div",attrs={"class":"conv_txt"})
    kos = engs[0]
    ens = engs[1]

    print("[오늘의 영어 회화]")
    print("(영어 지문)")
    for e in ens:
        print(e.get_text().strip())
    print("(한글 지문)")
    for k in kos:
        print(k.get_text().strip())


if __name__ == "__main__":
    get_weather()
    get_news()
    get_it()
    get_english()

