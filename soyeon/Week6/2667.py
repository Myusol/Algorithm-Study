import sys
input = sys.stdin.readline

N = int(input())
graph = []

for _ in range(N):
     graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            cnt += 1
            dfs(nx, ny)
res = []
for X in range(N):
    for Y in range(N):
        if graph[X][Y] == 1:
            cnt = 1
            graph[X][Y] = 0
            dfs(X, Y)
            res.append(cnt)
res.sort()

print(len(res))
for cnt in res:
    print(cnt)