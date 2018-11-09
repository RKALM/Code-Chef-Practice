import math
n = int(input())
for i in range(n):
    a,b = [int(k) for k in input().split()]
    print(math.gcd(a,b))