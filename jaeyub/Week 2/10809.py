S = input()
alphabet ='abcdefghijklmnopqrstuvwxyz'

for a in alphabet:
    if a in S:
        print(S.index(a), end= ' ')
    else:
        print( -1, end =' ')