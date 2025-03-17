# # 비효율 - 모든 상황 고려 코드
for _ in range(int(input())):
    paren=input()
    stack=[]
    if paren[0]==')':
        print('NO')
        continue
    for i in range(len(paren)):
        if paren[i]=='(':
            stack.append(paren[i])
            if i==len(paren)-1 and stack:
                print('NO')
        else:
            if not stack:
                print('NO')
                break
            else:
                stack.pop()
                if i==len(paren)-1 and not stack:
                    print('YES')
                elif i==len(paren)-1 and stack:
                    print('NO')
                    
# 효율 - 유효성 변수 활용
for _ in range(int(input())):
    paren=input()
    stack=[]
    if paren[0]==')':
        print('NO')
        continue
    valid=True
    for i in range(len(paren)):
        if paren[i]=='(':
            stack.append(paren[i])
        else:
            if not stack:
                valid=False
                break
            stack.pop()
    if valid and not stack:
        print('YES')
    else:
        print('NO')