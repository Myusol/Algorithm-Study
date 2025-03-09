N, S = map(int, input().split()) # 5, 0
numbers = list(map(int, input().split())) # -7, -3, -2, 5, 8
count = 0

# for k in range(1,N-1,1):
#     for i in range(2, N, 1): # 묶는 숫자 개수
#         for j in range(0, N-1, 1): # 인덱스번호
#             sumarr = sum(numbers[j]+numbers[j+1])
#             if sumarr == S:
#                 count += 1

# print (count)

def dfs(idx, total, cnt):
    if idx == N:
        return 1 if cnt > 0 and total == S else 0
    return dfs(idx + 1, total + numbers[idx], cnt + 1) + dfs(idx + 1, total, cnt)

count = dfs(0, 0, 0)
print(count)