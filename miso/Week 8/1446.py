import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]

for i in range(D):
    graph[i].append((i+1, 1))
    
for _ in range(N):
    s, e, l = map(int, input().split())
    if e > D:
        continue
    graph[s].append((e, l))
    
def dijkstra(s):
    dist = [INF] * (D + 1)
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    
    while q:
        km, now = heapq.heappop(q)
        
        if dist[now] < km:
            continue
        
        for shortcut, length in graph[now]:
            total = km + length
            if total < dist[shortcut]:
                dist[shortcut] = total
                heapq.heappush(q, (total, shortcut))
    return dist

result = dijkstra(0)
print(result[D])