n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def dfs(idx, current_sum):
    global cnt
    if idx >= 0 and current_sum == s:
        cnt += 1

    if idx == n - 1:
        return

    for next_idx in range(idx + 1, n):
        dfs(next_idx, current_sum + arr[next_idx])

dfs(-1, 0)

print(cnt)