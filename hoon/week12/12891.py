# DNA 비밀번호 / 실버2
import sys
input = sys.stdin.readline

# 입력
s, p = map(int, input().split())
dna = input().strip()
A, C, G, T = map(int, input().split())

# 현재 윈도우의 문자 개수 저장
current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
check = {'A': A, 'C': C, 'G': G, 'T': T}
cnt = 0

# 초기 윈도우 설정 (0 ~ p-1)
for i in range(p):
    current[dna[i]] += 1

# 조건 만족하면 카운트
def is_valid():
    return all(current[x] >= check[x] for x in "ACGT")

if is_valid():
    cnt += 1

# 슬라이딩 윈도우
for i in range(p, s):
    current[dna[i]] += 1        # 새로 들어온 문자
    current[dna[i - p]] -= 1    # 윈도우에서 빠진 문자
    if is_valid():
        cnt += 1
print(cnt)