from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, rain, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고, 방문하지 않았고, 물에 잠기지 않은 경우
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > rain:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 최대 높이 찾기
max_height = max(map(max, graph))
result = 0

# 비의 양을 0부터 최대 높이까지 확인
for rain in range(0, max_height + 1):
    visited = [[False]*n for _ in range(n)]
    safe_area = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:
                bfs(i, j, rain, visited)
                safe_area += 1
    result = max(result, safe_area)

print(result)