# 안전 영역 / 실버1
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
grid = [] # 맵 만들고
for _ in range(n):
    row = list(map(int,input().split()))
    grid.append(row)
maxx = max(map(max,grid)) # 최대 높이 발견

def bfs(x, y, rain, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    # 방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n: # 필요없는 지역 제외
                # 물에 잠기지 않았고 아직 방문하지 않았으면
                if not visited[nx][ny] and grid[nx][ny] > rain:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
max_safe = 0
for rain in range(0,maxx + 1):
    visited = [[False] * n for _ in range(n)]
    safe_c = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] > rain:
                bfs(i, j, rain, visited)
                safe_c += 1
    max_safe = max(max_safe, safe_c)
print(max_safe)