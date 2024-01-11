# 체스는 16개의 피스를 사용
# 킹 1 퀸 1 룩 2 비숍 2 나이트 2 폰 8
#발견한 흰색피스의 개수가 주어짐
# 몇 개를 더하거나 뺴야 올바른 세트가 되는지 구하라

white = list(map(int,input().split()))
piece = [1,1,2,2,2,8]    # 전체 피스수
black=[]

for i in range(len(piece)):
    black.append(piece[i]-white[i]) # 전체 피스수에서 흰색피스를 뺌
for i in black:
    print(i,end=' ')