import sys
def fibo(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return(fibo(n-2)+fibo(n-1))
n=int(sys.stdin.readline().strip())
print(fibo(n))