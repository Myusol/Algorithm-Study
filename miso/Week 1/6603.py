# 집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

def lt():
    if len(l)==6:
        print(' '.join(map(str, l)))
        return
    for i in range(0, k):
        if not l or l[-1] < S[i]:
            l.append(S[i])
            lt()
            l.pop()

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0 :
        break
    S = arr[1:]
    l=[]
    lt()
    print()
    
