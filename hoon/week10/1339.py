# 단어 수학 / 골드4
import sys
input = sys.stdin.readline
N = int(input())
S = [input().strip() for _ in range(N)]
words = {}  # 단어별 값 지정
# 값들의 각 자릿수 값 주기
for s in S: 
    x = len(s) - 1  # 왼쪽에서 부터 시작(만의 자리면 10** 4)
    for i in s:
        if i in words:
            words[i] += 10 ** x # 있으면 x만큼 제콥해서 더함
        else:
            words[i] = 10 ** x # 없으면 x만큼 제곱해서 넣음
        x -= 1 # 다음 자릿수
words_sort = sorted(words.values(), reverse=True) # 딕셔너리의 value만 내림차순으로 정렬
result = 0
num = 9
for k in words_sort:
    result += k * num # 내림차순 한거에 9 부터 하나씩 곱해서 더함
    num -= 1
print(result)