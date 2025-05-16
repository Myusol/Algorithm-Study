# 후보 추천하기 / 실버1
import sys
input = sys.stdin.readline
N = int(input())
V = int(input())
students = list(map(int, input().split()))
picture = []
score = []
for i in range(V):
    if students[i] in picture: # 사진 틀에 있으면
        for j in range(len(picture)):
            if students[i] == picture[j]:
                score[j] += 1 # 점수증가
    else: # 사진틀에 없는데
        if len(picture) >= N: # 사진틀 꽉차면
            for j in range(N):
                if score[j] == min(score): # 가장 작은 점수 찾고 삭제
                    del picture[j]
                    del score[j]
                    break # 오래 된거는 앞에 있으니까 멈춤
        picture.append(students[i]) # 새로운거 뒤에 더하기
        score.append(1)
picture.sort() # 오름차순 정렬
print(*picture)