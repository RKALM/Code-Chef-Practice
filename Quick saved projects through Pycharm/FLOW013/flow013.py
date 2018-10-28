T = int(input())
N = []
for x in range(T):
    N = input().split(" ")
    A = int(N[0])
    B = int(N[1])
    C = int(N[2])
    ABC = A + B + C
    if ABC == 180:
        print("YES")
    else:
        print("NO")
