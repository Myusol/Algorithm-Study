from collections import deque

def BFS(x,y):
    count = 0
    deq = deque()
    deq.append((x,y))
    board[x][y] = -1
    count+=1

    while deq:
        x,y = deq.popleft()
        pos = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx,dy in pos:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==1:
                deq.append((nx,ny))
                board[nx][ny]=-1
                count+=1
    return count

N = int(input())
board = [list(map(int,input())) for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            answer.append(BFS(i,j))

answer.sort()
print(len(answer))
for count in answer:
    print(count)