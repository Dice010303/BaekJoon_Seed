# 소수 : 약수가 1과 자기 자신뿐인 수
import sys as s
input = s.stdin.readline

n = int(input())
x = list(map(int,input().strip().split()))
decimal_cnt = 0 # 소수의 개수

for i in x:
    cnt = 0
    for j in range(2,i+1): # 1을 제외한 약수
        if i % j == 0:
            cnt+=1
    if cnt == 1:
        decimal_cnt += 1
print(decimal_cnt)