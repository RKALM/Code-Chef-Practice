def check_sequence(thread, seq, s, n):
    if n == 0:
        return
    else:
        for i in thread:
            k = i[0]
            if k > 0:
                if i[k] == seq[s]:
                    i[0] -= 1
                    break
        check_sequence(thread, seq, s + 1, n - 1)


T = int(input())

while T > 0:
    N = int(input())
    thread = []
    for t in range(N):
        thread.append(list(map(int, input().split())))
    seq = list(map(int, input().split()))
    res = "Yes"
    if N == 1:
        l = thread[0][0]
        for j in range(l):
            if seq[j] != thread[0][l - j]:
                res = "No"
                break
    else:
        check_sequence(thread, seq, 0, len(seq))
        for k in thread:
            if k[0] > 0:
                res = "No"
                break
    print(res)
    T -= 1
