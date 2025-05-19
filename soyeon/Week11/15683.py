import sys
import copy
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
min_blind_spot = int(1e9)

# CCTV 좌표 수집
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))

# 감시 처리
def watch(temp, x, y, directions):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                break
            if temp[nx][ny] == 6:  # 벽
                break
            if temp[nx][ny] == 0:
                temp[nx][ny] = -1  # 감시 표시

# 백트래킹
def dfs(depth, arr):
    global min_blind_spot
    if depth == len(cctvs):
        count = sum(row.count(0) for row in arr)
        min_blind_spot = min(min_blind_spot, count)
        return

    x, y, type = cctvs[depth]
    for dirs in cctv_dir[type]:
        temp = copy.deepcopy(arr)
        watch(temp, x, y, dirs)
        dfs(depth + 1, temp)

dfs(0, office)
print(min_blind_spot)