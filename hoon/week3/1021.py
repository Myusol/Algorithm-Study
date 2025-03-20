# 회전하는 큐 / 실버3
from collections import deque
a,b = map(int,input().split())
targets = list(map(int,input().split()))
dq = deque(range(1,a+1)) # 일단 deque로 숫자대로 가득채우기
count = 0
for target in targets: # 하나씩 찾아보기
    idx = dq.index(target) # 인덱스는 반복하면서 각 타겟의 위치
    if idx <= len(dq) - idx: # target 인덱스랑 전체 길이를 비교해서 인덱스 숫자가 낮다면 왼쪽으로 실행
        dq.rotate(-idx) # 왼쪽으로 회전 시킬것
        count += idx # 회전한 만큼 플러스
    else:
        dq.rotate(len(dq) - idx)
        count += (len(dq)- idx)
    dq.popleft() # 맨 왼쪽 타겟을 제거하고 다시 진행
print(count)
# 1. deque로 총 길이만큼 만든다
# 2. 타겟을 받은대로 하나씩 반복을 한다
# 3. 타겟의 인덱스를 받고 총길이를 기준으로 더 낮은 쪽으로 회전(rotate)한다.
# 4. 이때 회전은 idx 만큼 할 것이라서 그만큼 count에 추가 해준다
# 5. 위 연산이 끝나면 무조건 왼쪽 끝에 원소가 있을것이고 popleft를 써서 맨앞을 삭제 시키고
# 6. 다시 반복을 하면 targets에 들어온 수를 최소한의 움직임으로 처리한다