import sys
def z(N,r,c):
    if N==1:
        arr=[[0,1],[2,3]]
        return arr[r][c]
    div=2**(N-1)
    if r<div and c<div:
        return z(N-1,r,c)
    elif r<div and c>=div:
        return z(N-1,r,c-div)+4**(N-1)
    elif r>=div and c<div:
        return z(N-1,r-div,c)+2*(4**(N-1))
    else:
        return z(N-1,r-div,c-div)+3*(4**(N-1))
N,r,c=map(int,sys.stdin.readline().split())
print(z(N,r,c))