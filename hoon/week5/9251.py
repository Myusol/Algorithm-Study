# LCS / 골드5
import sys
input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()
# lcs[i][j]는 s1의 i번째 문자까지, s2의 j번째 문자까지 비교했을 때
# 만들 수 있는 최장 공통 부분 수열의 길이를 저장
# 테이블 크기는 (len(s1)+1) x (len(s2)+1), 0행과 0열은 공백 상태를 의미
lcs = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
# 문자열의 각 문자를 하나씩 비교하며 DP 테이블 채우기
for i in range(1, len(s1)+1):        # s1의 i번째 문자 (1부터 시작)
    for j in range(1, len(s2)+1):    # s2의 j번째 문자 (1부터 시작)
        # 문자가 같으면: 이전 상태(lcs[i-1][j-1])에 +1
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            # 문자가 다르면: 왼쪽(lcs[i][j-1]) 또는 위쪽(lcs[i-1][j]) 중 큰 값 선택
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
# DP 테이블 중 가장 큰 값을 출력 (즉, LCS의 최대 길이)
# 사실 lcs[len(s1)][len(s2)]와 동일한 값
print(lcs[-1][-1])