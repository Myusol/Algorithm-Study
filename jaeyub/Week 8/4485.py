import sys
import heapq
input = sys.stdin.readline

n = int(input())
pos = [(0,1),(1,0),(-1,0),(0,-1)]
cnt = 0

while n != 0:
    cnt+=1
    board = [list(map(int, input().split())) for _ in range(n)]
    heap = []

    dist = [[1e9] * n for _ in range(n)]

    dist[0][0] = board[0][0]
    heapq.heappush(heap, (board[0][0], 0, 0))

    while heap:
        distance, x, y = heapq.heappop(heap)

        if x == n-1 and y == n-1:
            print(f"Problem {cnt}: {distance}")
            n = int(input())
            break

        for dx,dy in pos:
            nx = x + dx
            ny = y + dy
			
            if 0 <= nx < n and 0 <= ny < n:
                cost = distance + board[nx][ny]
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    heapq.heappush(heap, (cost, nx, ny))