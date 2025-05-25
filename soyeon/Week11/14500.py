import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_sum = 0
visited = [[False] * m for _ in range(n)]

def dfs(x, y, depth, total):
    global max_sum

    if depth == 4:
        max_sum = max(max_sum, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

# ㅗ 모양은 DFS로 만들 수 없기 때문에 따로 처리
def check_extra_shape(x, y):
    global max_sum
    center = board[x][y]
    shapes = [
        [(0, 1), (0, -1), (1, 0)],   # ㅗ
        [(0, 1), (0, -1), (-1, 0)],  # ㅜ
        [(1, 0), (-1, 0), (0, 1)],   # ㅏ
        [(1, 0), (-1, 0), (0, -1)]   # ㅓ
    ]

    for shape in shapes:
        total = center
        valid = True
        for dx_, dy_ in shape:
            nx = x + dx_
            ny = y + dy_
            if 0 <= nx < n and 0 <= ny < m:
                total += board[nx][ny]
            else:
                valid = False
                break
        if valid:
            max_sum = max(max_sum, total)

# 전체 탐색
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_extra_shape(i, j)

print(max_sum)