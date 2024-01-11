# 알파벳 소문자로만 이루어진 단어
# 앞으로 읽을때와 거꾸로 읽을 때 똑같은 단어 - 팰린드롬
#팰린드롬이면 1 아니면 0 출력

palindrome = input()
if palindrome[::1] == palindrome[::-1]: # 원래문자녕 == 역순문자열
    print(1)
else:
    print(0)
