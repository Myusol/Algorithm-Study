import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


N, D = map(int,input().split())
graph = [[] for _ in range(D+1)]
distance = [float(1e9)] * (D+1)

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    s, e, l = map(int,input().split())
    if e > D:
        continue
    graph[s].append((e,l))

dijkstra(0)
print(distance[D])