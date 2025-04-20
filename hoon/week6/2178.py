# 미로 탐색 / 실버1
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 연결된 길로 이동할 때 그래프를 벗어나면 무시
                continue
            if maze[nx][ny] == 0: # 미로의 0 은 벽이니까 무시
                continue
            if maze[nx][ny] == 1: # 이제 길을 찾아서 이동할 때
                maze[nx][ny] = maze [x][y] +1 # 숫자를 1씩 증가 시킴
                queue.append((nx,ny)) # 이동한거 다시 넣어서 또 반복
    return maze[n-1][m-1] # 마지막 도착지에 점수가 카운팅 됐으니까 끝
print(bfs(0,0))