from collections import deque

N,M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]

def BFS(x,y):
    pos = [(0,1),(0,-1),(1,0),(-1,0)]
    deq = deque()
    deq.append((x,y))

    while deq:
        x,y = deq.popleft()
        for dx,dy in pos:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                deq.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[-1][-1]

print(BFS(0,0))
