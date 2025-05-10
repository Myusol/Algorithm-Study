N = int(input())
words = [input() for _ in range(N)]

weight = {}

for word in words:
    length = len(word)
    for i, ch in enumerate(word):
        w = 10 ** (length - i - 1)
        if ch in weight:
            weight[ch] += w
        else:
            weight[ch] = w

sorted_weights = sorted(weight.values(), reverse=True)

answer = 0
digit = 9
for w in sorted_weights:
    answer += w * digit
    digit -= 1

print(answer)