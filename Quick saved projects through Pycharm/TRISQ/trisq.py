import math

T = int(input())
for x in range(T):
    B = int(input())
    S = math.sqrt((B**2)/2)
    A = (B * S)/2
    result = int(A/4)
    print(result)
