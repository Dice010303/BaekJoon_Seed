# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고,
# 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

n = int(input())

for i in range(n):
    OX_list = list(input())
    score = 0
    sum_score = 0
    for ox in OX_list:
        if ox == 'O':
            score+=1  # O가 나올때마다 score 증가
            sum_score+=score
        else:
            score = 0
    print(sum_score) # X가 나오면 0으로 초기화