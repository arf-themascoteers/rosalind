import math

n = 100
r = 9
result = 1
for x in range(n-r+1, n+1):
    result = result * x
print(result%1000000)