import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())
INF = float('inf')
dist = [INF] * (n + 1)
dist[start] = 0
pq = [(0, start)]

while pq:
    cost, u = heapq.heappop(pq)
    if cost > dist[u]:
        continue
    for v, w in graph[u]:
        new_cost = cost + w
        if new_cost < dist[v]:
            dist[v] = new_cost
            heapq.heappush(pq, (new_cost, v))

print(dist[end])