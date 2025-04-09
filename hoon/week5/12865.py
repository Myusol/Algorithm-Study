# 평범한 배낭 / 골드5
# 물품 수 = n 무게 = w 가치 = v 최대 무게 = k
# 첫째줄 n,k
# 다음 부터 w, v
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
items = []
for _ in range(n):
    w, v = map(int,input().split())
    items.append((w, v)) # w, v는 세트니까 튜플 활용
dp = [0] * (k+1) # 최대 무게 가방을 만들고 (0부터니까 +1)
# 지금 items에 w,v 저장
for w, v in items:
    for i in range(k, w-1, -1): # 역순으로 반복( 앞에서 부터 하면 중복 가능)
        dp[i] = max(dp[i], dp[i-w] + v)
        # dp[i]: 현재 무게 i일 때 최대 가치
        # dp[i-w] + v: 이 물건을 넣었을 때 (남은 무게 i-w에서 최대 가치 + 이 물건의 가치)
        # 즉, 물건을 넣을지 말지를 결정하는 코드
print(dp[k])