T = int(input())
N = []
for x in range(T):
    n = input()
    N = list(map(int, n))
    R = list(map(int, n))
    R.reverse()
    if N==R :
        print("wins")
    else:
        print("losses")