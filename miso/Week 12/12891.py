import sys
from collections import defaultdict
input = sys.stdin.readline
S, P = map(int, input().split())
DNA = list(input())
A, C, G, T = map(int, input().split())

password = defaultdict(int)
cnt = 0
for i in range(P):
    password[DNA[i]] += 1
if password['A'] >= A and password['C'] >= C and password['G'] >= G and password['T'] >= T:
    cnt += 1

for i in range(S - P):
    password[DNA[i]] -= 1
    password[DNA[i + P]] += 1
    if password['A'] >= A and password['C'] >= C and password['G'] >= G and password['T'] >= T:
        cnt += 1
print(cnt)