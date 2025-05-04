N=int(input())
paper=[list(map(int,input().split(' '))) for _ in range(N)]

minus_one = 0
zero = 0
plus_one = 0

def dnc(x, y, n):
    global minus_one,zero,plus_one
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                check = 3
                break

    if check == 3:
        n = n // 3
        for nx in range(x,x+3*n,n):
            for ny in range(y,y+3*n,n):
                dnc(nx,ny,n)

    elif check == -1:
        minus_one+=1
    elif check == 0:
        zero+=1
    else:
        plus_one+=1

dnc(0,0,N)
print(minus_one)
print(zero)
print(plus_one)