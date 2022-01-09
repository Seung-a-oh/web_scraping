import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=774862"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]
print(title)
print("https://comic.naver.com"+link)

# 만화 제목과 링크 가져오기 
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)
    

# 평점 구하기
scores = soup.find_all("div", attrs={"class":"rating_type"})
title = cartoons[0].a.get_text()

total_score = 0
for score in scores:
    rate = score.find("strong").get_text()
    print(rate)
    total_score += float(rate)
print("전체 점수: ", total_score)
print("평균 점수: ", total_score/len(scores))