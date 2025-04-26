import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
N, K = map(int, input().split())
fb = [-1, 1, 2]

def hidenseek(s, d):
    time = [INF] * 100001
    q = []
    heapq.heappush(q, (0, s))
    time[s] = 0
    
    while q:
        sec, n = heapq.heappop(q)
        
        if n == d:
            return time[n]
        
        for move in fb:
            if move == 2:
                nsec, next = sec, n * move
            else:
                nsec, next = sec + 1, n + move
            if 0 <= next < 100001 and nsec < time[next]:
                time[next] = nsec
                heapq.heappush(q, (nsec, next))
                
print(hidenseek(N, K))