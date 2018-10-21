T = int(input())
for x in range(T):
    N = input().split()
    A = int(N[0])
    B = int(N[1])
    C = int(N[2])
    ABC = [A, B, C]
    ABC.sort()
    second = int(ABC[1])
    print(int(second))
