S_list = []

while True:
    array = list(map(int, input().split()))
    k = array[0]
    if k == 0 :
        break
    S = array[1:]
    S_list.append(S)


조합 = []
def dfs():
    if len(조합) == 6:
        print(" ".join(map(str, 조합)))
        return
    for i in S:
        if i not in 조합:
            if len(조합) == 0 or 조합[-1] < i :
                조합.append(i)
                dfs()
                조합.pop()

for S in S_list:
    dfs()
    print()

