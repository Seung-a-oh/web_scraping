import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# html 문서를 lxml parser를 통해서 객체로 만든 것
# soup 객체를 통해 element에 바로 접근을 할 수 있음
print(soup.title)   # title 출력
print(soup.title.get_text())
print(soup.a)       # 처음 발견되는 a 출력
print(soup.a.attrs) # a element의 속성 정보 반환
print(soup.a["href"])   # a element의 href 값 

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
print(soup.find(attrs={"class":"Nbtn_upload"}))

rank01 = soup.find("li", attrs={"class":"rank01"})
print(rank01.a.get_text())
print(rank01.next_sibling)              # 태그 사이에 개행 정보가 있어서 한 번으론 출력 안됨
print(rank01.next_sibling.next_sibling) # 두 번 해주면 제대로 출력되는 것을 확인 가능

rank02 = rank01.next_sibling.next_sibling
rank03 = rank02.next_sibling.next_sibling
print(rank02)
print(rank03)

rank02 = rank03.previous_sibling.previous_sibling

print(rank01.parent)

# next_sibling 갯수를 항상 알 수 있는 것이 아님.
# 다음 li를 대상으로 sibling 진행
rank02 = rank01.find_next_sibling("li")
print(rank02)

# rank01 뒤 전체 li 찾기 sliblig"s"
print(rank01.find_next_siblings("li"))

# 내용으로 태그 검색
content = soup.find("a", text="존망코인-10화 이게 사치가 아니면 뭐임!")
print(content)