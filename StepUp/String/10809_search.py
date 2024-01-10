# 단어 S를 받아서 각각의 알파벳이 처음!등장하는 위치를 포함되어있지 않으면 -1 출력

s = input()
eng=[]
for i in range(97,123):  # 알파벳 소문자 리스트
    eng.append(chr(i))
# for x in range(65,91): # 알파벳 대문자 리스트
#     eng.append(chr(i))
for i in eng:
    if i in s:
        print(s.index(i),end=' ')
    else:
        print("-1",end=' ')

