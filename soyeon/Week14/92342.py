def solution(n, info):
    from copy import deepcopy

    max_diff = 0
    answer = [-1]
    
    def dfs(idx, arrows_left, lion_info):
        nonlocal max_diff, answer

        if idx == 11:
            if arrows_left > 0:
                lion_info[10] += arrows_left  # 남은 화살은 0점에 다 쏨

            # 점수 계산
            apeach_score, lion_score = 0, 0
            for i in range(11):
                if info[i] == 0 and lion_info[i] == 0:
                    continue
                if info[i] >= lion_info[i]:
                    apeach_score += 10 - i
                else:
                    lion_score += 10 - i

            if lion_score > apeach_score:
                diff = lion_score - apeach_score
                if diff > max_diff:
                    max_diff = diff
                    answer = lion_info[:]
                elif diff == max_diff:
                    # 더 낮은 점수를 많이 맞힌 경우를 선택
                    for i in range(10, -1, -1):
                        if lion_info[i] > answer[i]:
                            answer = lion_info[:]
                            break
                        elif lion_info[i] < answer[i]:
                            break

            if arrows_left > 0:
                lion_info[10] -= arrows_left  # 복원

            return

        # 화살 안 쏘는 경우
        dfs(idx + 1, arrows_left, lion_info[:])

        # 화살 쏘는 경우 (이기려면 info[idx] + 1개 이상 필요)
        if arrows_left > info[idx]:
            lion_info[idx] = info[idx] + 1
            dfs(idx + 1, arrows_left - lion_info[idx], lion_info[:])
            lion_info[idx] = 0  # 복원

    dfs(0, n, [0] * 11)

    return answer