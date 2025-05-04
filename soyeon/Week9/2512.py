n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

low = 0
high = max(budgets)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = 0
    for budget in budgets:
        if budget > mid:
            total += mid
        else:
            total += budget

    if total <= m:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)