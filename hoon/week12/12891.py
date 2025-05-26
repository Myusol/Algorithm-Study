# DNA 비밀번호 / 실버2
import sys
input = sys.stdin.readline
s, p = map(int, input().split())
dna = input()
A, C, G, T = map(int, input().split())
# 현재 부분 문자열에서 실시간 카운트
current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
# 최소 몇 번 나와야 하는지 지정
check = {'A': A, 'C': C, 'G': G, 'T': T}
cnt = 0
# 초기 윈도우 설정 (0 ~ p-1)
for i in range(p):
    current[dna[i]] += 1
# 현재 부분 문자열이 비밀번호 조건 인지 확인
# current 인덱스가 check 인덱스를 넘었는지 확인(처음 한번)
if all(current[x] >= check[x] for x in "ACGT"):
    cnt += 1
# 슬라이딩 윈도우
for right in range(p, s):
    current[dna[right]] += 1 # 새로 들어온 문자(오른쪽 으로 이동)
    current[dna[right - p]] -= 1 # 빠지는 문자(왼 쪽 으로 이동)
    if all(current[x] >= check[x] for x in "ACGT"):
        cnt += 1
print(cnt)