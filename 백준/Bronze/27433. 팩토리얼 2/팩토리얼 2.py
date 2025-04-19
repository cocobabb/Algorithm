def func(n):
    if n==0:
        return 1
    else:
        return n * func(n-1)

N = int(input())
print(func(N))