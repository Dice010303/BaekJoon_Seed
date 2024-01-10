# 다이얼 전화기
#     ABC DEF GHI JKL MNO PQRS TUV WXYZ Operator
# 1   2   3   4   5   6    7   8    9   0
# 2s  3s  4s  5s  6s  7s   8s  9s  10s
# 입력된 문자를 거는데 걸리는 시간

s = input().lower()
time=0
dial = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
for i in range(len(s)):
    for j in dial:
        if s[i] in j:
            # 요소 하나를 하나의 배열로 s[i]번째 알파벳이 들어있는지 확인
            time+=dial.index(j) + 3  # index 0부터 시작 + 1은 2s
print(time)