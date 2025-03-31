import sys
n,m=map(int,sys.stdin.readline().split())
poke={}
pokel=[]
for i in range(n):
    name=sys.stdin.readline().rstrip()
    poke[name]=i
    pokel.append(name)
for _ in range(m):
    i=sys.stdin.readline().rstrip()
    if not i.isalpha():
        i=int(i)
        print(pokel[i-1])
    else:
        print(poke.get(i)+1)