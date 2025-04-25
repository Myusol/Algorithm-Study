import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
maze=[list(map(int,input().strip())) for _ in range(N)]
direct=[(-1,0),(1,0),(0,-1),(0,1)]
def bfs():
    queue=deque([(0,0,1)])
    while queue:
        y,x,path=queue.popleft()
        if not(0<=y<N and 0<=x<M) or maze[y][x] == 0:
            continue
        if y==N-1 and x==M-1:
            print(path)
            return
        maze[y][x] = 0
        for dx,dy in direct:
            queue.append((y+dy,x+dx,path+1))
bfs()