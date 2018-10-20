while True:
    n = int(input())
    if n == 0:
        break

    inverse = [0]*n
    original = list(map(int, input().split()))
    for position, number in enumerate(original):
        inverse[number-1] = position+1

    if inverse == original:
        print('ambiguous')
    else:
        print('not ambiguous')