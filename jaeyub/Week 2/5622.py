alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

S=input()
time=0

for s in S:
    for i,a in enumerate(alphabet):
        if s in a:
            time += (i+3)
print(time)