import sys
input = sys.stdin.readline

N = int(input())
recommend = int(input())
student = list(map(int, input().split()))

photo = []
cnt = {}
when = {}
for i in range(recommend):
    s = student[i]
    
    if s in photo:
        cnt[s] += 1
        
    else:
        if len(photo) < N:
            photo.append(student[i])
            cnt[s] = 1
            when[s] = i
            
        else:
            remove = sorted(photo, key=lambda x: (cnt[x], when[x]))[0]
            photo.remove(remove)
            del cnt[remove]
            del when[remove]
            
            photo.append(student[i])
            cnt[s] = 1
            when[s] = i

print(*sorted(photo))