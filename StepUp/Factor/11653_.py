# 소인수분해 : n을 소수의 곱으로 나타냄
import sys as s
input = s.stdin.readline

n = int(input())
factor = []
d = 2

for i in range(2,n+1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n = n / i