N,M = map(int,input().split())

ans = 1000000

home_list = []
chicken_list = []

for i in range(N):
    row = list(map(int,input().split()))

    for j in range(N):
        if row[j] == 1:
            home_list.append((i,j))
        elif row[j]==2:
            chicken_list.append((i,j))

def cal_distance(chicken_list):
    chicken_distance = 0

    for home in home_list:
        distance = 100000
        for chicken in chicken_list:
            distance = min(distance, (abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])))
        chicken_distance += distance

    return chicken_distance

visited = [False for _ in range(len(chicken_list))]

def backtrack_comb(idx, arr):
    global ans

    if len(arr)==M:
        ans = min(ans,cal_distance(arr))
        return arr

    for i in range(idx+1, len(chicken_list)):
        if visited[i]==False:
            visited[i] = True
            backtrack_comb(i, arr+[chicken_list[i]])
            visited[i] = False

backtrack_comb(-1,[])
print(ans)