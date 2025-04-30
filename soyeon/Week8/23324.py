import sys, heapq
input = sys.stdin.readline
INF = 10**18

N, M, K = map(int, input().split())

adj = [[] for _ in range(N + 1)]
ku = kv = None          # K번째(=가중치1) 간선의 양 끝

for i in range(1, M + 1):
    u, v = map(int, input().split())
    if i == K:          # 가중치 1인 간선이므로 일단 저장만
        ku, kv = u, v
    else:               # 나머지는 가중치 0
        adj[u].append((v, 0))
        adj[v].append((u, 0))

# 다익스트라 (여기선 0-1 BFS와 동일)
dist = [INF] * (N + 1)
dist[ku] = 0
pq = [(0, ku)]

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    for v, w in adj[u]:
        if dist[v] > d + w:           # w 는 항상 0
            dist[v] = d + w
            heapq.heappush(pq, (dist[v], v))

# K번째 간선이 0-경로로 대체 가능한지 판단
if dist[kv] == 0:                     # 같은 컴포넌트 → 모든 최단거리 합 0
    print(0)
else:
    sizeA = sum(1 for x in dist[1:] if x == 0)   # ku 가 속한 컴포넌트 크기
    sizeB = N - sizeA
    print(sizeA * sizeB)
