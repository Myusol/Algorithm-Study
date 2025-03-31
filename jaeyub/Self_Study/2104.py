import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
sum_list = [0]
for i in range(N) :
    sum_list.append(sum_list[-1] + num_list[i])

stack = []
max_num = 0

for i in range(N) :
    idx = i
    while stack and stack[-1][1] >= num_list[i] :
        idx, height = stack.pop()
        max_num = max(max_num, (sum_list[i] - sum_list[idx])*height)
    stack.append((idx, num_list[i]))

while stack :
    idx, height = stack.pop()
    max_num = max(max_num, (sum_list[-1] - sum_list[idx])*height)

print(max_num)
