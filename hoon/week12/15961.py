# 회전 초밥 / 골드4
import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
# 각 종류별로 몇 개 먹었는지 카운트
count = [0] * (d + 1)
unique = 0
# 초기 윈도우 설정
for i in range(k):
    if count[belt[i]] == 0:
        unique += 1
    count[belt[i]] += 1
# 쿠폰 초밥을 먹었는지 체크
max_kind = unique + (1 if count[c] == 0 else 0)
# 슬라이딩 윈도우 이동
for i in range(1, N):
    # 왼쪽 초밥 제거
    left = belt[i - 1]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1
    # 오른쪽 초밥 추가
    right = belt[(i + k - 1) % N]
    if count[right] == 0:
        unique += 1
    count[right] += 1
    # 쿠폰 초밥이 윈도우에 없으면 +1
    current_kind = unique + (1 if count[c] == 0 else 0)
    if current_kind > max_kind:
        max_kind = current_kind
print(max_kind)