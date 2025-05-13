from itertools import combinations

N=int(input())
food=[list(map(int,input().split())) for _ in range(N)]
result=1e9
for combination in [combinations(food,i) for i in range(1,N+1)]:
    for c in combination:
        S,B=1,0
        for s,b in c:
            S*=s
            B+=b
        result=min(result, abs(S-B))
print(result)