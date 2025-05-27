N, M = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 1
answer = 0

while right<=N and left<=right:
    total = sum(numbers[left:right])

    if total == M:
        answer += 1
        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(answer)