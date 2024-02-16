# 세 개의 자연수 A,B,C가 주어질떄 A*B*C를 계산한 결과에 0부터 9까지의 숫자가 각각 몇 번씩 쓰였는지를 구함
# 150 * 266 * 427 = 17037300
# 0: 3번 , 1: 1번 , 3:2번 , 7:2번

a = int(input())
b = int(input())
c = int(input())
# 입력

num = a*b*c
# num = list(map(int,str(num)))
num= str(num)

cnt = [0 for i in range(10)]

for i in num:
    for j in range(10):
        if int(i) == j:
            cnt[j]+=1

for i in cnt:
    print(i)
