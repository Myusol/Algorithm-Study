# 체스말 / 브론즈5
# 킹, 퀸, 룩, 비숍, 나이트, 폰
lis = list(map(int,input().split()))
liss = [] # 1 1 2 2 2 8 있어야될 개수
liss.append(1)
liss.append(1)
liss.append(2)
liss.append(2)
liss.append(2)
liss.append(8)
lisss = []
for i in range(6):
    a = liss[i] - lis[i]
    lisss.append(a)
print(*lisss)