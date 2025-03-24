import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
Id = {}
Name = {}
for i in range(1, N + 1):
    pokemon = input()
    Id[i] = pokemon
    Name[pokemon] = i

for _ in range(M):
    x = input()
    if x.isdigit():
        print(Id[int(x)])
    else:
        print(Name[x])