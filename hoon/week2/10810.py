# a = 5 b = 4 i,j,k = 1 2 3
a,b=map(int,input().split())
list=[0] * a
for _ in range(b):
    i,j,k=map(int,input().split())
    for z in range(i-1,j):
        list[z] = k
print(*list)