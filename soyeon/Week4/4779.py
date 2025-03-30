import sys
input = sys.stdin.readline

def sep(n, i, j) :
    if n == 0 :
        return

    length = (j - i + 1) // 3
    sep(n - 1, i, i + length - 1)
    for k in range(i + length, i + length * 2):
        ans[k] = ' '
    sep(n - 1, i + length * 2, i + length * 3 - 1)

while True:
    try:
        n = int(input())
        ans = ['-'] * (3 ** n)
        sep(n, 0, 3 ** n - 1)
        print(''.join(ans))
    except:
        break