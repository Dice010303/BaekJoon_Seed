import sys as s
input = s.stdin.readline

x = int(input())
stick = [64,32,16,8,4,2,1]
cnt = 0

for i in range(len(stick)):
    if x >= stick[i]:
        cnt+=1
        x-=stick[i] # 막대기를 붙이고 막대기 길이만큼 x에서 빼줌

    if x == 0:
        break
print(cnt)