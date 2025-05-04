# 숨바꼭질 3 / 골드5
import sys
input = sys.stdin.readline
import heapq
n, k = map(int, input().strip().split())
def dijkstra(n,k):
    max = 100001 # 최대범위
    dist = [float('inf')] * max
    dist[n] = 0
    queue = []
    heapq.heappush(queue,(0,n)) # 술래 시작점
    while queue:
        time, curr = heapq.heappop(queue)
        # 저장된 시간이 새로 계산된 시간보다 작으면 무시
        if dist[curr] < time:
            continue
        # 순간이동 처리
        move = curr * 2
        # 0 - 100000 안으로만 허용 그리고 누적시간보다 time이 더 작으면 갱신
        if 0 <= move < max and time < dist[move]:
            dist[move] = time
            heapq.heappush(queue, (time, move))
        # 일반 이동
        move = curr +1
        # 이동시간에 1추가해서 더 낮으면 저장
        if 0 <= move < max and time + 1 < dist[move]:
            dist[move] = time + 1
            heapq.heappush(queue, (time + 1, move))
        move = curr -1
        if 0 <= move < max and time + 1 < dist[move]:
            dist[move] = time + 1
            heapq.heappush(queue, (time + 1, move))
    return dist[k]
print(dijkstra(n,k))