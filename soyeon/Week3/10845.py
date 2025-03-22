import sys
from collections import deque

n = int(sys.stdin.readline().strip())
commands = [sys.stdin.readline().strip().split() for _ in range(n)]

def queue_commands(commands):
    queue = deque()
    result = []

    for command in commands:
        if command[0] == 'push':
            queue.append(command[1])
        elif command[0] == 'pop':
            if queue:
                result.append(queue.popleft())
            else:
                result.append(-1)
        elif command[0] == 'size':
            result.append(len(queue))
        elif command[0] == 'empty':
            result.append(0 if queue else 1)
        elif command[0] == 'front':
            if queue:
                result.append(queue[0])
            else:
                result.append(-1)
        elif command[0] == 'back':
            if queue:
                result.append(queue[-1])
            else:
                result.append(-1)

    return result

results = queue_commands(commands)
sys.stdout.write("\n".join(map(str, results)) + "\n")