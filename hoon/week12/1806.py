# 부분합 / 골드4
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
min_length = n + 1 # 전부 다 틀린 경우 및 전체 길이
cnt = 0 # 부분 배열 합
left = 0
for right in range(n):
    cnt += arr[right] # 부분 배열 누적 합
    while cnt >= s:
        min_length = min(min_length, right - left + 1) # 오른쪽 에서 왼쪽 뺀 값이 길이(+ 1 은 인덱스 맞추기용)
        cnt -= arr[left]
        left += 1
if min_length != n + 1: # 하나도 못 찾는 경우가 아니면
    print(min_length)
else: # 하나도 없으면 0 출력
    print(0)