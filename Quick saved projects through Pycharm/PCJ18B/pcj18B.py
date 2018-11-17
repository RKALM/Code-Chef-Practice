T=int(input())
for _ in range(T):
    N=int(input())
    T=0
    for i in range(N):
        if (N-2*i)>0:
            T+=(N-2*i)**2
        else:
            T+=0
    print(T)