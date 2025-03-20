croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
x = input()

for c in croatia:
    x = x.replace(c,'_')

print(len(x))