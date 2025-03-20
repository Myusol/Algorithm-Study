ca=['c=','c-','dz=','d-','lj','nj','s=','z=']
w=input()
for c in ca:
    w=w.replace(c,'0')
print(len(w))