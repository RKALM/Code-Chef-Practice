n=int(input())
a=[]
for i in range(n):
	a.append(int(input()))
for i in a:
	fact=1
	while i>0:
		fact=fact*i
		i=i-1
	print(fact)