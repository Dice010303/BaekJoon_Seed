# M * N 크기의 보드에서 8 * 8 크기의 체스판을 만드려고 함 (첫째줄에 입력)
# 체스판은 검은색과 흰색이 번갈아져 칠해져 있어야한다.
# 8*8 크기는 어디서든 고를 수 있다
# 다시 칠해야하는 정사각형의 최소 개수를 구함

# ex) 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW

# 1

n,m = map(int,input().split())
board = [] # 원래의 판을 저장하기 위한 리스트
result = [] # 바뀐 체스판의 개수를 저장하기 위한 리스트

for i in range(n):
    board.append(input())

# 8 * 8 로 자를 수 있는 범위의 시작점
for a in range(n-7) :
    for b in range(m-7):
        draw1 = 0 # W 로 시작할 경우
        draw2 = 0 # B 로 시작할 경우

        # 행과 열의 시작점을 기준으로 8칸씩 모두 체크
        for i in range(a,a+8):
            for j in range(b,b+8):
                # 짝수이면 시작점의 색깔과 같고
                # 홀수이면 시작점의 색깔과 다르다
                if (i+j) % 2 == 0:
                    if board[i][j] != "W" :
                        draw1 += 1
                    if board[i][j] != "B" :
                        draw2 += 1
                else:
                    if board[i][j] != "B" :
                        draw1 += 1
                    if board[i][j] != "W" :
                        draw2 += 1
        result.append(min(draw1,draw2))
print(min(result))
