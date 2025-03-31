def cantor(k):
    if k==0:
        return "-"
    else:
        line2 = cantor(k-1)
        line = line2 + ' '*(3**(k-1)) + line2
        return line


while True:
    try:
        N = int(input())
        print(cantor(N))
    except:
        break