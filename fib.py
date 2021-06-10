n = 29
k = 4

def f(n,k):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return f(n-1,k) + f(n-2,k)*k

print(f(n,k))