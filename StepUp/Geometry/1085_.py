import sys as s

input = s.stdin.readline
x,y,w,h = map(int,input().strip().split())
print(min(x,y,w-x,h-y))