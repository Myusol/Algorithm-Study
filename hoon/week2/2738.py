a,b = map(int,input().split())
lis=[]
for _ in range(a):
    row = list(map(int,input().split()))
    lis.append(row)
liss=[]
for _ in range(a):
    row = list(map(int,input().split()))
    liss.append(row)
lisss=[]
for i in range(a):
    nrow=[]
    for j in range(b):
        z = lis[i][j] + liss[i][j]
        nrow.append(z)
    lisss.append(nrow)
for row in lisss:
    print(" ".join(map(str, row)))
        