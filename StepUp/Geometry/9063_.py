import sys as s
input = s.stdin.readline

point = int(input())
x_list,y_list = [],[]
for i in range(point):
    x,y = map(int,input().strip().split())
    x_list.append(x)
    y_list.append(y)
width = max(x_list)-min(x_list)
height = max(y_list)-min(y_list)
area = width * height
print(area)