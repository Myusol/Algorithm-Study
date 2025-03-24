# 나는야 포켓몬 마스터 이다솜 / 실버4
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
dic = {} # 숫자 : 문자
dic2 = {} # 문자 : 숫자
for i in range(1, n+1):
    a = input().strip() # 양끝 제거 쓰면 좋음..
    dic[i] = a # dic의 숫자에 a라는 값 저장
    dic2[a] = i # dic의 a에 들어온 순으로 저장
for _ in range(m):
    b = input().strip() # 추가로 readline사용사 /n 붙어서 중요
    if b.isdigit(): # 정수 인지 확인
        print(dic[int(b)]) # dic의 b번째 출력 - 즉 문자 출력
    else:
        print(dic2[b]) # dic2의 문자의 값 출력 - 즉 숫자 출력