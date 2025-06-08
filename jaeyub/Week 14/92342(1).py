def calc_diff(A, L):
    A_score = 0
    L_score = 0
    for i in range(11):
        if A[i] == L[i] == 0:
            continue
        if A[i] >= L[i]:
            A_score += 10 - i
        else:
            L_score += 10 - i
    return L_score - A_score

def DFS(i, n, A, L):
    global answer, max_diff
    if n < 0:
        return

    if i < 0:
        diff = calc_diff(A, L)
        if diff <= 0:
            return
        if diff > max_diff:
            max_diff = diff
            answer = [L[i] for i in range(11)]
            answer[10] += n            
        return

    L[10-i] = A[10-i]+1
    DFS(i-1, n-L[10-i], A, L)

    L[10-i] = 0
    DFS(i-1, n, A, L)

def solution(n, A):
    global answer, max_diff
    answer = [-1]
    max_diff = 0
    DFS(10, n, A, [0 for _ in range(11)])
    return answer