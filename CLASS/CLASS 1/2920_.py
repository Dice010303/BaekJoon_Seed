# 1부터 8까지 차례로 연주하면 ascending
# 8부터 1까지 차례로 연주하면 descending
# 둘다 아니라면 mixed

num = list(map(int,input().split()))

# sorted (기본적으로 오름차순 정렬)
# sorted(정렬할 데이터,{reverse 파라미터})
# sorted(정렬할 데이터,{key 파라미터})
# sorted(정렬할데이터,{key},{reverse})
# list.sort : 본체의 리스트를 정렬해서 반환
# sorted(list) : 정렬한 새로운 리스트를 반환

if num == sorted(num):
    print("ascending")
elif num == sorted(num,reverse=True):
    print("descending")
else:
    print("mixed")