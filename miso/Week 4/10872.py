import sys
def facto(n):
    if n==0:
        return 1
    else:
        return facto(n-1)*n
n=int(sys.stdin.readline().strip())
print(facto(n))