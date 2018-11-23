from functools import reduce

T = int(input())
for _ in range(T):
    N, Q = [int(x) for x in input().split()]
    D = [int(x) for x in input().split()]
    X = [int(x) for x in input().split()]

    m = reduce(lambda x, y: x * y, D)
    X = [x // m for x in X]
    print(*X)