# 오큰수 / 골드4
# nge 위치에서 오른쪽 중에 큰수 젤왼쪽 구하기
# 스택으로 1보다 클때까지 검사(pop 써서)
# [3, 5, 2, 7]
import sys
input = sys.stdin.readline
n = int(input())
lis = list(map(int,input().split()))
result = [-1] * n # 기본 -1
stack = []
for i in range(n):
    while stack and lis[stack[-1]] < lis[i]:
# 스택에 값이 있고 스택의 마지막에 저장된 인덱스 원소가
# 현재 원소보다 작으면 실행
        index = stack.pop()
        result[index] = lis[i]
    stack.append(i) # 처음에 반복 안하고 0 추가
print(*result)


# import sys
# input = sys.stdin.readline
# n = int(input())
# lis = list(map(int,input().split()))
# result = []
# for i in range(len(lis)):
#     if lis[i] == max(lis):
#         result.append(-1)
#     else:
#         for j in range(i+1,len(lis)):
#             if lis[i] < lis[j]:
#                 result.append(lis[j])
#                 break
#             else:
#                 pass
# print(*result)