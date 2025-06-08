# n발 쏘고 n발
# 0~10 많이 맞춘 사람이 그 점수만 획득 추가 획득은 x
# 만약 둘이 하나의 점수에 맞춘 횟수가 같다면 앞 사람 점수
# 어피치가 10 ~ 0 까지 맞춘 횟수가 주어짐
# 라이언이 같이 n을 쏴서 이기는 리스트 return 비기거나 지면 -1
import copy

def solution(n, info):
    best_diff = 0
    best_alloc = [-1]  # 초기에는 이길 방법이 없다고 가정

    # 현재까지의 화살 배분을 저장할 배열
    curr = [0] * 11

    # 점수 계산 함수
    def calc_diff():
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            if info[i] == 0 and curr[i] == 0:
                # 둘 다 맞힌 화살이 없으면 아무도 점수를 가져가지 않음
                continue
            if curr[i] > info[i]:
                ryan_score += 10 - i
            else:
                apeach_score += 10 - i
        return ryan_score - apeach_score

    # 백트래킹: index는 0(10점)부터 10(0점)까지
    def dfs(index, arrows_left):
        nonlocal best_diff, best_alloc

        # 마지막 구역(0점)까지 왔으면 남은 화살을 모두 할당하고 결과 계산
        if index == 10:
            curr[10] = arrows_left
            diff = calc_diff()
            if diff > 0:
                # 더 큰 점수 차이가 나면 무조건 갱신
                if diff > best_diff:
                    best_diff = diff
                    best_alloc = copy.deepcopy(curr)
                # 점수 차이가 같다면, 더 낮은 점수(인덱스가 큰 쪽)에 화살을 많이 할당한 쪽을 택함
                elif diff == best_diff:
                    # 인덱스 10부터 0까지 순서대로 비교
                    for i in range(10, -1, -1):
                        if curr[i] > best_alloc[i]:
                            best_alloc = copy.deepcopy(curr)
                            break
                        elif curr[i] < best_alloc[i]:
                            break
            # 할당했던 화살 초기화
            curr[10] = 0
            return

        # 1) 해당 점수(10 - index)를 가져오기 위해 필요한 화살 개수
        needed = info[index] + 1
        # 1-1) 화살이 충분하면 “이긴다” 선택
        if arrows_left >= needed:
            curr[index] = needed
            dfs(index + 1, arrows_left - needed)
            curr[index] = 0

        # 2) “포기한다” 선택 (0발 할당)
        #    단순히 curr[index]=0 상태로 다음 단계로 넘어간다
        dfs(index + 1, arrows_left)

    dfs(0, n)

    return best_alloc