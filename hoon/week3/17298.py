# 오큰수 / 골드4
# nge 위치에서 오른쪽 중에 큰수 젤왼쪽 구하기
import sys
input = sys.stdin.readline
n = int(input())
lis = list(map(int,input().split()))
result = []
for i in range(len(lis)):
    if lis[i] == max(lis):
        result.append(-1)
    else:
        for j in range(i+1,len(lis)):
            if lis[i] < lis[j]:
                result.append(lis[j])
                break
            else:
                pass
print(*result)