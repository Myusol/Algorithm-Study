from collections import deque

N = int(input())
K = int(input())

board = [[0]*N for _ in range(N)]  # 0: 빈칸, 1: 사과
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input())
directions = dict()
for _ in range(L):
    t, c = input().split()
    directions[int(t)] = c

# 방향: 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 초기 방향: 오른쪽

snake = deque()
snake.append((0, 0))
time = 0
x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽에 부딪히거나 자기 몸에 부딪히면 종료
    if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in snake:
        break

    snake.append((nx, ny))
    if board[nx][ny] == 1:
        board[nx][ny] = 0  # 사과 먹기
    else:
        snake.popleft()  # 꼬리 제거

    x, y = nx, ny

    # 방향 회전
    if time in directions:
        if directions[time] == 'D':
            direction = (direction + 1) % 4
        else:  # 'L'
            direction = (direction - 1) % 4

print(time)