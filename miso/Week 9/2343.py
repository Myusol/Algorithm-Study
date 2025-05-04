import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lecture = list(map(int, input().split()))

def binary_search():
    s, e = max(lecture), sum(lecture)
    result = 0
    
    while s <= e:
        m = (s + e) // 2
        cnt = 1
        total = 0
        for i in lecture:
            if total + i > m:
                cnt += 1
                total = i
            else:
                total += i
        if cnt <= M:
            result = m
            e = m - 1
            
        else:
            s = m + 1
            
    return result

print(binary_search())