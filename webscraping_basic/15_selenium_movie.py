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

movies = soup.find_all("div", attrs={"class":"VfPpkd-WsjYwc VfPpkd-WsjYwc-OWXEXe-INsAgc KC1dQ Usd1Ac AaN0Dd  MPNOXb"})
print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())
