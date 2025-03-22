w=input()
rw=w[::-1]
if w==rw:
    print(1)
else:
    print(0)
    
#####

w=input()
rw=''.join(reversed(w))
if w==rw:
    print(1)
else:
    print(0)