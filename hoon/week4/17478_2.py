# 재귀함수가 뭔가요? / 실버5
import sys
input = sys.stdin.readline
n = int(input())
def recursive_func(n, current):
    # 현재 깊이만큼 언더스코어("____")를 출력하며 질문을 출력
    print("____" * current + '"재귀함수가 뭔가요?"')
    
    if current == n:
        # 가장 깊은 재귀 단계에서는 간단한 답변 출력
        print("____" * current + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        # 재귀의 중간 단계에서는 이야기 형식의 문장을 출력
        print("____" * current + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print("____" * current + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print("____" * current + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 한 선비가 찾아와서 물었어.")
        # 재귀 호출: 재귀 깊이를 한 단계 증가시킴
        recursive_func(n, current + 1)
    
    # 재귀 호출이 끝난 후, 답변 문장을 역순으로 출력 (재귀 종료 시점에 출력)
    print("____" * current + "라고 답변하였지.")
# 첫 줄 출력
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# 재귀 호출 시작: 현재 깊이 0부터 시작
recursive_func(n, 0)