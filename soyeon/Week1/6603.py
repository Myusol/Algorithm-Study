def dfs(start, path):
    if start == 6:
        print(*out)
        return
    
    for i in range(path, k):
        out.append(s[i])
        dfs(start + 1, i + 1)
        out.pop()

while True:
    data = list(map(int, input().split()))
    k = data[0]
    s = data[1:]

    out = []
    dfs(0, 0)
    if k == 0:
        exit()

    print()