import sys

n = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(n)]


dp=[0]*n
if n <3:
    print(sum(score))
else:
    dp[0] = score[0]
    dp[1] = score[0]+score[1]
    dp[2] = max(score[0]+score[2],score[1]+score[2],dp[1])
    for i in range(3,n):
        dp[i]= max(dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i],dp[i-1])

    print(dp[-1])