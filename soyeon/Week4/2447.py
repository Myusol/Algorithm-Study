def star(N) :
    if N ==  3 :
        return ['***', '* *', '***']
    else :
        star_arr = star(N//3)
        a = []

        for i in star_arr :
            a.append(i*3)

        for i in star_arr :
            a.append(i + " "*(N//3) + i)
        
        for i in star_arr :
            a.append(i*3)

        return a

N = int(input())
print("\n".join(star(N)))