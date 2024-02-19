# 단어 정렬
# 길이가 짧은것부터 정렬
# 길이가 같으면 사전 순으로 정렬
# 단, 중복된 단어는 하나만 남기고 제거

# 첫째줄에 단어의 개수 N 입력
# 둘째줄~ 알파벳 소문자로 이루어진 단어
import sys
words = []
n = int(sys.stdin.readline().strip())
for i in range(n):
    words.append(sys.stdin.readline().strip())

words = list(set(words))
words.sort() # 사전순으로 정렬
words.sort(key=len) # 길이순으로 정렬
# 기본 정렬에서 길이순으로 다시 정렬

for i in range(len(words)):
    print(words[i])