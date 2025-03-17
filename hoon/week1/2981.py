# gpt로 정답지

# 1. 최대공약수를 구하는 함수를 정의합니다.
def gcd(a, b):
    # b가 0이 아닐 동안 계속 반복합니다.
    while b != 0:
        # a와 b를, b와 a를 b로 나눈 나머지로 바꿉니다.
        a, b = b, a % b
    # b가 0이 되었을 때, a가 최대공약수입니다.
    return a

# 2. 사용자로부터 입력받은 숫자 개수 N을 읽습니다.
N = int(input())

# 3. while문을 사용하여 N개의 숫자를 입력받아 리스트에 저장합니다.
nums = []      # 입력받은 숫자들을 저장할 리스트
i = 0          # 반복을 위한 인덱스 변수
while i < N:
    # 한 줄에 하나씩 숫자를 입력받아 정수로 변환한 후 리스트에 추가합니다.
    num = int(input())
    nums.append(num)
    i += 1

# 4. 숫자들을 오름차순으로 정렬합니다.
nums.sort()

# 5. 인접한 두 숫자 사이의 차이의 공약수를 구합니다.
# 먼저, 첫 번째 차이로 초기화합니다.
diff = nums[1] - nums[0]
# 인덱스 2부터 N-1까지, 인접한 차이를 하나씩 공약수와 계산합니다.
i = 2
while i < N:
    # 현재 diff와 (nums[i] - nums[i-1])의 최대공약수를 구해 diff에 저장합니다.
    diff = gcd(diff, nums[i] - nums[i-1])
    i += 1

# 6. diff의 약수들 중, 1보다 큰 수들을 찾습니다.
# 약수를 저장할 리스트입니다.
divisors = []
# candidate는 약수를 찾기 위한 후보 숫자입니다.
candidate = 2
# candidate가 diff의 제곱근까지 반복합니다.
limit = int(diff**0.5)
while candidate <= limit:
    # 만약 candidate가 diff의 약수라면,
    if diff % candidate == 0:
        # candidate는 약수이므로 추가합니다.
        divisors.append(candidate)
        # candidate와 짝이 되는 약수도 diff/candidate입니다.
        # 두 수가 같지 않다면 둘 다 추가합니다.
        if candidate != diff // candidate:
            divisors.append(diff // candidate)
    candidate += 1

# 7. diff 자체도 약수이므로 추가합니다.
divisors.append(diff)

# 8. 찾은 약수들을 오름차순으로 정렬합니다.
divisors.sort()

# 9. 약수들을 공백으로 구분하여 출력합니다.
print(" ".join(map(str, divisors)))
