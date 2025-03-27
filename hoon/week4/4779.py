# 칸토어 집합 / 실버3
# n의 3승만큼 - 만들고 3등분함 중간을 공백으로 하고
# 또 3등분해서 중간에 공백을 만들고
# 또 3등분해서 중간에 공백을 만든다
import sys
input = sys.stdin.readline
def kan(n):
    if n == 0:
        return '-'
    prev = kan(n-1)
    return prev + ' ' * len(prev) + prev
for line in sys.stdin:
    n = int(line)
    print(kan(n))