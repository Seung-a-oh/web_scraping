import requests
url = "http://nadocoding.tistory.com"
#User Agent가 없었을 때는 스크래핑을 할 수 없었는데, User Agent를 넣어주자 가능해짐.
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html","w", encoding="utf-8") as f:
    f.write(res.text)