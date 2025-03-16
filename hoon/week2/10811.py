a,b=map(int,input().split())
lis = list(range(1,a+1)) # [1, 2, 3, 4, 5]
for _ in range(b):
    i,j = map(int,input().split())
    lis[i-1:j] = reversed(lis[i-1:j]) # i-1부터 j까지
print(*lis)