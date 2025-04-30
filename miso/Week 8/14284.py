import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start, end):
    dist = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        shortest, now = heapq.heappop(q)
        
        if now == end:
            return dist[end]
        
        if dist[now] < shortest:
            continue
        
        for next, weight in graph[now]:
            nweight = shortest + weight
            if nweight < dist[next]:
                dist[next] = nweight
                heapq.heappush(q, (nweight, next))

    return dist[end]
s, t = map(int, input().split())
print(dijkstra(s, t))