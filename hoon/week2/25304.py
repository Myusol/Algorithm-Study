x=int(input())
n=int(input())

total = 0 # 누적을 위해서 밖에 선언
for _ in range(n): # _ 반복만 원할때
    a,b=map(int,input().split())
    total += a*b
if total == x:
    print("Yes")
else:
    print('No')