while True:
    n = int(input()) # 10
    if n == 0:
        exit()

    m = n * 2
    count = 0
    for i in range(n+1, m+1):
        if n <= 1:
            count += 1
            break
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            count += 1

    print(count)