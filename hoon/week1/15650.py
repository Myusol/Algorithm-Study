N, M = map(int, input().split()) # N = 3 M = 1 출력 = 1 2 3

comb = list(range(1, M + 1)) # list로 1부터 M까지 저장

while True:
    print(" ".join(map(str, comb))) # 공백으로 구분
    i = M - 1 # 인덱스 용
    while i >= 0 and comb[i] == N - (M - 1 - i):
        i -= 1 # 최대값인 맨뒤에서 부터 하나씩 감소
    if i < 0: # -1 되면 멈춤
        break
    comb[i] += 1 # 각 숫자 1씩 증가
    for j in range(i + 1, M): # 왼쪽거를 옮기는 작업이니까 i +1 부터 M까지
        comb[j] = comb[j - 1] + 1 # comb[j]들은 인덱스 왼쪽에 +1 값
