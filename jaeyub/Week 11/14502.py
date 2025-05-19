from collections import deque
from itertools import combinations

def bfs(vgraph,vrs):
    copy_vrs = deque(vrs)
    visited = [[False]*M for _ in range(N)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for x,y in copy_vrs:
        visited[x][y] = True

    while copy_vrs:
        x,y = copy_vrs.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == False and vgraph[nx][ny] == 0:
                    vgraph[nx][ny] = 2
                    visited[nx][ny] = True
                    copy_vrs.append((nx,ny))
    return vgraph

N,M = map(int,input().split())
graph = []
empty = []
virus = deque()
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] == 2:
            virus.append((i,j))
        if arr[j] == 0:
            empty.append((i,j))

    graph.append(arr)

safe = 0
for a,b,c in combinations(empty, 3):
    vgraph = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            vgraph[i][j] = graph[i][j]
    for x,y in [a,b,c]:
        vgraph[x][y] = 1

    vgraph = bfs(vgraph,virus)
    zero = 0
    for i in vgraph:
        for j in i:
            if j==0:
                zero += 1
    safe = max(safe, zero)
print(safe)