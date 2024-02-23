# 분해합 2
import sys as s
input = s.stdin.readline
n = int(input())
num = 0

start = n - len(str(n))*9
if start >= 0:
    for i in range(start,n):
        num = i + sum(map(int,str(i)))
        if num == n :
            print(i)
            # 가장 처음으로 num이 n과 같아지는 값
            break
    else:
        print(0)
else :
    for i in range(n):
        num = i + sum(map(int,str(i)))
        if num == n :
            print(i)
            # 가장 처음으로 num이 n과 같아지는 값
            break
    else:
        print(0)