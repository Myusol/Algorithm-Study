import sys
import heapq
input = sys.stdin.readline

n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]
for _ in range(n):
    u, v, w = map(int, input().split())
    if v <= d:
        graph[u].append((v, w))

for i in range(d):
    graph[i].append((i+1, 1))

INF = 10**18
dist = [INF] * (d+1)
dist[0] = 0

pq = [(0, 0)]
while pq:
    curr_d, u = heapq.heappop(pq)
    if curr_d > dist[u]:
        continue
    for v, w in graph[u]:
        nd = curr_d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[d])