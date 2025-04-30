import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
T = int(input())
        
def hacking(start):
    time = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0
    
    while q:
        sec, hack = heapq.heappop(q)
        
        if time[hack] < sec:
            continue
        
        for next, ns in graph[hack]:
            nsec = sec + ns
            if nsec < time[next]:
                time[next] = nsec
                heapq.heappush(q, (nsec, next))
                
    cnt = 0
    maxt = 0
    for t in time:
        if t != INF:
            cnt += 1
            maxt = max(maxt, t)
    return cnt, maxt

for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    print(*hacking(c))