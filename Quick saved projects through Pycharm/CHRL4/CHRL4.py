import numpy as np


def minprod(N, K, A):
    cost = [np.inf if i > 0 else A[i] for i in range(N)]
    i, start = 0, 0

    while True:
        last = min(i + K, N - 1)
        for k in range(last, start, -1):
            x = cost[i] * A[k]
            if cost[k] > x:
                cost[k] = x

            if k == N - 1:
                return cost[-1]

        i, start = last - np.argmin(cost[last:i:-1]), last


N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

print(minprod(N, K, A) % 1000000007)