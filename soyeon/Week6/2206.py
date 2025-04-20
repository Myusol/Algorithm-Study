import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = list(str(input().rstrip()))
    graph.append(list(map(int, row)))

moves = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1

    while queue:
        x, y, w = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for move in moves:
            nx, ny = x + move[0], y + move[1]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])
                elif graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    queue.append([nx, ny, w + 1])
    return -1

print(bfs())