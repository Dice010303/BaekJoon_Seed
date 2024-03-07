import sys as s
input = s.stdin.readline
# 중첩 반복문의 시간 복잡도
# for i <- 1 to n - 1
#  for j <- i + 1 to n
#   sum <- sum + A[i] × A[j]; # 코드1
#  i가 증가할수록 j의 반복횟수 가 감소
# (n+n+n+...) - (1+2+3+..)
# 등차수열의 합 공식
# s = n(n-1(초항) + (n-n(말항)) / 2
# s = n(n-1)/2 # 2차항
n = int(input())
print(int(n*(n-1)/2))
print(2)