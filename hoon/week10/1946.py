# 신입 사원 / 실버1
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    jiwon = [tuple(map(int, input().split())) for _ in range(N)]
    # 서류 순위 기준 정렬
    jiwon.sort()
    count = 1  # 첫 번째는 무조건 선발
    bi = jiwon[0][1]  # 첫 면접 순위
    for i in range(1, N):
        if jiwon[i][1] < bi:
            count += 1
            bi = jiwon[i][1]  # 면접 최소 순위 갱신
    print(count)