import re

p = re.compile("ca.e") 

def print_match(m):
    if m: 
        print(m.group())    #일치하는 문자열 반환
        print(m.string)     #입력받은 문자열
        print(m.start())    #일치하는 문자열의 시작 index
        print(m.end())      #일치하는 문자열의 끝 index
        print(m.span())     #일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

m = p.match("careless")
print_match(m)
# print(m.group()) # match: 매칭이 되면 출력, 매칭이 안되면 에러 발생

m2 = p.search("careless") # search: 주어진 문자열 중에 일치하는게 있는지 확인

m3 = p.findall("careless") # findall: 일치하는 모든 것을 리스트 형태로 변환



# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 화인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열"): 일치하는 모든 것을 리스트 형태로 변환

# 원하는 형태: 정규식
# (ca.e) . : 하나의 문자를 의미 => care, cade, cave ...
# (^de) ^ : 문자열의 시작 => desk, destination, delivery ...
# (se$) $ : 문자열의 끝 => case, loose, rose ...
