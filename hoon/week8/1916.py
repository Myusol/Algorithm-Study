# 최소비용 구하기 / 골드5
import sys
input = sys.stdin.readline
import heapq
# n = 도시 개수 m = 이동 버스 개수
# 출발 도시, 도착 도시, 비용 을 m개 입력
# 목표 = m+3(마지막줄)에 출발,도착 까지 cost 출력
n = int(input().strip())
m = int(input().strip())
graph = [[]for _ in range(n+1)]
# 버스 노선 입력
for _ in range(m):
    s, a, weight = map(int, input().strip().split())
    graph[s].append((a, weight))
# 출발지 도착지
start, arrive = map(int, input().split())
def dijkstra(scity):
    distance = [float('inf')] * (n + 1) # 무한대로 초기화, 1부터 니까 +1
    distance[start] = 0
    queue = [(0, start)] # (비용, 시작 도시)
    while queue:
        # 방문할 비용, 도시
        current_cost, current_city = heapq.heappop(queue)
        # 방문할 비용이 현재 비용보다 크면 무시
        if current_cost > distance[current_city]:
            continue
        # 이동 할 도시, 가는 비용 현재 위치에서 반복
        for next_city, next_cost in graph[current_city]:
            # total_cost = 지금까지 비용 + 다음 비용 값 (즉, 다음으로 이동했다고 가정)
            total_cost = current_cost + next_cost
            # total_cost가 이동할 도시에 가는 현재 최단거리 보다 작으면 갱신
            if total_cost < distance[next_city]:
                distance[next_city] = total_cost
                heapq.heappush(queue, (total_cost, next_city))
    return distance
min_cost = dijkstra(start)
print(min_cost[arrive])