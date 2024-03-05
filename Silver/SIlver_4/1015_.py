import sys as s

input = s.stdin.readline
n = int(input())
a = list(map(int,input().strip().split()))

b = sorted(a)
p=[]
for i in range(n):
    idx = b.index(a[i])
    p.append(idx)
    b[idx] = -1 # 중복을 허용하므로 지나간 인덱스 값 변경
    print(p[i],end=' ')