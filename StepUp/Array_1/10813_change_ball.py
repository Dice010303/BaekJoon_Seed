# N번까지의 바구니에는 각 바구니의 번호와 같은 공이 한개씩 들어있다.
# 바구니 두개를 선택하고 두 바구니에 들어있는 공을 교환한다. - 시행
# M번 시행

basket=[]
temp=0
n,m = map(int,input().split())
for i in range(n):
    basket.append(i+1)
for i in range(m):
    a,b = map(int,input().split())
    temp=basket[a-1]
    basket[a-1]=basket[b-1]
    basket[b-1]=temp
for i in basket:
    print(i,end=' ')


