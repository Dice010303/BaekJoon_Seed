import sys as s
input = s.stdin.readline

n = int(input())
a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))

s = 0
for i in range(n):
    s+=min(a)*max(b) # a의 최솟값 * b의 최대값
    a.remove(min(a))
    b.remove(max(b))
print(s)