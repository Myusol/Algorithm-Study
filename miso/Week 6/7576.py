import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
tomato=[list(map(int,input().split())) for _ in range(M)]
direct=[(-1,0),(1,0),(0,-1),(0,1)]
queue=deque()
for y in range(M):
    for x in range(N):
        if tomato[y][x]==1:
            queue.append((x,y))
def bfs():
    while queue:
        x,y=queue.popleft()
        for dx,dy in direct:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and tomato[ny][nx]==0:
                tomato[ny][nx]=tomato[y][x]+1
                queue.append((nx,ny))
bfs()
days=0
for row in tomato:
    for value in row:
        if value==0:
            print(-1)
            exit()
        days=max(days,value)
print(days-1)