import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    score = []
    
    for _ in range(N):
        score.append(list(map(int, input().split())))
        
    score = sorted(score, key=lambda x: x[0])
    cnt = 1
    interview = score[0][1]
    
    for i in range(N):
        if score[i][1] < interview:
            interview = score[i][1]
            cnt += 1
            
    print(cnt)