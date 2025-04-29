import sys
input = sys.stdin.readline
while True:
    triangle = list(map(int, input().split()))
    if triangle.count(0) == 3:
        break
    else:
        c = max(triangle)
        triangle.remove(c)
        result = c ** 2
        for i in triangle:
            result -= i ** 2
        if result == 0:
            print("right")
        else:
            print("wrong")