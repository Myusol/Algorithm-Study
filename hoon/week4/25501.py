# 재귀의 귀재 / 브론즈2
n = int(input())
def recursion(s, l, r): # AAA, 0, 2
    global count # 호출하는곳에서 쓰고 다시 반복할때도 누적 할거니까 global 써줘야함
    count += 1 # 호출시 1씩 증가
    if l >= r: return 1 # 반복하면서 줄여질때 l이 r보다 커지면 성공
    elif s[l] != s[r]: return 0 # 반복중 틀리게 발견되면 아니라고 판단하고 종료
    else:
        return recursion(s, l+1, r-1) # 다음 호출땐 점점 줄여감
# 문자열을 받으면 recursion을 호출하는데 그때 (문자열, 0, 문자열 길이 -1)제공
def isPalindrome(s):
    return recursion(s, 0, len(s)-1) # len(s)-1 이유는 마지막 문자열 비교하기 위해
for _ in range(n):
    s = input()
    count = 0 # 밖에서 선언하면 쌓여서 나옴
    print(isPalindrome(s), count)