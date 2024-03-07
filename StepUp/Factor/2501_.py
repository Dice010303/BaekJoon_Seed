import sys as s
input = s.stdin.readline

cnt = 0
n,k = map(int,input().strip().split())
for i in range(1,n+1):
    if n % i == 0 :
       cnt+=1
       if cnt == k:
           print(i)
           break
else:
    print(0) # 약수의 개수가 K보다 적을 때