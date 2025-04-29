import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
ku = kv = 0
for i in range(M):
    u, v = map(int, input().split())
    if i == K - 1:
        ku, kv = u, v
    else:
        graph[v].append((u, 0))
        graph[u].append((v, 0))

def dijkstra():
    dist = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, ku))
    dist[ku] = 0
    
    while q:
        t, now = heapq.heappop(q)
        
        if t != dist[now]:
            continue
        
        for next, w in graph[now]:
            if dist[next] > t + w:
                dist[next] = t + w
                heapq.heappush(q, (dist[next], next))
                
    if dist[kv] == 0:
        return 0
    
    else:
        beforeU = sum(1 for x in dist[1:] if x == 0)
        afterV = N - beforeU
        return beforeU * afterV
    
print(dijkstra())

# 플로이드 워셜 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9)
N, M, K = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for y in range(1, N + 1):
    for x in range(1, N + 1):
        if y == x:
            graph[y][x] = 0
            
for i in range(M):
    u, v = map(int, input().split())
    if i == K:
        graph[v][u] = 1
        graph[u][v] = 1
    else:
        graph[v][u] = 0
        graph[u][v] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

s = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        sum += graph[i][j]
print(s)