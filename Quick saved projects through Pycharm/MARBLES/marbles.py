def marbles(n,k):
    a=1
    if n == k:
      print(1)
      return
    if n<k:
      print(0)
      return
    if n>k :
        for j in range(min(k-1,n-k)):
           n=n-1
           a=(a*n)//(j+1)

    print(a)
for i in range(int(input())):
    n, k= map(int,input().split(" "))
    marbles(n,k)