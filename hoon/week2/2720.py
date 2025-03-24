T = int(input())
for _ in range(T):
    c = int(input())
    # 쿼터(25센트)
    q = c // 25
    r = c % 25
    # 다임(10센트)
    d = r // 10
    r = r % 10
    # 니켈(5센트)
    n = r // 5
    # 페니(1센트)
    p = r % 5
    print(q, d, n, p)