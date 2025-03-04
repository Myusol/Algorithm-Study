N,M = map(int,input().split())
조합 = []

def dfs():
    if len(조합) == M:
        print(" ".join(map(str, 조합)))
        return
    for i in range(1,N+1):
        if i not in 조합:
            if len(조합) == 0 or 조합[-1] < i :
                조합.append(i)
                dfs()
                조합.pop()

dfs()