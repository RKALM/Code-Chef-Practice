n=int(input())
a=[]
if n<=1000:
    for i in range(n):
        sum=0
        num=int(input())
        while num!=0:
            sum=sum+num%10
            num=num//10
        a.append(sum)
for i in a:
    print(i)