# 최소 힙 / 실버2
n = int(input())
lis = [] # 정수 리스트
for _ in range(n):
    a = int(input())
    if a > 0:
        lis.append(a)
    elif a ==0:
        if len(lis) == 0:
            print(0)
        else:
            minv = min(lis)
            print(minv)
            lis.remove(minv)