lis=[]
max_val = -float('inf')
max_pos = (0, 0)
for _ in range(9):
    z = list(map(int,input().split()))
    lis.append(z)
for i in range(len(lis)):
    for j in range(len(lis[i])):
        if lis[i][j] > max_val:
            max_val = lis[i][j]
            max_pos = i+1,j+1
print(max_val)
print(max_pos[0],max_pos[1])