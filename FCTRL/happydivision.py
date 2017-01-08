import sys

firstlineiszero=0
templist = list()
counter = 0
firstint = 0
k1=0
t1=0
count=0

def tiisdividedbyk(t,k):
        if int(t)%int(k) == int(0):
                return True


for line in sys.stdin:
    if firstlineiszero == 0:
        firstlineiszero +=1
        templist = line.split()
        firstint = templist[0]
        k1=templist[1]
    else:
        t1=line
        if counter+1 < int(firstint):
                counter += 1
                if tiisdividedbyk(t1,k1) == True:
                        count += 1
        else:
                if tiisdividedbyk(t1,k1) == True:
                        count += 1
                        print(count)
                else:
                        print(count)

print(count)



