n = int(input())
for i in range(n):
    n, mi, ma = [int(x) for x in input().split()]
    a, c = 1, 0
    for j in range(n):
        w, b = [int(x) for x in input().split()]
        a = w * a + b
        if (a % 2 == 0):
            a = 0
        else:
            a = 1
        c = w * c + b
        if (c % 2 == 0):
            c = 0
        else:
            c = 1
    if (a == 1 and c == 1):
        print(0, ma - mi + 1, sep=" ")
        continue
    elif (a == 0 and c == 0):
        print(ma - mi + 1, 0, sep=" ")
        continue
    elif (a == 0 and c == 1):
        if (ma % 2 == 0 and mi % 2 == 0):
            print((ma - mi) // 2, ((ma - mi) // 2) + 1, sep=' ')
            continue
        elif (ma % 2 == 1 and mi % 2 == 1):
            print(((ma - mi) // 2) + 1, (ma - mi) // 2, sep=' ')
            continue
        else:
            print(((ma - mi + 1) // 2), (ma - mi + 1) // 2, sep=' ')
            continue
    elif (a == 1 and c == 0):
        if (ma % 2 == 0 and mi % 2 == 0):
            print(((ma - mi) // 2) + 1, (ma - mi) // 2, sep=' ')
            continue
        elif (ma % 2 == 1 and mi % 2 == 1):
            print((ma - mi) // 2, ((ma - mi) // 2) + 1, sep=' ')
            continue
        else:
            print(((ma - mi + 1) // 2), (ma - mi + 1) // 2, sep=' ')
            continue
