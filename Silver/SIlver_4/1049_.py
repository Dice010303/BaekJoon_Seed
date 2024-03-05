import sys as s
input = s.stdin.readline
pack = []
each = []
n,m = map(int,input().strip().split())
for i in range(m):
    a,b=map(int,input().strip().split())
    pack.append(a)
    each.append(b)

pack = min(pack)
each = min(each)

if pack < each * 6 : # 세트값이 낱개로 살때보다 적을때
    if pack < (n%6) * each: # 세트로 사고 남는 값이 세트값보다 클때
        print((n//6)*pack + pack) # x세트 + 한세트(더 구매)
    else:
        print((n//6)*pack + (n%6)*each)
elif pack >= each * 6: # 낱개로 사는게 이득일때 !
    print(n * each)