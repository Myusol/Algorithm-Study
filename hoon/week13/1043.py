# 거짓말 / 골드4
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
knowList = set(input().split()[1:]) # 처음 숫자는 진실을 아는 사람 수니까 그 뒤부터
parties = []
for _ in range(m):
    parties.append(set(input().split()[1:])) # 맨 앞 숫자는 인원 수 니까
# 지식 전파
for _ in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)
cnt = 0
# 진실을 아는 사람이 없는 파티만 count
for party in parties:
    if party & knowList:
        continue
    cnt += 1
print(cnt)
'''
& 이거는 set 연산자로서 교집합을 뜻함 저걸 사용하려면
list(set(a) & set(b)) 이런식으로 변환 필요
'''