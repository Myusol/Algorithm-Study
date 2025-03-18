# 유효성 변수를 활용해 오큰수를 발견하면 리스트에 추가하고, 발견하지 못하면 -1
import sys
n=int(input())
list=list(map(int,sys.stdin.readline().split()))
stack=[]
for i in range(n):
    found=False
    for j in range(i+1,n):
        if list[i]<list[j]:
            stack.append(list[j])
            found=True
            break
    if not found:
        stack.append(-1)
print(*stack)

#######

# 블로그 참고
import sys
n=int(input())
list=list(map(int,sys.stdin.readline().split()))
stack=[] # 오큰수를 찾지 못한 인덱스 저장하는 리스트
ans=[-1]*n
for i in range(n):
    while stack and list[i]>list[stack[-1]]: # 스택이 비어있지 않고, 현재 숫자가 스택의 top보다 크면
        ans[stack.pop()]=list[i] # 현재 숫자가 오큰수가 되고 그 인덱스 pop
    stack.append(i) # 현재 숫자의 인덱스를 스택에 추가
print(*ans)