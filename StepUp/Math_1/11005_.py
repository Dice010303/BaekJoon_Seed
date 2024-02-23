import sys as s
input = s.stdin.readline

# 10진법 수 n을 b진법으로 출력
n,b = map(int,input().strip().split())
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while n!=0:
    result += str(tmp[n%b])
    # 나머지를 문자로 더하기
    n = n //b
    # 몫
print(result[::-1])


