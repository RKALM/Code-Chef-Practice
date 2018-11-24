for i in range(int(input())):
	l,k=map(int,input().split(" "))
	count=0
	for s in range(l-k+1):
		count+=(s+1)
	print ("Case ",i+1,": ",count,sep='')