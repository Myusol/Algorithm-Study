n = int(input())
words = [input() for _ in range(n)]
cnt = 0

for word in words:
    seen = set()
    prev = ''
    is_group_word = True

    for char in word:
        if char != prev:
            if char in seen:
                is_group_word = False
                break
            seen.add(char)
        prev = char
    
    if is_group_word:
        cnt += 1

print(cnt)