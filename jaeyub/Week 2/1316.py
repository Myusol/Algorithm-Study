N = int(input())
answer = N

for _ in range(N):
    S = input()
    a_list = []
    for c in S:
        if c in a_list and a_list[-1] !=c:
            answer-=1
            break
        else:
            a_list.append(c)

print(answer)