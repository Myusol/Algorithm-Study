from itertools import combinations

n, m = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(list(map(int, input().split())))

house = []
chicken = []
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 :
            house.append((i, j))
        elif arr[i][j] == 2 :
            chicken.append((i, j))
pickup = list(combinations(chicken, m))
ans = [0]*len(pickup)

for i in house :
    for j in range(len(pickup)) :
        result = 100000
        for k in pickup[j] :
            result = min(result, abs(i[0] - k[0]) + abs(i[1] - k[1]))
        ans[j] += result
    

print(min(ans))