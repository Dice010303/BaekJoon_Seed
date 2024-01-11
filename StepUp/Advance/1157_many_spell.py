# 단어 하나를 입력받는다
# 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다
# 대소문자를 구분하지 않는다
# 가장 많이 사용된 알파벳이 여러개일 경우 ?를 출력한다

s = input().lower()
s_list = list(set(s))  # set 자료형은 중복을 허용하지않는다.
                       #     순서가 없다.
cnt = []
for i in s_list:
    count = s.count(i)
    cnt.append(count)

if cnt.count(max(cnt))>=2 :
    print("?")
else:
    print(s_list[cnt.index(max(cnt))].upper())
