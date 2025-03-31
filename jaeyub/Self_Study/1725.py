import sys

input = sys.stdin.readline

N = int(input())
histogram = [int(input()) for _ in range(N)]

stack = []
max_area = 0
for i in range(N):
    idx = i
    while stack and stack[-1][1] > histogram[i]:
        idx, height = stack.pop()
        new_area = (i - idx) * height
        max_area = max(max_area, new_area)
    stack.append([idx, histogram[i]])

while stack:
    idx, height = stack.pop()
    new_area = (N - idx) * height
    max_area = max(max_area, new_area)

print(max_area)