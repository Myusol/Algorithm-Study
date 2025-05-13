import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(N)]

    # 서류 등수 기준으로 정렬
    applicants.sort()

    cnt = 1  # 첫 번째는 무조건 선발
    best_interview = applicants[0][1]

    for i in range(1, N):
        if applicants[i][1] < best_interview:
            cnt += 1
            best_interview = applicants[i][1]

    print(cnt)