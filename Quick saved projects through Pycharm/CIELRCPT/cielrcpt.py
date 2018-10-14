import math

t=int(input())
for i in range(t):
    m = int(input())
    c = 0
    while m > 2048:
        m -= 2048
        c += 1
    while m > 0:
        p = int(math.log2(m))
        m -= 2**p
        c += 1
    print(c)  