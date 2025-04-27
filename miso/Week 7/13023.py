import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(i, depth):
    if depth == 5:
        return True
    visited[i] = True
    for p in graph[i] :
        if not visited[p]:
            if dfs(p, depth + 1):
                return True
    visited[i] = False
    return False
    
for i in range(N):
    visited = [False] * N
    if dfs(i, 1):
        print(1)
        break
else:
    print(0)