t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if c%2!=0:
        a*=2
    print((max(a,b))//(min(a,b)))