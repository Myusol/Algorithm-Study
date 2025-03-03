from itertools import permutations

N, M = map(int, input().split())
numbers = list(range(1, N + 1))

for perm in permutations(numbers, M):
    print(" ".join(map(str, perm)))

# 위 코드에 대한 공부+다른 방법 연구