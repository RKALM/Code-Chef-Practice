n=int(input())
for i in range(n):
    g=int(input())
    for j in range(g):
        i,n,q=map(int,input().split())
        if n%2==0:
            print(n//2)
        else:
            if i==q:
                print(n//2)
            else:
                print((n//2)+1)