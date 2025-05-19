# 뱀 / 골드4
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1 # 사과는 1
l = int(input())
turn = dict()
for _ in range(l):
    x, c = input().split() # x초에 c(L, D)로 방향 전환
    turn[int(x)] = c
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direc = 0
snake = deque() # 뱀 위치, appendleft(머리), pop(꼬리)
snake.append((0,0))
time = 0
x, y = 0, 0
while True:
    time += 1 # 한번 작동마다 1초 증가
    nx = x + dx[direc]
    ny = y + dy[direc]
    if not (0<= nx < n and 0 <= ny < n) or (nx, ny) in snake:
        break # 범위 벗어나면 종료
    snake.appendleft((nx, ny))
    if board[nx][ny] == 1: # 사과 만나면 0으로 바꿈
        board[nx][ny] = 0
    else:
        snake.pop()
    x, y = nx, ny
    if time in turn: # turn 가능한 시간인지 확인
        if turn[time] == 'L':
            direc = (direc - 1) % 4 # 방향 인덱스를 바꾸고 0보다 작거나 3보다 커지면 순환하기 위해서 % 씀
        else:
            direc = (direc + 1) % 4
print(time)