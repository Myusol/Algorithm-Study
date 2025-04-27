import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
miro = []

pos_j = []
pos_f = []
for i in range(R):
    tmp = list(input())
    for j in range(C):
        if tmp[j] == "J":
            pos_j.append((i, j))
        elif tmp[j] == "F":
            pos_f.append((i, j))
    miro.append(tmp)

q = deque()
q.append((pos_j[0][0], pos_j[0][1], "J"))
miro[pos_j[0][0]][pos_j[0][1]] = 0

if len(pos_f) != 0:
    for (r, c) in pos_f:
        q.append((r, c, "F"))
        miro[r][c] = "#"

def bfs():
    pos = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x, y, case = q.popleft()
        if case == "J" and (x == 0 or y == 0 or x == R - 1 or y == C - 1) and miro[x][y] !='#':
            return miro[x][y] + 1
        for dx,dy in pos:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if case == "F" and miro[nx][ny] != "#":
                    miro[nx][ny] = "#"
                    q.append((nx, ny, "F"))
                elif case == "J" and miro[nx][ny] == "." and miro[x][y] != "#":
                    miro[nx][ny] = miro[x][y] + 1
                    q.append((nx, ny, "J"))
    return "IMPOSSIBLE"

print(bfs())