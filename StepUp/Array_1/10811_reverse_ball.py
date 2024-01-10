# N번까지의 바구니에 각 번호가 들어있다.
# I번쨰 부터 J번쨰까지의 바구니의 공을 역순으로 만든다 . - 시행
# M번 시행

reverse=[]
slice=[]
piece=[]
basket = []
n,m = map(int,input().split())
for x in range(n):
    basket.append(x+1)
for x in range(m):
    i,j = map(int,input().split())
    slice = basket[i-1:j] #배열의 일부를 슬라이스 (i-1 부터 j까지)
    slice.reverse() #배열을 역순으로
    basket[i-1:j] = slice #역순한 배열을 원래 배열에 대입
for x in basket:
    print(x,end=' ')