# 점근적 표기 - 빅 오
# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# f(n) = a1n + a0
# O(n)의 정의를 만족하는가?
import sys as s
input = s.stdin.readline

a1,a0 = map(int,input().strip().split())
c = int(input())
n0 = int(input())

# fn = 7n + 7 , g(n)= n ,c =8
# 7(1) + 7 <= 8 * 1 (x)
# 7(10) + 7 <= 8 * 10 (o)
if (a1 * n0 + a0 <= c*n0) and a1 <= c :# a0가 음수일 경우
    # 4 2 -2 <= 2 2
    print(1)
else :
    print(0)