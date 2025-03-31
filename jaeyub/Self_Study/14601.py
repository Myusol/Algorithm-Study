import sys

N = int(input())
length = 2**N
tile = [[0]*length for _ in range(length)]
x,y = map(int,input().split())
tile[length-y][x-1] = -1
num = 0

def check(x,y,len):
    for i in range(x,x+len):
        for j in range(y,y+len):
            if tile[i][j] !=0:
                return False
    return True

def tromino(x,y,len):
    global num
    num+=1
    half = len//2
    if(check(x,y,half)):tile[x+half-1][y+half-1]=num
    if(check(x,y+half,half)):tile[x+half-1][y+half]=num
    if(check(x+half,y,half)):tile[x+half][y+half-1]=num
    if(check(x+half,y+half,half)):tile[x+half][y+half]=num
    if len ==2: return

    tromino(x,y,half)
    tromino(x,y+half,half)
    tromino(x+half,y,half)
    tromino(x+half,y+half,half)


tromino(0,0,length)

for i in range(length):
    for j in range(length):
        print(tile[i][j], end=' ')
    print()
