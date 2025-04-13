import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
rain=[list(map(int,input().split())) for _ in range(N)]
direct=[(-1,0),(1,0),(0,-1),(0,1)]
minh = min(map(min,rain))
maxh = max(map(max,rain))
def bfs(x,y,height):
    queue=deque([(x, y)])
    visited[y][x]=1
    while queue:
        x,y=queue.popleft()
        for dx,dy in direct:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and visited[ny][nx]==0 and rain[ny][nx]>height:
                    visited[ny][nx]=1
                    queue.append((nx,ny))
safe=[]
for i in range(minh-1,maxh+1):
    visited=[[0]*N for _ in range(N)]
    cnt=0
    for y in range(N):
        for x in range(N):
            if visited[y][x]==0 and rain[y][x]>i:
                bfs(x,y,i)
                cnt+=1
    safe.append(cnt)
print(max(safe))