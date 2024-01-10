# 수 10개를 입력받고 이를 42로 나눈 나머지를 구함
# 서로 다른 나머지 --> 배열 중복 제거

array=[]
result=[]
for i in range(10):
    x=int(input())
    remain=x%42
    array.append(remain)

for i in array:
    if i not in result:
        result.append(i)
print(len(result))
