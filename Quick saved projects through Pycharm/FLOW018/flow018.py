T = int(input())
for x in range(T):
    N = int(input())
    summation = 1
    for k in range(N):
        summation = summation * N
        N = N - 1
    print(summation)
