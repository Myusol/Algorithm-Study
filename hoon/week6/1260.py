# DFS와 BFS / 실버2
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 1번부터 사용

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향

# 정점 번호가 작은 것을 먼저 방문해야 하므로 정렬
for adj in graph:
    adj.sort()

# DFS 실행
visited_dfs = [False] * (n + 1)
dfs(graph, v, visited_dfs)
print()

# BFS 실행
visited_bfs = [False] * (n + 1)
bfs(graph, v, visited_bfs)