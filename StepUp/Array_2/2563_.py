import sys as s

input = s.stdin.readline

n = int(input().strip())
rect = [[0]*100 for _ in range(100)]
# 전체를 0으로 초기화
area = 0


for i in range(n):
    x,y = map(int,input().strip().split())

    # x,y를 기준으로 가로로 10칸,세로로 10칸씩 1로 채움
    for i in range(x,x+10):
        for j in range(y,y+10):
            rect[i][j] = 1

for k in range(100):
    area+=rect[k].count(1)
    # 1인 곳의 개수만 셈
print(area)