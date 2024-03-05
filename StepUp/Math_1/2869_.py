# 높이가 v미터인 나무를 올라가는 달팽이
# 낮에 a미터 올라가고 , 밤에 b미터 미끄러짐
# 입력 : a,b,v
import sys as s
input = s.stdin.readline
a,b,v = map(int,input().strip().split())
# 올라가야할 거리 % 하루에 갈 수 있는거리 = 0 이면 정상에 도달
# 이미 a만큼 올라감(v-b) , a만큼 오르고 b만큼 내려갈수있음(a-b)
if (v-b) % (a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1) # 하루+1