def solution(n,k):
    number = ''
    answer = 0
    while n:
        number += str(n % k)
        n = n//k
    number = number[::-1]

    number = number.split("0")

    for n in number:
        if len(n)==0:
            continue
        if int(n)<2:
            continue
        is_prime = True
        for i in range(2,int(int(n)**0.5)+1):
            if int(n)%i==0:
                is_prime = False
                break
        if is_prime:
            answer+=1
    return answer

# print(solution(437674,3))
# print(solution(110011,10))