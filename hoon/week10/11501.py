# 주식 / 실버2
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split())) 
    max_price = 0
    profit = 0
    # prices를 뒤에서 부터 확인
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        # 현 시점 최고가 에서 현재 금액 차익을 누적 저장
        else:
            profit += max_price - price
    print(profit)