# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
#
# 예제 입력 1
# 5
# 20 10 35 30 7
# 예제 출력 1
# 7 35

n = int(input())
a = list(map(int,input().split()))
max=a[0]
min=a[0]
for i in range(n):
    if a[i]>=max:
        max=a[i]
    if a[i]<=min:
        min=a[i]
print(min,max)