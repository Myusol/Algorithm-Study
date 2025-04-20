import sys
from collections import deque
input=sys.stdin.readline
F,S,G,U,D=map(int,input().split())
updown=[U,-D]
def bfs(floor):
    queue=deque([(floor,0)])
    visited=[False]*(F+1)
    visited[floor]=True
    while queue:
        floor,cnt=queue.popleft()
        if floor==G:
            print(cnt)
            return
        for act in updown:
            next_floor=floor+act
            if 1<=next_floor<=F and not visited[next_floor]:
                visited[next_floor]=True
                queue.append((next_floor,cnt+1))
    print("use the stairs")
bfs(S)