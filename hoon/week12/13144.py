# List of Unique Numbers / 골드4
n = int(input())
arr = list(map(int, input().split()))
count = [0] * 100001
left = 0
answer = 0
for right in range(n):
    count[arr[right]] += 1
    # 중복이 있으면 left를 이동
    while count[arr[right]] > 1:
        count[arr[left]] -= 1
        left += 1
    # 현재 윈도우 내에서 가능한 부분 배열의 개수 더하기
    answer += (right - left + 1)
print(answer)