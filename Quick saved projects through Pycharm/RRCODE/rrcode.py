for ti in xrange(input()):
    n, k, ans = map(int, raw_input().strip().split())
    l = map(int, raw_input().strip().split())
    d = raw_input().strip()
    if not k:
        print
        ans
        continue
    if d == "XOR":
        if k % 2 == 0:
            print
            ans
            continue
        for i in l:
            ans = ans ^ i

    elif d == "OR":
        for i in l:
            ans = ans | i
    else:
        for i in l:
            ans = ans & i
    print
    ans