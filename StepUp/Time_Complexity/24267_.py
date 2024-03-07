# 시간복잡도 문제
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#       for j <- i + 1 to n - 1
#           for k <- j + 1 to n
#               sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
# 시그마 공식
# n-2   k        n-2
# ∑   ( ∑ x ) =   ∑  ( k(k+1) / 2 )
# k=1  x=1      k = 1
# n(n-1)(n-2) / 6
import sys as s
input = s.stdin.readline
n = int(input())
print(int((n*(n-1)*(n-2))/6))
print(3)