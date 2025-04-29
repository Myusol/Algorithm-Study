import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())
INF = float('inf') 
dist =[INF] * (n + 1)
pq = []
dist[start] = 0
heapq.heappush(pq, (0, start))

while pq:
    d, u = heapq.heappop(pq)
    if dist[u] < d:
        continue
    if u == end:
        break
    for v, w in graph[u]:
        nd = d + w
        if dist[v] > nd:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[end])