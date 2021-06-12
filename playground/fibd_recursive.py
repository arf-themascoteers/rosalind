def f(n,m):
    total = 0
    for i in range(m):
        total = total + population(n,i,m)
    return total


def population(n,age,max_age):
    if n == 1:
        if age == 0:
            return 1
        else:
            return 0
    if age == 0:
        total = 0
        for i in range(1,max_age):
            total += population(n-1,i, max_age)
        return total
    else:
        return population(n-1,age-1, max_age)

n = 6
m = 3
print(f(n,m))