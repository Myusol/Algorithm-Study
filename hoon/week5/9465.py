# 스티커 / 실버1
# 2xn 길이 스티커 중에 양옆위아래 는 연속 불가능 하나씩 선택해서 최대값 구하기
T = int(input())
for _ in range(T):
    n = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, input().split()))) # 2차원 두줄 만들기
    if n == 1:
        print(*max(dp)) # 하나면 더 높은거
    elif n > 1: # 둘중에 높은거 고르기
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        for i in range(2, n):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2]) # 아래쪽에서 오는 최대값 더함
            dp[1][i] += max(dp[0][i-1], dp[0][i-2]) # 위쪽에서 오는 최대값 더함
        print(max(dp[0][n-1], dp[1][n-1])) # 마지막에 있는 최대값중 젤 높은 누적된 값을 출력