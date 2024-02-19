# 그룹 단어 체커
# 그룹 단어 : 단어에 존재하는 모든 문자에 대해서 , 각 문자가 연속해서 나타나는 경우
# ex) ccazzzzbb는 c,a,z,b가 모두 연속
#   ) kin도 k,i,n이 연속해서 나타남
#   ) aabbbccb는 b가 떨어져서 나타나기 떄문에 그룹 단어가 아니다.
#   단어 N개를 입력받아 그룹 단어의 개수를 출력하는 프로그램

n = int(input())
cnt = n # 전체 입력받는 단어의 개수

for i in range(n):
    word = input()
    for j in range(0,len(word)-1): # j+1로 인덱스를 줘도 범위벗어나지 않음.
        if word[j] == word[j+1] :
            pass # 연속된 문자 유무 체크
        # 연속된 문자라면 pass
        elif word[j] in word[j+1:]:
            # 연속되지 않은 두 문자
            # j+1부터 끝까지 검사하여 j 인덱스의 문자가 포함되면
            # 그룹 단어가 아님 ex) a a b / b  c  / c b
            #                           j j+1
            cnt-=1 # 조건에 맞지 않는 단어를 제외
            break
print(cnt)


