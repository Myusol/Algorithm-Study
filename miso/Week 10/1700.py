import sys
input = sys.stdin.readline
N, K = map(int, input().split())
electro = list(map(int, input().split()))
multi = []
cnt = 0

for i in range(K):
    e = electro[i]
    
    if e in multi:
        continue
    
    else:
        if len(multi) < N:
            multi.append(e)
        else:
            late = -1
            lateitem = -1
            for t in multi:
                if t in electro[i + 1:]:
                    idx = electro[i + 1:].index(t)
                    if idx > late:
                        late = idx
                        lateitem = t
                else:
                    lateitem = t
                    break

            multi.remove(lateitem)
            cnt += 1
            multi.append(e)
print(cnt)