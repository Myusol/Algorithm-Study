N,S = map(int, input().split())

arr = list(map(int,input().split()))

combination = []
cnt = 0

def dfs(i):
    global cnt
    if sum(combination) == S and len(combination) > 0:
        cnt+=1

    for j in range(i,N):
        combination.append(arr[j])
        dfs(j+1)
        combination.pop()

dfs(0)
print(cnt)