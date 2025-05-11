N = int(input())
pos, neg = [], []
ones = 0
zero = 0

for _ in range(N):
    x = int(input())
    if x > 1:
        pos.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zero += 1
    else:
        neg.append(x)

# 양수는 큰 수부터, 음수는 작은 수부터 정렬
pos.sort(reverse=True)
neg.sort()

answer = 0

# 양수 두 개씩 묶기
for i in range(0, len(pos) - 1, 2):
    answer += pos[i] * pos[i + 1]
if len(pos) % 2 == 1:
    answer += pos[-1]

# 음수 두 개씩 묶기
for i in range(0, len(neg) - 1, 2):
    answer += neg[i] * neg[i + 1]
if len(neg) % 2 == 1:
    # 음수가 하나 남았는데 0이 있으면 제거 가능
    if zero == 0:
        answer += neg[-1]

# 1은 모두 그냥 더하기
answer += ones

print(answer)