# Top-Down 방식
import sys
n=int(sys.stdin.readline().strip())
memo={}
def tile(n):
    if n in memo:
        return memo[n]
    if n<=2:
        return n
    else:
        memo[n]=tile(n-1)+tile(n-2)
        return memo[n]
print(tile(n)%10007)

# Bottom-Up 방식
import sys
n=int(sys.stdin.readline().strip())
def tile(n):
    if n<=2:
        return n
    p2,p1=1,2
    for _ in range(3,n+1):
        res=p1+p2
        p2,p1=p1,res
    return res
print(tile(n)%10007)
