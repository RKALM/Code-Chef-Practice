import numpy as np
import sys
n, q = map(int, sys.stdin.readline().split())
a = np.zeros(n,dtype=bool)
for _ in range(q):
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 0:
        a[y:z+1]=~(a[y:z+1])
    else:
        print(a[y:z+1].sum())