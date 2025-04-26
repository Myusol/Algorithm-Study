import sys
input = sys.stdin.readline

N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]
min_diff = float('inf')

def backtrack(index, sour, bitter, cnt):
    global min_diff
    
    if index == N:
        if cnt > 0:
            min_diff = min(min_diff, abs(sour - bitter))
        return

    backtrack(index + 1, sour * ingredients[index][0], bitter + ingredients[index][1], cnt + 1)

    backtrack(index + 1, sour, bitter, cnt)

backtrack(0, 1, 0, 0)
print(min_diff)