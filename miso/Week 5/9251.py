import sys
lcs1=list(map(str,sys.stdin.readline().strip()))
lcs2=list(map(str,sys.stdin.readline().strip()))
lcs=[[0]*(len(lcs2)+1) for _ in range(len(lcs1)+1)]
for i in range(1,len(lcs1)+1):
    for j in range(1,len(lcs2)+1):
        if lcs1[i-1]==lcs2[j-1]:
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
print(lcs[-1][-1])