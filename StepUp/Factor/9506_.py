# 완전수 : 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같을때
# n을 제외한 약수들의 합
import sys as s
input = s.stdin.readline

while True:
    n = int(input())
    if n == -1 :
        break
    fact_arr = []
    for i in range(1,n):
        if n%i == 0:
            fact_arr.append(i)

    if sum(fact_arr) == n:
        print(n,"=",end=" ")
        print(*fact_arr,sep=" + ")
    else:
        print("{} is NOT perfect.".format(n))