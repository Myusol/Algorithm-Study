T = int(input())
for _ in range(T):
    N = int(input())
    money = list(map(int, input().split()))
    money.reverse()
    max_price = 0
    benefit = 0

    for m in money:
        if m > max_price:
            max_price = m
            continue
        benefit += max_price - m

    print(benefit)