import sys
import heapq

input = sys.stdin.read
data = input().split()

V, E = int(data[0]), int(data[1])
K = int(data[2])

graph = [[] for _ in range(V + 1)]
idx = 3
for _ in range(E):
    u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    graph[u].append((v, w))
    idx += 3

INF = float('inf')
distance = [INF] * (V + 1)
distance[K] = 0

heap = []
heapq.heappush(heap, (0, K))

while heap:
    dist, now = heapq.heappop(heap)
    
    if distance[now] < dist:
        continue
    
    for neighbor, weight in graph[now]:
        cost = dist + weight
        if cost < distance[neighbor]:
            distance[neighbor] = cost
            heapq.heappush(heap, (cost, neighbor))

output = []
for i in range(1, V + 1):
    if distance[i] == INF:
        output.append("INF")
    else:
        output.append(str(distance[i]))

print("\n".join(output))