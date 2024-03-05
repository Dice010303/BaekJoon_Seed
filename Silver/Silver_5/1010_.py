# 전체 M개에서 N개 선택
#  조합 mCn
import sys as s
import math
input = s.stdin.readline

test = int(input())
for i in range(test):
    n,m = map(int,input().strip().split())
    n_fact = math.factorial(n) #r!
    m_fact = math.factorial(m) #n!
    n_m_fact = math.factorial(m-n) #(n-r)!
    result = m_fact / (n_fact * n_m_fact)
    print(int(result))