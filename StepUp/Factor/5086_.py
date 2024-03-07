import sys as s
input = s.stdin.readline

while True :
    a,b = map(int,input().strip().split())
    if a == 0 and b == 0 :
        break
    if b % a == 0 : # b가 a의 약수
        print("factor")
    elif a % b == 0 : # a가 b의 배수(b가 a의 약수)
        print("multiple")
    else:
        print("neither")