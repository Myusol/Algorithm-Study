n = int(input())
data = [list(input()) for _ in range(n)]

def compress(x, y, size):
    first = data[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if data[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        print(first, end='')
    else:
        print('(', end='')
        half = size // 2
        compress(x, y, half)
        compress(x, y + half, half)
        compress(x + half, y, half)
        compress(x + half, y + half, half)
        print(')', end='')

compress(0, 0, n)