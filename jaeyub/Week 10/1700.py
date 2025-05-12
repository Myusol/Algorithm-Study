N, K = map(int,input().split())
use = list(map(int,input().split()))
plug = []
answer = 0

for i in range(K):
    if use[i] in plug:
        continue

    if len(plug) < N:
        plug.append(use[i])
        continue

    priority = []
    for p in plug:
        if p in use[i:]:
            priority.append(use[i:].index(p))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    plug.remove(plug[target])
    plug.append(use[i])
    answer += 1

print(answer)