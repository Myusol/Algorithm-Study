import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
empties = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_valid(x, y, num):
    for i in range(9):
        if board[x][i] == num or board[i][y] == num:
            return False

    start_x, start_y = x // 3 * 3, y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[start_x + i][start_y + j] == num:
                return False

    return True

def dfs(index):
    if index == len(empties):
        for row in board:
            print(' '.join(map(str, row)))
        sys.exit(0)

    x, y = empties[index]
    for num in range(1, 10):
        if is_valid(x, y, num):
            board[x][y] = num
            dfs(index + 1)
            board[x][y] = 0

dfs(0)