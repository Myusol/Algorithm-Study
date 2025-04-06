# 1 2, 3 더하기 / 실버3
import sys
input = sys.stdin.readline
n  = int(input())
def cnt(a):
    dp = [0] * (12)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7
    for i in range(5,a+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[a]
for _ in range(n):
    a = int(input())
    print(cnt(a))