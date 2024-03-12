import sys as s
input = s.stdin.readline

n,m = map(int,input().strip().split())
card = list(map(int,input().strip().split()))
result = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k] > m:
                continue
                # 3중 반복문 - 세 카드의 값을 각각 순회
            else:
                # m보다 크지 않을때(작거나 같을때) (<=)
                result = max(result,card[i]+card[j]+card[k])
                # m과 가장 가까운 값
print(result)