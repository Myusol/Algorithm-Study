# 피보나치 수 5 / 브론즈2
n = int(input())
def fibo(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibo(a-1) + fibo(a-2)
print(fibo(n))