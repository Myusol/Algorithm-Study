import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
apart = [list(map(int, input().split())) for _ in range(N)]
max_rain = max(map(max, apart))

pos = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(i,j):
    global count
    deq = deque()
    deq.append((i,j))
    sink[i][j] = True
    count += 1
    while deq:
        x,y = deq.popleft()
        for dx,dy in pos:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<N and sink[nx][ny]==False:
                sink[nx][ny] = True
                deq.append((nx,ny))

count_list = []
for rain in range(max_rain):
    count = 0
    sink = [[False for _ in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if apart[i][j]<=rain:
                sink[i][j]=True
                
    for i in range(N):
        for j in range(N):
            if sink[i][j]==False:
                bfs(i,j)
    count_list.append(count)

print(max(count_list))