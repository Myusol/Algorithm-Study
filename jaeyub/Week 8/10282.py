import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distances[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)

        if distances[now] > dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost

            if distances[next_node] > cost:
                distances[next_node] = cost
                heapq.heappush(hq, (cost, next_node))


t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distances = [INF] * (n + 1)
    result = []

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dijkstra(c)

    for distance in distances:
        if distance < INF:
            result.append(distance)

    print(len(result), max(result))