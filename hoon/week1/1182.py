N, S = map(int, input().split()) # 5, 0
numbers = list(map(int, input().split())) # -7, -3, -2, 5, 8
count = 0

for k in range(1,k-1,1):
    for i in range(2, N, 1): # 묶는 숫자 개수
        for j in range(0, N-1, 1): # 인덱스번호
            sumarr = sum(numbers[j]+numbers[j+1])
            if sumarr == S:
                count += 1

print (count)