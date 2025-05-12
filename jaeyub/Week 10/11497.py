T=int(input())
for _ in range(T):
    N=int(input())
    log=list(map(int,input().split()))
    log.sort()

    min_level = log[2]-log[0]

    for i in range(3,N):
        if log[i]-log[i-2] > min_level:
            min_level = log[i]-log[i-2]
    print(min_level)