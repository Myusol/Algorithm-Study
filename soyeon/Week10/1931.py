n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for meeting in meetings:
    start = meeting[0]
    end = meeting[1]
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)