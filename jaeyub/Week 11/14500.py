N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]

tets = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)],
        [(0,1), (1,0), (1,1)],
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)],
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)], 
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)],
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)],
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)],
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)]]

def calc(i,j,tet) :
    score = arr[i][j]
    for di,dj in tet :
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0<= nj < M :
            score += arr[ni][nj]
        else :
            return 0
    return score

answer = 0
for i in range (N) :
    for j in range (M) :
        for tet in tets:
            score = calc(i,j,tet)
            answer = max(score, answer)

print(answer)