w, d = [float(i) for i in input().strip().split(' ')]
if (w % 5 == 0 and w + 0.5 <= d):
    d -= w + 0.5
print('%.2f' % d)
