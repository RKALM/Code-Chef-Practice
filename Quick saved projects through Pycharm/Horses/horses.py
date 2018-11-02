T = int(input())
for x in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    minimum = abs(int(S[1]) - int(S[0]))
    for k in range(2, N):
        differ = abs(int(S[k]) - int(S[k-1]))
        if differ < minimum:
            minimum = differ
    print(minimum)
