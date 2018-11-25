for i in range(int(input())):
        n=input().split()
        seq=list(map(int,input().split()))
        ls=[]
        leng=len(seq)
        for i in range(leng):
            ls.append(1)
        for i in range(1,leng):
            if seq[i]>=seq[i-1] and ls[i] <=ls[i-1]:
                ls[i]=1+ls[i-1]
        print(sum(ls))