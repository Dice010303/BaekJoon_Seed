import sys as s
input = s.stdin.readline

n = int(input())
line = 1

while n > line :
    n-=line # 줄 확인 , n값이 그 줄에서 몇번째 수인지
    line+=1
if line%2 == 0: # 짝수 줄일때 분자1증가 분모1감소
    top = n
    bottom = line-n+1
else: # 홀수 줄일때 분자1감소 분모1증가
    top = line-n+1
    bottom = n
print("{}/{}".format(top,bottom))
