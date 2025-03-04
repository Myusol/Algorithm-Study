N,M = map(int,input().split())
순열 = []

def dfs():
    if len(순열) == M:
        print(" ".join(map(str, 순열)))
        return
    for i in range(1,N+1):
        if i not in 순열:
            순열.append(i)
            dfs()
            순열.pop()

dfs()