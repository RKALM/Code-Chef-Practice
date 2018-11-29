n,k=map(int,input().split())
a = dict()
while(k):
    c=input()
    if(c=="CLOSEALL"):
        a=dict()
    else:
        v = c.split()[1]
        if v in a:
            a.pop(v)
        else:
            a[v]=1
    print(len(a))
    k = k-1