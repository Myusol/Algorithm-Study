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
    if i < 0:
        if n < 0:
            return
        L_copy = L.copy()
        L_copy[10] += n
        diff = calc_diff(A, L_copy)
        if diff < max_diff:
            return
        if diff > max_diff:
            max_diff = diff
            answer = L_copy
        elif diff == max_diff:
            for j in range(10, -1, -1):
                if L_copy[j] > answer[j]:
                    answer = L_copy
                    break
                elif L_copy[j] < answer[j]:
                    break
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


print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))