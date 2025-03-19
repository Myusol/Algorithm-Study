# 25206 너의 평점은 / 실버5
dic = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0}

sc=0
scc=0
for _ in range(20):
    a, b, c = map(str,input().split())
    z = float(b)
    y = c

    if c != 'P':
        sc += z * dic[y]
        scc += z
avg = sc / scc
print(avg)