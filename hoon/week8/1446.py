# 지름길 / 실버1
import sys
input = sys.stdin.readline
import heapq
n, d = map(int, input().strip().split())
graph = [[]for _ in range(d+1)]
for _ in range(n): # 지름길 입력
    start, end, length = map(int, input().strip().split())
    if end > d: # 넘어가면 무시
        continue
    graph[start].append((end,length))
for i in range(d):
    graph[i].append((i+1,1)) #  
def dijkstra(start):
    road = [float('inf')] * (d+1) # 무한대로 길이만큼 저장
    road[start] = 0
    queue = [(0, start)]
    while queue:
        dist, now = heapq.heappop(queue) # 현재 큐에서 가장 가까운 노드를 꺼냄
        if dist > road[now]: # 더 짧은 경로가 처리된 경우면 무시
            continue
        for n_node, we in graph[now]: # 현재 위치에서 갈 수 있는 모든 경로를 순회
            cost = dist + we
            if cost < road[n_node]: # 새로운 cost가 기존 cost보다 작으면 갱신
                road[n_node] = cost
                heapq.heappush(queue, (cost, n_node)) # 개신 됐으면 큐에 다시 push해서 나중에 탐색
    return road[d]
print(dijkstra(0))