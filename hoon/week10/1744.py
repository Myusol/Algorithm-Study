# 수 묶기 / 골드4
import sys
input = sys.stdin.readline
n = int(input())
nums_pos = [] # 양수
nums_min = [] # 음수
# 수를 양수와 음수로 분리
for _ in range(n):
    num = int(input())
    if num > 0:
        nums_pos.append(num)
    else:
        nums_min.append(num)
# 양수 내림차순 정렬
nums_pos.sort(reverse=True)
# 음수 오름차순 정렬
nums_min.sort()
res = 0
# 양수 묶기
for i in range(1, len(nums_pos), 2):
    # 1은 곱하기 보다 더하기가 더 높음
    if nums_pos[i-1] == 1 or nums_pos[i] == 1:
        res += nums_pos[i-1] + nums_pos[i]
    else:
        res += nums_pos[i-1] * nums_pos[i]
# 남은 하나의 양수 더하기
if len(nums_pos) % 2 != 0:
    res += nums_pos[-1]
# 음수 묶기
for j in range(1, len(nums_min), 2):
    res += nums_min[j-1] * nums_min[j]  # 음수도 곱하는 것이 유리(음수는 더하면 손해)
# 남은 하나의 음수 더하기
if len(nums_min) % 2 != 0:
    res += nums_min[-1]
print(res)