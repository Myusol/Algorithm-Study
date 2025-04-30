import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

max_size = 100001
dist = [float('inf')] * max_size
dist[N] = 0

heap = []
heapq.heappush(heap, (0, N))

while heap:
    time, now = heapq.heappop(heap)
    
    if dist[now] < time:
        continue
    
    # 순간이동 (시간 0초)
    if 0 <= now * 2 < max_size and dist[now * 2] > time:
        dist[now * 2] = time
        heapq.heappush(heap, (time, now * 2))
    
    # 앞으로 한 칸 (시간 1초)
    if 0 <= now + 1 < max_size and dist[now + 1] > time + 1:
        dist[now + 1] = time + 1
        heapq.heappush(heap, (time + 1, now + 1))
    
    # 뒤로 한 칸 (시간 1초)
    if 0 <= now - 1 < max_size and dist[now - 1] > time + 1:
        dist[now - 1] = time + 1
        heapq.heappush(heap, (time + 1, now - 1))

print(dist[K])