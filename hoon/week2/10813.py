a,b=map(int,input().split())
lis = list(range(1,a+1))
for _ in range(b):
    i,j=map(int,input().split())
    c = lis[i-1]
    lis[i-1] = lis[j-1]
    lis[j-1] = c
print(*lis)