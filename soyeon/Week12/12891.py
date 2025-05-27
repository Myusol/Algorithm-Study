import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())

required = [a, c, g, t]
curr = [0, 0, 0, 0]

for i in range(p):
    if dna[i] == 'A':
        curr[0] += 1
    elif dna[i] == 'C':
        curr[1] += 1
    elif dna[i] == 'G':
        curr[2] += 1
    elif dna[i] == 'T':
        curr[3] += 1

result = 0
if all(curr[i] >= required[i] for i in range(4)):
    result += 1

for i in range(p, s):
    # 빠지는 문자
    out = dna[i - p]
    if out == 'A':
        curr[0] -= 1
    elif out == 'C':
        curr[1] -= 1
    elif out == 'G':
        curr[2] -= 1
    elif out == 'T':
        curr[3] -= 1

    # 들어오는 문자
    in_ = dna[i]
    if in_ == 'A':
        curr[0] += 1
    elif in_ == 'C':
        curr[1] += 1
    elif in_ == 'G':
        curr[2] += 1
    elif in_ == 'T':
        curr[3] += 1

    if all(curr[i] >= required[i] for i in range(4)):
        result += 1

print(result)