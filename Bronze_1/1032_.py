n = int(input())

# 파일 명들도 입력받는다
file_names = []

for _ in range(n):
    file_names.append(input())

answer = ''

# 파일 이름 길이는 모두 같다고 하니 첫 글자 기준으로 한글자씩 반복하며
for i in range(len(file_names[0])):
    character = ''
    # 모든 글자들을 확인하는데
    for file_name in file_names:
        # 첫글자이거나 저장해둔 문자와 같으면 그 문자로 갱신
        if character == '' or character == file_name[i]:
            character = file_name[i]
        # 만약 하나라도 저장된 글자와 다르면 그 인덱스의 문자는 ?
        else:
            character = '?'
            break
    # 정답에 한 글자씩 추가
    answer += character

print(answer)