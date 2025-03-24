# 단어 공부 / 브론즈1
word = input().strip().upper()
freq = [0] * 26 # 알파벳 수 만큼 리스트 생성
for ch in word:
    freq[ord(ch) - ord('A')] += 1 # 아스크 코드를 이용해서 빈도값 계산
max_freq = max(freq) # 최대값 찾음
if freq.count(max_freq) > 1:# 최대 빈도수가 2개 이상인지 확인함
    print("?")
else:
    index = freq.index(max_freq) # 아닐시 최대 빈도수를 가진 알파벳 인덱스 찾고 알파벳 출력
    print(chr(index + ord('A')))