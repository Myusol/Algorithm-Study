import itertools

x,y = map(int,input().split())

for z in itertools.permutations(list(range(1,x+1)),y):
    print(" ".join(map(str,z)))