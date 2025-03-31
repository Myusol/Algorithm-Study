import sys
def recursion(s, l, r, c):
    if l >= r:
        return 1, c
    elif s[l] != s[r]:
        return 0, c
    else:
        return recursion(s, l+1, r-1, c+1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1, cnt)
cnt = 1
for _ in range(int(sys.stdin.readline().rstrip())):
    w=sys.stdin.readline().rstrip()
    out=isPalindrome(w)
    print(*out)