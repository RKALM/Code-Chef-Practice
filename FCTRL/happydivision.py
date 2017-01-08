import sys

itIsTheFirstLine = True
arrayNList = list()
setN=0
N1=0
N2=0
result = "Not any result right now"

def n1N2BalanceChecker(N1,N2):
        if int(N1) <= int(N2):
                return True
            
def functionZ(N1,N2):
    if n1N2BalanceChecker(N1,N2):
        return float(N1) * float(N2)

def firstLineCorrection(inputForNInitiation):
    itIsTheFirstLine = False
    setN = inputForNInitiation
    

for N in sys.stdin:
    print("itIsTheFirstLine is " + str(itIsTheFirstLine))
    if itIsTheFirstLine == True:
        firstLineCorrection(N)
    else:
        if N < setN:
            result = str(functionZ(N,N+1))
            print("the setN now is " + str(setN))
            print ("the N now is " + str(N))
 
        


print(result)



