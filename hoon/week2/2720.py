T = int(input())
for _ in range(T):
    c = int(input())
    # 쿼터(25센트)
    q = c // 25
    rem = c % 25
    # 다임(10센트)
    d = rem // 10
    rem = rem % 10
    # 니켈(5센트)
    n = rem // 5
    # 페니(1센트)
    p = rem % 5
    print(q, d, n, p)