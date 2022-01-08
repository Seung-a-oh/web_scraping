import re

p = re.compile("ca.e") 
# (ca.e) . : 하나의 문자를 의미 => care, cade, cave ...
# (^de) ^ : 문자열의 시작 => desk, destination, delivery ...
# (se$) $ : 문자열의 끝 => case, loose, rose ...

def print_match(m):
    if m: 
        print(m.group())
    else:
        print("매칭되지 않음")

m = p.match("careless")
print_match(m)
# print(m.group()) # 매칭이 되면 출력, 매칭이 안되면 에러 발생

