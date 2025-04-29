import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def divide(x, y, N):
    global white, blue
    check = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != check:
                divide(x, y, N//2)
                divide(x + N//2, y, N//2)
                divide(x, y + N//2, N//2)
                divide(x + N//2, y + N//2, N//2)
                return
    if check == 1:
        blue += 1
    elif check == 0:
        white += 1
                
divide(0, 0, N)
print(white)
print(blue)