n = int(input())

def star(k):
    if k == 3:
        return ['  *  ',
                ' * * ',
                '*****']
    
    arr = star(k//2)
    new_star = []
    for i in arr:
        new_star.append(' '*(k//2)+ i+' '*(k//2))
    for i in arr:
        new_star.append(i+' '+i)

    return new_star

print('\n'.join(star(n)))