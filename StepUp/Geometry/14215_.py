import sys as s
# 삼각형의 조건 : 가장 긴변의 길이보다 나머지 두 변의 길이의 합이 더 커야함
input = s.stdin.readline

triangle = []
a,b,c = map(int,input().strip().split())
triangle.append(a)
triangle.append(b)
triangle.append(c)
max_side = max(triangle)
triangle.remove(max_side)
remain_side = sum(triangle)
if max_side < remain_side : # 조건을 만족
    round = max_side + remain_side
else : # 조건을 만족하지 않음 -> 작은 두 수의 합의 2배에서 1을 뺌
    round = remain_side * 2 - 1
print(round)