import requests
res = requests.get("http://google.com")
print("응답코드:",res.status_code)

#문제가 생겼을 때는 에러를 뱉고 프로그램을 종료
res.raise_for_status()

#에러 없을 시 아래 문장 출력
print("웹 스크래핑을 진행합니다.")

with open("mygoogle.html","w", encoding="utf-8") as f:
    f.write(res.text)