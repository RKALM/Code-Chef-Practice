for i in range(int(input())):
    n= int(input())
    m = list(map(int,input().split()))
    c=0
    a=[]
    for i in range(n):
        a.append(1)
    for j in range(n-2,-1,-1):
        if(m[j]*m[j+1]<0):
            a[j] = a[j+1]+ 1
        else:
            a[j]=1
    for i in range(n):
        print(a[i],end=" ")
    print("\r")