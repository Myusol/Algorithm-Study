# 가장 긴 증가하는 부분 수열 / 실버2
import sys
input = sys.stdin.readline
n = int(input())
lis = list(map(int,input().split()))
dp = [1] * n # 어차피 하나씩 보면 경우의 수는 일단 1
for i in range(n): # 리스트의 i번째 숫자가 젤 max일때
    for j in range(i): # 그전의 숫자들 비교
        if lis[i] > lis[j]:
            dp[i] = max(dp[i], dp[j]+1) # 지금까지 계산된 길이중에 더 긴것을 dp[i]번째에 저장
print(max(dp)) # 마지막 수 기준으로 최대값 저장한 것 중에 최대값을 출력