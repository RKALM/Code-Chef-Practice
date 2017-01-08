import sys

itIsTheFirstLine = True
arrayNList = list()
setN=0
N1=0
N2=0
result = "Not any result right now"

def n1N2BalanceChecker(N1):
        if int(N1) > 0:
                return True
            
def functionZ(N1):
    if n1N2BalanceChecker(N1):
        return int(N1)

def firstLineCorrection(inputForNInitiation):
    global itIsTheFirstLine
    global setN
    itIsTheFirstLine = False
    setN = inputForNInitiation
    

for N in sys.stdin:
    print("itIsTheFirstLine is " + str(itIsTheFirstLine))
    if itIsTheFirstLine == True:
        firstLineCorrection(N)
    else:
        if N < setN:
            result = int(N) + functionZ(int(N))
            print("the setN now is " + str(setN))
            print ("the N now is " + str(N))
        else:
            print(result)
 
        





