import sys
from collections import deque
input=sys.stdin.readline
moves=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
def bfs(x,y,cnt):
    queue=deque([(x,y,cnt)])
    while queue:
        x,y,cnt=queue.popleft()
        if x==xend and y==yend:
            print(cnt)
            return
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if 0<=nx<l and 0<=ny<l and not chess[ny][nx]:
                chess[ny][nx]=1
                queue.append((nx,ny,cnt+1))
n=int(input().strip())
for _ in range(n):
    l=int(input().strip())
    xstart,ystart=map(int,input().split())
    xend,yend=map(int,input().split())
    chess=[[0]*l for _ in range(l)]
    bfs(xstart,ystart,0)