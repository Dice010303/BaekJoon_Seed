# 첫번째 줄에 본 시험의 개수 N입력
# 두번째 줄에 시험 점수 입력
# 조작 : 점수/최고점*100

n = int(input())
score = list(map(int,input().split())) # 한줄에 입력받기(리스트이용)
m = max(score) #최대값
rig =[]
for i in range(n):
    rig.append(score[i]/m*100) #조작하여 rig리스트에 넣기
print(sum(rig)/n) #rig리스트의 평균
