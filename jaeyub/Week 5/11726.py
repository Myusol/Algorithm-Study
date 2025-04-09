import sys

tile = [0]*1001
tile[1] = 1
tile[2] = 2

n = int(sys.stdin.readline())

for i in range(3,n+1):
    tile[i]= (tile[i-1]+tile[i-2])%10007
print(tile[n])