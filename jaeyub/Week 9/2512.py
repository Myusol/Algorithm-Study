import sys
input = sys.stdin.readline

N = int(input())
money = list(map(int,input().split()))
total = int(input())

start, end = 0, max(money)

if sum(money) <= total:
    print(max(money))
else:
    while start<=end:
        mid = (start+end) //2
        sum_money = 0
        for i in money:
            sum_money += min(mid,i)

        if sum_money > total:
            end = mid-1
        else:
            start = mid+1
    print(end)