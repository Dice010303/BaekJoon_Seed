# 다섯줄의 문자열 입력
# 각 줄에 1~15개의 글자들이 빈칸없이 연속으로 주어짐
# 각 줄의 시작과 마지막에 빈칸은 없음.
# 만들어진 다섯개의 단어를 세로로 읽음
import sys
input = sys.stdin.readline

max_word_len = 0 # 세로로 읽는 횟수 : 단어의 최대길이
word = ""
board = []
vertical_word = ""
vertical_line = ""

for i in range(5):
    word = input().strip()
    if len(word) >= max_word_len:
        max_word_len = len(word)
    board.append(word)

# 단어 길이가 다를 경우 out of index 오류 발생
for i in range(5):
    if len(board[i]) < max_word_len:
        board[i] += " "*(max_word_len - len(board[i]))
        # 부족한 자리(최대길이-현재단어길이)를 공백으로 채워 인덱스 수 맞추기

# print(board)

# vertical_word += board[0][0]
# vertical_word += board[1][0]
# vertical_word += board[2][0]
# vertical_word += board[3][0]
# vertical_word += board[4][0]

for i in range(max_word_len):
    for j in range(5):
        vertical_word += board[j][i]
    vertical_line += vertical_word
    vertical_word =""
print(vertical_line.replace(" ","")) # 공백 제거