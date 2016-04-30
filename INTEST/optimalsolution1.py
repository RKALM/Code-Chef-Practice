inp=input()
 
n = int(inp.split()[0])
s=int(inp.split()[1])
count = 0
 
for i in range (n):
    k = int(input())
    
    if k%s==0:
        count +=1
    i +=1
 
print (count)
