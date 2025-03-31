# 별 찍기 - 10 / 골드5
import sys
input = sys.stdin.readline
n = int(input())
def draw_star(x, y, size): # x,y = 시작 위치
    if size == 1:
        board[x][y] = '*'
        return    
    next_size = size // 3 # 3x3 정사각형으로 나눔
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue # 가운데 비우기
            draw_star(x + i * next_size, y + j * next_size, next_size) # 3x 중 i, j 번째 시작 위치
board = [[' ' for _ in range(n)] for _ in range(n)] # 2차원으로 비워있는 리스트 만들기
draw_star(0, 0, n)
for row in board:
    print(''.join(row)) # print(*row, sep='')