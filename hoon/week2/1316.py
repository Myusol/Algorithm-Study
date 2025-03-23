# 1316 그룹 단어 체커 / 실버5
T = int(input())
count = 0
for _ in range(T):
    s = input().strip()
    c = ''
    group = True
    for i in range(len(s)):
        if s[i] != c and s[i] in s[:i]:
            group = False
            break
        c = s[i]
    if group:
        count += 1
print(count)