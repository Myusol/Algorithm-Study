# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

def dfs(N, M, R, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for node in graph:
        graph[node].sort(reverse=True)

    visited_order = [0] * (N + 1)
    visited = [False] * (N + 1)
    stack = [R]
    order = 1

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            visited_order[node] = order
            order += 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

    return visited_order[1:]
data = input().split()
N, M, R = map(int, data[:3])
edges = [tuple(map(int, data[i:i+2])) for i in range(3, len(data), 2)]
result = dfs(N, M, R, edges)
for val in result:
    print(val)