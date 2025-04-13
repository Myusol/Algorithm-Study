# 단지 번호 붙이기 / 실버1
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
grid = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    row = list(map(int,input().strip()))
    grid.append(row)
def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    count = 1 # 어차피 시작이 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4): # cx, cy 기준으로 4가지 방향(dx,dy)으로 각각 순회
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n: # 그래프 범위 안에 있는 곳 맞는지 확인
                if grid[nx][ny] == 1 and not visited[nx][ny]: # 1표시 및 아직 방문 안 했으면 계속 탐색
                    visited[nx][ny] = True # True로 계속 방문 표시
                    queue.append((nx,ny)) # queue에 집어 넣어서 계속 탐색
                    count+=1 # 집 개수 추가
    return count # 단지하나 끝났으면 숫자 반환
homecount = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]: # 다시 전체 순회하면서 1인 곳 그리고 방문 안 했으면 계속 탐색
            homecount.append(bfs(i,j)) # i,j를 카운트에 넣고 계속 탐색 시작
homecount.sort() # 오름차순으로 정렬
print(len(homecount))
for count in  homecount:
    print(count)