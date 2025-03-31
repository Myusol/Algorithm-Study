# 알고리즘 수업 - 병합 정렬 1 / 실버3
import sys
input = sys.stdin.readline
n, k = map(int, input().split())  # 크기, 저장횟수
li = list(map(int, input().split()))
count = 0
def merge(li, p, q, r): # p = 시작 인덱스 q = 중간 r = 마지막 인덱스(왼쪽p ~ q, 오른쪽은 q + 1 ~ r)
    global count, k
    tmp = [] # 배열 두개를 합해서 저장할 임시 리스트
    i, j = p, q + 1 # i는 왼쪽 배열(li[p ~ q])의 인덱스, j는 오른쪽 배열(li[q+1 ~ r ])의 인덱스
    while i <= q and j <= r: # 왼쪽 배열 오른쪽 배열 둘다 각각 비교
        if li[i] <= li[j]: # 결과에 따라서 tmp 임시저장
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= q: # 한쪽이 끝나면 남은 배열들 tmp 추가
        tmp.append(li[i])
        i += 1
    while j <= r:
        tmp.append(li[j])
        j += 1
    i = p
    for value in tmp: # tmp에 전부 하나씩 li랑 확인
        li[i] = value
        count += 1
        if count == k: #count랑 같아지면 출력 및 종료
            print(li[i])
            sys.exit(0)
        i += 1
def merge_sort(li, p, r):
    if p < r:
        q = (p + r) // 2 # 중간 인덱스 구하기
        merge_sort(li, p, q) # 왼쪽 부분 배열 정렬
        merge_sort(li, q + 1, r) # 오른쪽 부분 배열 정렬
        merge(li, p, q, r) # 정렬된 두 배열을 병합
merge_sort(li, 0, n - 1)
print(-1) # exit() 를 써서 프로그램 자체를 종료시키니까 어차피 작을때 제외하면 출력 안됨