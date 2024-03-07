import sys as s
input = s.stdin.readline
# 시간 복잡도 문제
# MenOfPassion(A[], n) {
#     sum <- 0;
# for i <- 1 to n
#   for j <- 1 to n
#       for k <- 1 to n
#           sum <- sum + A[i] × A[j] × A[k]; # 코드1
# return sum;
# }
# i가 증가할수록 j의 반복횟수가 증가하고
# j가 증가할수록 k의 반복횟수가 증가
# n^3
n = int(input())
print(n**3)
print(3)