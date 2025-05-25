from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈 칸과 바이러스 위치 저장
empty = []
virus = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

# 바이러스 퍼뜨리는 함수 (BFS)
def spread_virus(board):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))

# 안전 영역 크기 계산
def get_safe_area(board):
    return sum(row.count(0) for row in board)

# 벽 3개를 세우는 모든 조합 시도
max_safe = 0
for walls in combinations(empty, 3):
    new_lab = copy.deepcopy(lab)
    for wx, wy in walls:
        new_lab[wx][wy] = 1
    spread_virus(new_lab)
    max_safe = max(max_safe, get_safe_area(new_lab))

print(max_safe)