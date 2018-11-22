t=int(input())
for _ in range(t):
    cnt=0
    n=int(input())
    s1=input()
    s2=input()
    m=list(map(int,input().split()))
    for i in range(len(s1)):
        if(s1[i]==s2[i]):
            cnt+=1
    ma=m[0]
    for j in range(cnt+1):
        if(m[j]>=ma):
            ma=m[j]
    if(cnt==n):
      print(m[n])
    else:
        print(ma)