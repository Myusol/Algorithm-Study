import sys
from collections import Counter

N,C=map(int,sys.stdin.readline().split())
m = list(map(int, sys.stdin.readline().split()))

counter = Counter(m)

for number,count in counter.most_common():
    for _ in range(count):    
        print(number,end=" ")