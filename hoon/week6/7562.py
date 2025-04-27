# 나이트의 이동 / 실버1
from collections import deque
import sys
input = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2] # 이동가능 범위
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
def bfs(l, start, end):
    visited = [[False]*l for _ in range(l)]
    queue = deque()
    queue.append((start[0], start[1], 0))  # (x, y, 이동횟수)
    visited[start[0]][start[1]] = True
    while queue:
        x, y, count = queue.popleft()
        if (x, y) == end:
            return count
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
    return 0
t = int(input())
for _ in range(t):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(bfs(l, start, end))