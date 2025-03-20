from collections import deque

N,M = map(int,input().split())
deq = deque([i for i in range(1,N+1)])
num_list = list(map(int,input().split()))

count = 0
for num in num_list:
    if deq[0] == num:
        deq.popleft()
    else:
        if deq.index(num) <= len(deq)//2:
            count+=deq.index(num)
            deq.rotate(deq.index(num)*-1)
            deq.popleft()
        else:
            count+=len(deq)-deq.index(num)
            deq.rotate(len(deq)-deq.index(num))
            deq.popleft()

print(count)


