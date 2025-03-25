# 재귀함수가 뭔가요? / 실버5
import sys
input = sys.stdin.readline
n = int(input())
def answer(n):
  li = []
  for i in range(0,n+1):
    if i == n: # n과 최종적으로 같을때 출력할것 _ 는 가장 길게 출력됨
      print(f'{i*4*"_"}"재귀함수가 뭔가요?"')
      print(f'{i*4*"_"}"재귀함수는 자기 자신을 호출하는 함수라네"')
      li.append(i*4)
    else:  # 그외는 이것만 계속 출력
     print(f'{i*4*"_"}"재귀함수가 뭔가요?"')
     print(f'{i*4*"_"}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
     print(f'{i*4*"_"}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
     print(f'{i*4*"_"}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
     li.append(i*4)
#   li.sort() # 들여쓰기 수치를 오름차순으로 정렬
  for j in range(len(li)-1,0,-1): # 마지막부터 0까지 출력
    print(f'{li[j]*"_"}라고 답변하였지.')
  return "라고 답변하였지." # 마지막엔 _ 없는 마지막 출력
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
print(answer(n))