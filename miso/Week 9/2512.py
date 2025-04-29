import sys
input = sys.stdin.readline
N = int(input())
budget = list(map(int, input().split()))
M = int(input())

def binary_search():
    s, e = 0, max(budget)
    result = 0
    
    while s <= e:
        m = (s + e) // 2
        total = sum(min(bi, m) for bi in budget)
        if total <= M:
            result = m
            s = m + 1
        else:
            e = m - 1
    
    return result

print(binary_search())