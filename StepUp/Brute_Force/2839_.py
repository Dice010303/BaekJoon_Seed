# 설탕 3kg , 5kg
# 설탕을 n kg 배달해야할때 몇개를 가져가야하는지 그 최소값
import sys as s
input = s.stdin.readline

n = int(input())
bag = 0

while n >= 0:
    if n % 5 == 0: # 5의 배수이면
        bag += (n//5)
        print(bag)
        break
    n-=3
    bag+=1 #5의 배수가 될 때까지 설탕 -3 봉지 +1
else:
    print(-1)