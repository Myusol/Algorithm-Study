l=[input() for _ in range(int(input()))]
cnt=len(l)
for i in range(len(l)):
    t=[]
    w=l[i]
    t.append(w[0])
    for j in range(1, len(w)):
        if w[j]!=w[j-1]:
            t.append(w[j])
    if len(t)!=len(set(t)):
        cnt-=1
print(cnt)