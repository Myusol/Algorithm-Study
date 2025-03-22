n = int(input().strip())
commands = [input().strip().split() for _ in range(n)]

def stack_commands(commands):
    stack = []
    result = []

    for command in commands:
        if command[0] == 'push':
            stack.append(command[1])
        elif command[0] == 'pop':
            if stack:
                result.append(stack.pop())
            else:
                result.append(-1)
        elif command[0] == 'size':
            result.append(len(stack))
        elif command[0] == 'empty':
            result.append(0 if stack else 1)
        elif command[0] == 'top':
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)

    return result

results = stack_commands(commands)
print("\n".join(map(str, results)))