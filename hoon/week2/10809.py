s = input()
lis = []
for i in 'abcdefghijklmnopqrstuvwxyz':
    lis.append(str(s.find(i))) # find()인덱스를 찾음 없으면 -1반환
print(*lis)