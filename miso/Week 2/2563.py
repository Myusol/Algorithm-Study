n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
xma=max(li[0] for li in l)
yma=max(li[1] for li in l)
b=[[0]*(xma+10) for _ in range(yma+10)]
for i in range(n):
    x,y=l[i][0]-1,l[i][1]-1
    for dx in range(10):
        for dy in range(10):
            b[y+dy][x+dx]+=1
print((xma+10)*(yma+10)-sum(row.count(0) for row in b))


####

b=[[0]*100 for _ in range(100)]
for i in range(int(input())):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            b[j][i]=1
print(sum(row.count(1) for row in b))