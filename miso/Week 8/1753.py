import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
def dijkstra(start):
    path = [INF] * (V + 1)
    q = []
    heapq.heappush(q, (0, start))
    path[start] = 0
    
    while q:
        dist, n = heapq.heappop(q)
        
        if path[n] < dist:
            continue
        
        for next, weight in graph[n]:
            sweight = dist + weight
            if sweight < path[next]:
                path[next] = sweight
                heapq.heappush(q, (sweight, next))
    return path            

result = dijkstra(K)
for i in range(1, V + 1):
    if K == i:
        print(0)
    else:
        print(result[i] if result[i] != INF else "INF")