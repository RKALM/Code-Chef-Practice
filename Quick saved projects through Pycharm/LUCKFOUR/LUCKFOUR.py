T = int(input())
for x in range(T):
    N = list(input())
    count = 0
    for k in N:
        if str(k) == "4":
            count = count + 1
    print(count)