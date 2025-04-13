from collections import deque

def bfs(F, S, G, U, D):
    visited = [False] * (F + 1)
    dist = [0] * (F + 1)

    queue = deque([S])
    visited[S] = True

    while queue:
        curr = queue.popleft()

        if curr == G:
            return dist[curr]

        for next_floor in (curr + U, curr - D):
            if 1 <= next_floor <= F and not visited[next_floor]:
                visited[next_floor] = True
                dist[next_floor] = dist[curr] + 1
                queue.append(next_floor)

    return "use the stairs"

F, S, G, U, D = map(int, input().split())
print(bfs(F, S, G, U, D))