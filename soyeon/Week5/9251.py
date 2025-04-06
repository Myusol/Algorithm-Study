A = input()
B = input()
arr = [0] * len(B)

for i in range(len(A)) :
    tmp = 0
    for j in range(len(B)) :
        if tmp < arr[j] :
            tmp = arr[j]
        elif A[i] == B[j] :
            arr[j] = tmp + 1
print(max(arr))