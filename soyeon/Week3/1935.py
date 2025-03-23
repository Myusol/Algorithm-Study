n = int(input())
expr = input().strip()
nums = [int(input()) for _ in range(n)]
stack = []

for ch in expr:
    if ch.isalpha():
        idx = ord(ch) - ord('A')
        stack.append(nums[idx])
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)

print(f"{stack[0]:.2f}")