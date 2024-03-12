import sys as s
input = s.stdin.readline

a,b,c,d,e,f = map(int,input().strip().split())

x = int((e*c-b*f)/(a*e-b*d))
y = int((a*f-d*c)/(a*e-b*d))
print(x,y)