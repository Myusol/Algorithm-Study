import sys

def hanoi(N,start,end,other):
    if N == 1:
        print(start, end)
        return
    else:
        hanoi(N-1,start,other,end)
        print(start, end)
        hanoi(N-1,other,end,start)

N = int(sys.stdin.readline())
print(2**N-1)
hanoi(N,1,3,2)