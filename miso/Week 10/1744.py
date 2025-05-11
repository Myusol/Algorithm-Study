import sys
input = sys.stdin.readline
N = int(input())

if N == 1:
    print(int(input()))
    
else:
    p = []
    m = []
    result = 0, 0
    
    for _ in range(N):
        num = int(input())
        if num <= 0:
            m.append(num)
        elif num > 1:
            p.append(num)
        else:
            result += 1
            
    m.sort()
    p.sort(reverse=True)
    
    if N != 1:
        i = 0
        mN = len(m)
        if mN % 2 == 1:
            mN = mN - 1
            result += m[-1]
        while i < mN:
            result += m[i] * m[i + 1]
            i += 2

        j = 0
        pN = len(p)
        if pN % 2 == 1:
            pN = pN -1
            result += p[-1]
        while j < pN:
            result += p[j] * p[j + 1]
            j += 2
            
        print(result)