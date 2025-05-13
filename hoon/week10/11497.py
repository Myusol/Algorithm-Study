# 통나무 건너뛰기 / 실버1
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    tong = [0] * N
    left = 0
    right = N - 1
    # 큰 값이 가운데, 양쪽 번갈아 배치
    for i in range(N):
        if i % 2 == 0:
            tong[left] = logs[i]
            left += 1
        else:
            tong[right] = logs[i]
            right -= 1
    # 인접 차이 계산 (원형이므로 마지막과 첫 번째도 포함)
    md = 0
    for i in range(N):
        # 절대값 구하기 - abs
        di = abs(tong[i] - tong[(i + 1) % N])
        md = max(md, di)
    print(md)