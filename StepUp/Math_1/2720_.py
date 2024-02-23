# 거스름돈
# 0.25 0.10 0.05 0.01
import sys as s
input = s.stdin.readline

n = int(input().strip())
# 1달러 = 100센트
for i in range(n):
    money = int(input().strip()) # 센트
    for j in [25,10,5,1]:
        print(money//j,end=' ')
        money = money % j
    print("")