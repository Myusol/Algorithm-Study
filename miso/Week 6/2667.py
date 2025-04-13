import sys
from collections import deque
input=sys.stdin.readline
N=int(input().strip())
apart=[list(map(int,input().strip())) for _ in range(N)]
direct = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(x, y):
    cnt=1
    queue=deque([(x,y)])
    apart[y][x]=0
    while queue:
        x,y=queue.popleft()
        for dx,dy in direct:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and apart[ny][nx]==1:
                apart[ny][nx]=0
                queue.append((nx,ny))
                cnt+=1
    return cnt
result=[]
for y in range(N):
    for x in range(N):
        if apart[y][x]==1:
            result.append(bfs(x,y))
print(len(result))
print(*sorted(result),sep='\n')