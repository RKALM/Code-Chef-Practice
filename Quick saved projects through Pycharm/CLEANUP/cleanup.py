def solve(li,n,m):
    ml=[i for i in range(1,n+1)]
    for it in li:
        del ml[ml.index(it)]
    ml=sorted(ml)
    chef=[]
    ass=[]
    for i in range(0,len(ml)):
        if i%2==0:
            chef.append(ml[i])
        else:
            ass.append(ml[i])
    return chef,ass
t=int(input())
for i in range(0,t):
    n,m=[int(x) for x in input().split()]
    li=[int(x) for x in input().split()]
    c,a=solve(li,n,m)
    if len(c)==0:
        print("")
    for it in c:
        print(it,end=" ")
    print("")
    for it in a:
        print(it,end=" ")
    if len(a)==0:
        print("")
    print("")