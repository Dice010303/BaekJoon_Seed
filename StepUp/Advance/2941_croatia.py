# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=

# 단어 하나를 입력받고 단어가 몇개의 크로아티아 문자로 이루어져있는지 출력
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()
for i in croatia:
    word = word.replace(i,'*') # 크로아티아 문자 하나를 *로 변환
# replace(old,new,[count])
# old문자를 new문자로 count만큼 변환
print(len(word)) #바뀐 단어의 길이 출력
