# GPT의 도움 + 블로그 참고 + 혼자 힘으로 못함.... 유감

import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N  # 기본적으로 -1로 초기화
stack = []  # 스택에는 오큰수를 찾지 못한 원소들의 "인덱스"를 저장

for i in range(N):
    # 현재 숫자가 스택에 있는 인덱스의 값보다 크면, 오큰수 갱신
    while stack and num_list[stack[-1]] < num_list[i]:
        idx = stack.pop()
        answer[idx] = num_list[i]

    # 현재 인덱스를 스택에 추가
    stack.append(i)

print(*answer)
