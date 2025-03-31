# 빈도 정렬 / 실버3
n, c = map(int,input().split())
lis = list(map(int,input().split()))
dic = {} # 횟수 저장용
dicin = {} # 인덱스 저장용
for i, num in enumerate(lis):
    if num in dic:
        dic[num] += 1 # 횟수 추가
    else:
        dic[num] = 1 # 처음 만나면 1
        dicin[num] = i # 처음 만나면 1
unique_num = list(dic.keys()) # 중복없이 들어온 순서대로 
unique_num.sort(key=lambda x: (-dic[x], dicin[x])) # 빈도수가 높은 숫자가 앞으로 정렬
# 음수부호(-)를 붙여서 빈도수가 높을때 더 작게 만들어서 앞쪽 정렬 유도
# 
result = []
for num in unique_num:
    result.extend([num] * dic[num]) # 추가된 숫자만큼 result에 추가
print(*result)