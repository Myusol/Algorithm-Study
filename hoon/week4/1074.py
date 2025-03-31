# Z / 골드5
import sys
input = sys.stdin.readline
n,r,c = map(int, input().split()) # 2**n하고 r = 행 c = 열
def sol(n,r,c): # 3, 7, 7 , 8x8 크기를 4등분하고 7,7찾기
    if n == 0: # 마지막 깊이 멈추기
        return 0  
    else:
        return 2*(r%2)+(c%2) + 4*(sol(n-1, r//2, c//2))
        # r%2=0,1로 위아래 표현         각 각 절반으로 크기 줄이기
        # c%2=0,1로 왼쪽 오른쪽 표현
print(sol(n,r,c))
# 행과 열의 값이 2배가 될 때 숫자가 4배가 된다