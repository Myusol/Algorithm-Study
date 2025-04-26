import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
udlr = [(0, 1), (0, -1), (-1, 0), (1, 0)]
cnt = 0
        
def dijkstra():
    rupee = [[INF] * N for _ in range(N)]
    q = []
    heapq.heappush(q, (test[0][0], 0, 0))
    rupee[0][0] = test[0][0]
    
    while q:
        cost, x, y = heapq.heappop(q)
        
        if x == N - 1 and y == N - 1:
            return cost
        
        if rupee[y][x] < cost:
            continue
        
        for dx, dy in udlr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                ncost = rupee[y][x] + test[ny][nx]
                if ncost < rupee[ny][nx]:
                    rupee[ny][nx] = ncost
                    heapq.heappush(q, (ncost, nx, ny))
                
while True:
    N = int(input())
    if N == 0:
        break
    cnt += 1
    test = [list(map(int, input().split())) for _ in range(N)]
    print('Problem {0}: {1}'.format(cnt, dijkstra()))