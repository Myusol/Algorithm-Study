import sys
memo={}
def plus(n):
    if n in memo:
        return memo[n]
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        memo[n] = plus(n-1) + plus(n-2) + plus(n-3)
        return memo[n]
T=int(sys.stdin.readline().strip())
for _ in range(T):
    n=int(sys.stdin.readline().strip())
    print(plus(n))
