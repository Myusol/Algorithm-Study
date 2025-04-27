from collections import deque

def BFS(x,y,ex,ey):
    deq = deque()
    deq.append((x,y))
    pos = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

    while deq:
        x,y=deq.popleft()
        if x==ex and y==ey:
            return chess[x][y]
        for dx,dy in pos:
            nx = x+dx
            ny = y+dy
            if 0<=nx<I and 0<=ny<I:
                if chess[nx][ny]==0:
                    deq.append((nx,ny))
                    chess[nx][ny]=chess[x][y]+1

T = int(input())
for _ in range(T):
    I = int(input())
    x,y=map(int,input().split())
    ex,ey=map(int,input().split())
    chess = [[0]*I for _ in range(I)]
    if x==ex and y==ey:
        print(0)
    else:
        print(BFS(x,y,ex,ey))