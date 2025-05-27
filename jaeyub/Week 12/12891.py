S, P = map(int, input().split())
data = input()
Ac, Cc, Gc, Tc = map(int, input().split())
answer = 0
start = 0
end = P - 1

dict = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
First = data[start:end]

for c in First:
    dict[c] += 1

while end <= S-1:
    dict[data[end]] += 1

    if dict['A'] >= Ac and dict['C'] >= Cc and dict['G'] >= Gc and dict['T'] >= Tc:
        answer += 1

    dict[data[start]] -= 1
    start += 1
    end += 1

print(answer)