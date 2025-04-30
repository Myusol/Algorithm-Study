import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dijkstra(s, e):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    
    while q:
        tcost, n = heapq.heappop(q)
        
        if n == e:
            return distance[e]
        
        if distance[n] < tcost:
            continue
        
        for g, cost in graph[n]:
            ncost = tcost + cost
            if ncost < distance[g]:
                distance[g] = ncost
                heapq.heappush(q, (ncost, g))

sc, ec = map(int, input().split())
print(dijkstra(sc, ec))