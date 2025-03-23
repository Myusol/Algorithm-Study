import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    score=[]
    for j in range(2):
        score.append(list(map(int, sys.stdin.readline().split())))

    if N == 1:
        print(max(score[0][0], score[1][0]))
        continue

    score[0][1] += score[1][0]
    score[1][1] += score[0][0]

    for k in range(2, N):
        score[0][k] += max(score[1][k-1], score[1][k-2])
        score[1][k] += max(score[0][k-1], score[0][k-2])

    print(max(score[0][-1], score[1][-1]))