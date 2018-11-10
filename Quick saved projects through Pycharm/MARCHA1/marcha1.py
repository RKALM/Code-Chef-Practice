T = int(input())
for x in range(T):
    n, m = [int(k) for k in input().split(" ")]
    print(n)
    print(m)
    summary = 0
    notes = []
    for l in range(n):
        notes.insert(int(l), int(input()))
    for j in notes:
        print(j)
