N = int(input())

alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
word_list = []
answer = 0

for _ in range(N):
    word = input()
    word_list.append(word)

for word in word_list:
    for i in range(len(word)):
        alphabet[word[i]] += 10**(len(word)-i-1)

number = []
for value in alphabet.values():
    if value > 0:
        number.append(value)

number.sort(reverse=True)
for i in range(len(number)):
    answer += number[i]*(9-i)
print(answer)
