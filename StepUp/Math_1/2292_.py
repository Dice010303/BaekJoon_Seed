# 벌집
import sys as s
input = s.stdin.readline
n = int(input())
def func(n):
    return 3*n*(n-1) + 1 # 등비수열의 일반항 1 , 6 12 18  + 1
if n == 1:
    print(1)
else:
    start , end = 0 , 1750000000
    while start <= end :
        mid = (start+end)//2
        if func(mid) >= n:
            end = mid - 1
        else:
            start = mid + 1
    print(end+1)