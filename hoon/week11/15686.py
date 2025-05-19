# 치킨 배달 / 골드5
import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
home = []
chic = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i, j)) # 집 일때 위치 저장
        elif board[i][j] == 2:
            chic.append((i, j)) # 치킨집 위치 저장
res = float('inf')
for chosen in combinations(chic, m): # 치킨집 리스트에서 m개의 치킨집 모든 조합 탐색(combinations)
    dist_sum = 0
    for hx, hy in home: # 각각의 집에 대해서 가장 가까운 거리 계산
        dist = min(abs(hx - cx) + abs(hy - cy) for cx, cy in chosen)
        dist_sum += dist
    res = min(res, dist_sum)
print(res)