# 그대로 출력하기 / 브론즈3

# 엔터를 치고 끝내는것
# while True:
#     s = input()
#     if len(s) == 0:
#         break
#     else:
#         print(s)

# 입력받는 모든 줄을 반복
import sys

for line in sys.stdin:
    print(line, end="")
