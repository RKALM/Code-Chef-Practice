T = int(input())
for x in range(T):
    N = input().split()
    maxim = int(N[0]) + int(N[1])
    N.sort()
    minim = int(N[1])
    print(int(maxim), int(minim))
