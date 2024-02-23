# 진법 변환
# B진법 수 N 을 10진법으로 바꿔 출력
# n = 36
# AAAAA
# 36^5*A(10) + 36^4*A(10)
# 입력 N , B
import sys as s
input = s.stdin.readline

b,n = input().strip().split()
n = int(n)
result = 0

for i in range(len(b)):
    if ord(b[i]) >= 65 :
        result += (n**(len(b)-1-i))*(ord(b[i])-55)
    else :
        result += (n**(len(b)-1-i)*int(b[i]))
    # ord : 아스키코드(문자)를 숫자로
    # ord(b[i]) -55 : A(65)는 10부터 시작
print(result)