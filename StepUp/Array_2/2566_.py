# 2차원에서의 최댓값 구하기
# 9 * 9 로 수 입력
# 첫째 줄에 최댓값 출력 , 둘째 줄에 행 번호와 열 번호 출력

max = 0
max_x,max_y = 0,0
arr = []
for i in range(9):
    arr.append(list(map(int,input().split())))

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] >= max :
            max = arr[i][j]
            max_x = i + 1 # 인덱스가 0부터 시작
            max_y = j + 1
print(max)
print("{} {}".format(max_x,max_y))

