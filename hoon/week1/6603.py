# K = 7 S = 1,2,3,5,8,13,21,34
# 모든 조합의 수를 구해라
first_case = True
while True:
    parts = input().split()
    k = int(parts[0])

    if k == 0: # 0이면 끝
        break

    if not first_case: # 빈줄 출력
        print()
    S = list(map(int, parts[1:]))
    for i1 in range(0, k - 5):
        for i2 in range(i1 + 1, k - 4):
            for i3 in range(i2 + 1, k - 3):
                for i4 in range(i3 + 1, k - 2):
                    for i5 in range(i4 + 1, k - 1):
                        for i6 in range(i5 + 1, k):
                            print(S[i1], S[i2], S[i3], S[i4], S[i5], S[i6])
    first_case = False