import sys
queue=[]
for _ in range(int(input())):
    command=sys.stdin.readline().split()
    if command[0]=='push':
        queue.append(command[1])
    elif command[0]=='pop':
        print(queue.pop(0) if queue else -1)
    elif command[0]=='size':
        print(len(queue))
    elif command[0]=='empty':
        print(1 if not queue else 0)
    elif command[0]=='front':
        print(queue[0] if queue else -1)
    elif command[0]=='back':
        print(queue[-1] if queue else -1)