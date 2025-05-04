# K번째 수 / 골드1
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
# K번째 수는 무조건 K보다 같거나 작기 때문에 right를 K
left, right = 1, K
result = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in range(1,N+1):
        # mid 이하의 수가 총 몇개인지 계산
        count += min(N, mid // i)
    # K보다 크면 mid가 K번째 수일 가능성이 있으니까
    # result를 mid로 가정하고 큰 범위를 줄이고 시작
    if count >= K:
        result = mid
        right = mid -1
    else:
        left = mid + 1
print(result)