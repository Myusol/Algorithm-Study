import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
rec = list(map(int, input().split()))

frame = []
info = dict()

for t, student in enumerate(rec):
    if student in info:
        info[student] = (info[student][0] + 1, info[student][1])
    else:
        if len(frame) < n:
            frame.append(student)
            info[student] = (1, t)
        else:
            remove = sorted(frame, key=lambda x: (info[x][0], info[x][1]))[0]
            frame.remove(remove)
            del info[remove]
            frame.append(student)
            info[student] = (1, t)

print(' '.join(map(str, sorted(frame))))