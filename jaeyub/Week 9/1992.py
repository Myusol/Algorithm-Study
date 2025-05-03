N=int(input())
video=[list(map(int,input())) for _ in range(N)]

def quad_tree(x, y, n):
    check = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != video[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        quad_tree(x, y, n)
        quad_tree(x, y + n, n)
        quad_tree(x + n, y, n)
        quad_tree(x + n, y + n, n)
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

quad_tree(0,0,N)