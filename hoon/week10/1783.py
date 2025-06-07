# 병든 나이트 / 실버3
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
# 위 아래로 이동불가 처음 위치 하나만 가능
if N == 1:
    print(1)
# 세로가 2일 경우
# 4번 이하는 이동 방법에 제약이 없으니까 4가 제한
elif N == 2:
    print(min(4, (M + 1) // 2))
# 세로가 3이상, 가로가 7미만 일때
# 4가지 이동 방법 모두 사용하려면 가로가 6이상 꼭 필요함
elif M < 7:
    print(min(4, M))
# 세로가 3이상, 가로가 7이상 일때
# 처음 조건 만족을 위해서 가로2번 이동 2가지 경우를 사용하기 때문에 -2
else:
    print(M - 2)