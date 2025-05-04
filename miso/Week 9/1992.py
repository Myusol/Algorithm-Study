import sys
input = sys.stdin.readline
N = int(input())
video = [list(map(int, list(input().strip()))) for _ in range(N)]

def divide(x, y, N):
    v = video[y][x]
    
    if N == 1:
        print(v, end="")
        return
    
    for i in range(x, x + N):
        for j in range(y, y + N):
            if video[j][i] != v:
                print("(", end="")
                divide(x, y, N//2)
                divide(x + N//2, y, N//2)
                divide(x, y + N//2, N//2)
                divide(x + N//2, y + N//2, N//2)
                print(")", end="")
                return
    print(v, end = "")

divide(0, 0, N)