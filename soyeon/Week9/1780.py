import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def count_paper(x, y, size):
    num = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != num:
                new_size = size // 3
                for dx in range(3):
                    for dy in range(3):
                        count_paper(x + dx * new_size, y + dy * new_size, new_size)
                return
    counts[num + 1] += 1  # -1 → 0, 0 → 1, 1 → 2

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

counts = [0, 0, 0]
count_paper(0, 0, N)

for c in counts:
    print(c)