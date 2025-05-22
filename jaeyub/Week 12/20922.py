N, K = map(int, input().split())
number = list(map(int, input().split()))

answer = 0
start, end = 0, 0
count = [0] * (max(number)+1)

while end < N:
    if count[number[end]] < K:
        count[number[end]] += 1
        end += 1
    else:
        count[number[start]] -= 1
        start += 1
    answer = max(end-start, answer)

print(answer)