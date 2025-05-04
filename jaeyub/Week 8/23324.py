import sys, heapq
input = sys.stdin.readline
INF = 10**18

N, M, K = map(int, input().split())

adj = [[] for _ in range(N + 1)]
ku = kv = None

for i in range(1, M + 1):
    u, v = map(int, input().split())
    if i == K:
        ku, kv = u, v
    else:
        adj[u].append((v, 0))
        adj[v].append((u, 0))

dist = [INF] * (N + 1)
dist[ku] = 0
pq = [(0, ku)]

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    for v, w in adj[u]:
        if dist[v] > d + w: 
            dist[v] = d + w
            heapq.heappush(pq, (dist[v], v))


if dist[kv] == 0:
    print(0)
else:
    sizeA = sum(1 for x in dist[1:] if x == 0)
    sizeB = N - sizeA
    print(sizeA * sizeB)