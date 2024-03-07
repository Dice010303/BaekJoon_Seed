import sys as s
input = s.stdin.readline

# m과 n사이의 자연수 중 소수인 것들의 합과 최솟값
m = int(input()) #최소
n = int(input()) #최대
dec_list = []

for num in range(m,n+1):
    error = 0
    if num > 1 :
        for i in range(2,num):
            if num % i == 0:
                error+=1 # 소수가 아닐때마다 증가
                break
        if error == 0: # 오류가 하나도 없을때 : 소수일때
            dec_list.append(num)
if len(dec_list) > 0:
    print(sum(dec_list))
    print(min(dec_list))
else:
    print(-1)