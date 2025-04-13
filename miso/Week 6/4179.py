import sys
from collections import deque
input = sys.stdin.readline
R,C=map(int,input().split())
maze=[list(input().strip())for _ in range(R)]
direct=[(1,0),(-1,0),(0,1),(0,-1)]
fqueue=deque()
jqueue=deque()
fire=[[-1]*C for _ in range(R)]
jihun=[[-1]*C for _ in range(R)]
for y in range(R):
    for x in range(C):
        if maze[y][x]=='F':
            fqueue.append((x,y))
            fire[y][x]=0
        if maze[y][x]=='J':
            jqueue.append((x,y))
            jihun[y][x]=0
            if x==0 or x==C-1 or y==0 or y==R-1:
                print(1)
                sys.exit()
def bfs():
    while fqueue:
        x,y=fqueue.popleft()
        for dx,dy in direct:
            nx,ny=x+dx,y+dy
            if 0<=nx<C and 0<=ny<R and maze[ny][nx]!='#' and fire[ny][nx]==-1:
                fire[ny][nx]=fire[y][x]+1
                fqueue.append((nx,ny))
    while jqueue:
        x,y=jqueue.popleft()
        for dx,dy in direct:
            nx,ny=x+dx,y+dy
            if 0<=nx<C and 0<=ny<R:
                if maze[ny][nx]!='#' and jihun[ny][nx]==-1:
                    if fire[ny][nx]==-1 or fire[ny][nx]>jihun[y][x]+1:
                        jihun[ny][nx]=jihun[y][x]+1
                        jqueue.append((nx,ny))
            else:
                return jihun[y][x]+1
    return'IMPOSSIBLE'
print(bfs())