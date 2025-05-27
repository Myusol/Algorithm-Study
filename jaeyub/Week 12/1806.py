N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0,0
sum = 0
len=100000

while True:
    if sum >= S:
        len=min(len,right-left)
        sum -= numbers[left]
        left +=1
    elif right == N:
        break
    else:
        sum += numbers[right]
        right+=1

if len == 100000:
    print(0)
else:
    print(len)