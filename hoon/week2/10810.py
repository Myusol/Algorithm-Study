# a = 5 b = 4 i,j,k = 1 2 3
a,b=map(int,input().split())
list=[0] * a
for _ in range(b):
    i,j,k=map(int,input().split())
    for z in range(i-1,j): # 어차피 인덱스 1씩 짤려서 j는 그대로
        list[z] = k
print(*list)