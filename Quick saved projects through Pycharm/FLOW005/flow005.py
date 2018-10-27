T = int(input())
for x in range(T):
    count = 0
    N = int(input())
    while N != 0:
        if N >= 100:
            a = int(N / 100)
            count = int(count + a)
            N = int(N - (a*100))
        elif N >= 50:
            a = int(N / 50)
            count = int(count + a)
            N = int(N - (a * 50))
        elif N >= 10:
            a = int(N / 10)
            count = int(count + a)
            N = int(N - (a * 10))
        elif N >= 5:
            a = int(N / 5)
            count = int(count + a)
            N = int(N - (a * 5))
        elif N >= 2:
            a = int(N / 2)
            count = int(count + a)
            N = int(N - (a * 2))
        else:
            a = N
            count = int(count + a)
            N = int(N - a)
    print(int(count))
