from collections import deque

N = int(input())
K = int(input())

board = [[0]* N for _ in range(N)]

for _ in range(K):
    Ax , Ay = map(int,input().split())
    board[Ax-1][Ay-1] = 2

x,y = 0,0
board[x][y] = 1
snake = deque()
snake.append((0,0))

dirDict = {}

L = int(input())
for _ in range(L):
    t,d = input().split()
    dirDict[int(t)] = d

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0
direction = 0

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N:
        break
    
    if board[x][y] == 2:
        board[x][y] = 1
        snake.append((x,y))

    elif board[x][y] == 1:
        break
    else:
        board[x][y] = 1
        snake.append((x,y))
        tx, ty = snake.popleft()
        board[tx][ty] = 0

    if time in dirDict:
        if dirDict[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)