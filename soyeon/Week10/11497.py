T = int(input())

for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()

    # 양옆 번갈아 배치 -> 인접한 통나무 간의 높이차가 최소화됨
    arr = [0] * N
    left, right = 0, N - 1
    for i in range(N):
        if i % 2 == 0:
            arr[left] = logs[i]
            left += 1
        else:
            arr[right] = logs[i]
            right -= 1

    max_diff = 0
    for i in range(N):
        diff = abs(arr[i] - arr[(i+1)%N])
        max_diff = max(max_diff, diff)

    print(max_diff)