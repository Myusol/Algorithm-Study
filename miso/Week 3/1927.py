import heapq
import sys
heap=[]
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    if n==0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,n)