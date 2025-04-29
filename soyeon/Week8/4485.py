import sys
import heapq
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 , 1]

case_num = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    dist[0][0] = graph[0][0]

    pq = [(dist[0][0], 0, 0)]
    while pq:
        cost, x, y = heapq.heappop(pq)
        if cost > dist[x][y]:
            continue
        if x == n-1 and y == n-1:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                nc = cost + graph[nx][ny]
                if nc < dist[nx][ny]:
                    dist[nx][ny] = nc
                    heapq.heappush(pq, (nc, nx, ny))

    print(f"Problem {case_num}: {dist[n-1][n-1]}")
    case_num += 1