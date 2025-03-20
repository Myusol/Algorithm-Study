n = int(input())

def star(k):
    if k == 1:
        return ['*']

    arr = star(k//3) 
    new_star = []  
    
    for i in arr:
        new_star.append(i*3)
    for i in arr:
        new_star.append(i+' '*(k//3)+i)
    for i in arr:
        new_star.append(i*3)
    return new_star

print('\n'.join(star(n)))