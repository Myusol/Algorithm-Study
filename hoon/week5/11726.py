# 2xn 타일링 / 실버3
import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(1%10007)
elif n == 2:
    print(2)
elif n == 3:
    print(3%10007)
elif n == 4:
    print(5%10007)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5
    for i in range(5,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%10007)