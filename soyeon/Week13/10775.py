import sys
input = sys.stdin.readline

def find(a) :
    if a == parent[a] :
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a == b :
        return
    if a > b :
        parent[a] = b
    else :
        parent[b] = a

g = int(input().rstrip())
p = int(input().rstrip())

plane = []
for i in range(p) :
    plane.append(int(input().rstrip()))

parent = [i for i in range(g+1)]

c = 0
for i in plane :
    a = find(i)
    if a == 0 :
        break
    union(a, a-1)
    c += 1
print(c)