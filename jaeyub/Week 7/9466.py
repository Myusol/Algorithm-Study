import sys
sys.setrecursionlimit(120000)

T = int(input())
for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    team_count = 0

    def dfs(i):
        global team_count

        visited[i] = True
        team.append(i)
        select = selected[i]

        if visited[select]:
            if select in team:
                team_count += len(team[team.index(select):])
        else:
            dfs(select)

    for i in range(1, N+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(N - team_count)