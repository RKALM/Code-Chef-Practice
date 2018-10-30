T = int(input())
for x in range(T):
    N = input().split(" ")
    A = int(N[0])
    B = int(N[1])
    if A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("=")
