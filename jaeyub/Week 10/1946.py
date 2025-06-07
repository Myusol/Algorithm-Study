import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    people = []
    for _ in range(N):
        t1 ,t2 = map(int,input().split())
        people.append([t1,t2])
    people.sort(key=lambda x:x[0])

    success = 1
    max_t2 = people[0][1]

    for i in range(1,N):
        if people[i][1] < max_t2:
            max_t2 = people[i][1]
            success+=1
    print(success)
