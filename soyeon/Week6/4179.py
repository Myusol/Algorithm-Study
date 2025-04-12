from collections import deque

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    fire_queue = deque()
    jihun_queue = deque()

    fire_time = [[-1]*C for _ in range(R)]     # 불의 도착 시간
    jihun_time = [[-1]*C for _ in range(R)]    # 지훈이의 이동 시간

    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'F':
                fire_queue.append((i, j))
                fire_time[i][j] = 0
            elif graph[i][j] == 'J':
                jihun_queue.append((i, j))
                jihun_time[i][j] = 0

    while fire_queue:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    fire_queue.append((nx, ny))

    while jihun_queue:
        x, y = jihun_queue.popleft()

        # 탈출 조건: 가장자리에 도달하면 바로 출력
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            print(jihun_time[x][y] + 1)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '#' or jihun_time[nx][ny] != -1:
                    continue

                # 불이 없거나, 지훈이가 먼저 도착하면 이동 가능
                if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    jihun_queue.append((nx, ny))
    print("IMPOSSIBLE")  

bfs()