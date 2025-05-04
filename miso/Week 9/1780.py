import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
mo, z, po = 0, 0, 0

def divide(x, y, N):
    global mo, z, po
    v = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != v:
                for n in range(3):
                    for m in range(3):
                        divide(x + (N//3) * n, y + (N//3) * m, N//3)
                return
    if v == -1:
        mo += 1
    elif v == 0:
        z += 1
    else:
        po += 1

divide(0, 0, N)
print(mo, z, po, sep='\n')