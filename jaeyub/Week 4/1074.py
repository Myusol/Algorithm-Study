import sys
N,r,c = map(int,sys.stdin.readline().split())


def Z(N,r,c):
    if N==0:
        return 0
    else:
        size = 2**N
        if size//2 > r:
            if size//2 >c:
                return Z(N-1,r,c)
            else:
                return Z(N-1,r,c-size//2) + 4**(N-1)
        else:
            if size//2 >c:
                return Z(N-1,r-size//2,c) + 4**(N-1)*2
            else:
                return Z(N-1,r-size//2,c-size//2) + 4**(N-1)*3
print(Z(N,r,c))