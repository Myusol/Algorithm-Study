# 두 용액 / 골드5
import sys
input = sys.stdin.readline
N = int(input())
liq = list(map(int, input().split()))
liq.sort()
left = 0
right = N - 1
# abs() 이거는 절대값을 구하는 함수
# 초기값 설정
min_diff = abs(liq[left] + liq[right])
answer = (liq[left], liq[right])
# 투 포인터 반복
while left < right:
    total = liq[left] + liq[right]
    # 0에 가까울 값 발견 시 갱신
    if abs(total) < min_diff:
        min_diff = abs(total)
        answer = (liq[left], liq[right])
        # 찾는 수 0 이 나오면 종료
    if total == 0:
        break
    # 합이 음수면 왼쪽을 더 높은 수로 변경
    elif total < 0:
        left += 1
    else:
    # 합이 양수면 수를 낮추기 위해서 더 낮은 수로 변경
        right -= 1
print(answer[0], answer[1])