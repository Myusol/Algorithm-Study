import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    INF = float('inf')
    dist = [INF] * (n+1)
    dist[c] = 0

    pq = [(0, c)]
    while pq:
        t, u = heapq.heappop(pq)
        if dist[u] < t:
            continue
        for v, w in graph[u]:
            nt = t + w
            if dist[v] > nt:
                dist[v] = nt
                heapq.heappush(pq, (nt, v))

    infected = sum(1 for x in dist[1:] if x < INF)
    last_time = max((x for x in dist[1:] if x < INF), default=0)
    print(infected, last_time)