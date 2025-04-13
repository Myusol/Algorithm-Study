from collections import deque
M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]

def BFS():
    deq = deque()
    for x in range(N):
        for y in range(M):
            if tomato[x][y] ==1:
                deq.append((x,y))

    while deq:
        x,y=deq.popleft()
        pos = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in pos:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M and tomato[nx][ny]==0:
                tomato[nx][ny]=tomato[x][y]+1
                deq.append((nx,ny))

BFS()
ans = 0

for i in tomato:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    ans = max(ans,max(i))

print(ans-1)