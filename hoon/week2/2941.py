#2941 크로아티아 알파벳 / 실버5
lis = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
count = 0
i = 0
while i < len(word):
    for cro in lis:
        if word[i:i+len(cro)] == cro:
            count += 1
            i += len(cro)
            break
    else:
        count += 1
        i += 1
print(count)