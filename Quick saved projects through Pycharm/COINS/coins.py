arr={}
arr[0]=0
arr[1]=1

def func(n):
    if n in arr:
        return arr[n]
    else:
        arr[n]=max(n,func(n//2)+func(n//3)+func(n//4))
        return arr[n]
if __name__=="__main__":
    count=10
    while(count):
        n=int(input())
        print(func(n))
        count=count-1