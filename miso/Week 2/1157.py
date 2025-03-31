word=input().upper()
alphabet_list=set(word)
maxcnt=0
alphabet=0
for ai in alphabet_list:
    cnt=word.count(ai)
    if maxcnt<cnt:
        maxcnt=cnt
        alphabet=ai
    elif maxcnt==cnt:
        alphabet='?'
print(alphabet)