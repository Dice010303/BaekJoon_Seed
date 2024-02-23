# 벌집
import sys as s
input = s.stdin.readline
n = int(input())
hive = 1
for i in range(n):
    hive += 6*i
    if hive>=n:
        print(i+1)
        break

