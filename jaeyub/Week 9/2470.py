N = int(input())
water = list(map(int, input().split(' ')))
water.sort()

left = 0
right = N-1

new_water = abs(water[left] + water[right])
answer = [water[left], water[right]]


while left < right:
    sum = water[left] + water[right]
  
    if abs(sum) < new_water:
        new_water = abs(sum)
        answer = [water[left], water[right]]
        if new_water == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(*answer)