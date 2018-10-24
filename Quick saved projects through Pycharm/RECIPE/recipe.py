t = int(input())

def factor(data, l):
    n = 1
    for j in range(1, data + 1):
        counter = 0
        for k in l:
            if k % j != 0:
                break
            else:
                counter += 1
        if counter == len(l):
            n = j

    return n

for i in range(t):
    l = list(map(int, input().split()))
    l.remove(l[0])
    data = max(l)
    d = factor(data, l)
    for j in range(len(l)):
        if j == (len(l) - 1):
            print(int(l[-1] / d), end="\n")
        else:
            print(int(l[j] / d), end=" ")