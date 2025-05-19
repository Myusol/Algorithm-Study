import sys
from collections import deque
input = sys.stdin.readline

direction = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}
dirs = ['R', 'D', 'L', 'U']

N = int(input())
K = int(input())
dummy = [[0] * N for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    dummy[y - 1][x - 1] = 1
    
L = int(input())
moves = deque([])
for _ in range(L):
    s, d = input().split()
    moves.append((int(s), d))
    
y, x = 0, 0
direct = 0
snake = deque([(y, x)])

time = 0
while True:
    time += 1
    
    dy, dx = direction[dirs[direct]]
    ny, nx = y + dy, x + dx
    
    if (ny, nx) in snake or not (0 <= nx < N and 0 <= ny < N):
        print(time)
        break
    
    snake.append((ny, nx))
    if dummy[ny][nx] == 1:
        dummy[ny][nx] = 0
    else:
        snake.popleft()
        
    y, x = ny, nx

    if moves and time == moves[0][0]:
        _, t = moves.popleft()
        if t == 'L':
            direct = (direct - 1) % 4
        else:
            direct = (direct + 1) % 4