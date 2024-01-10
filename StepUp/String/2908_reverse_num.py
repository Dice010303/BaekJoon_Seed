# 두 수를 입력받는다
# 수를 거꾸로 읽어 비교하여 크기가 큰 수를 찾는다
# 321 789 --> 123 < 987

a,b = input().split()
reverse_a = a[::-1]
reverse_b = b[::-1]
print(max(reverse_a,reverse_b))