import sys

itIsTheFirstLine = True
arrayNList = list()
T=0
result = "Not any result right now"

def mainCheckFunction(checkFunctionsProperty):
        if checkFunctionsProperty == True:
                return True
            
def mainCalculativFunction(inputProperty):
    if mainCheckFunction(True):
        return inputProperty

def firstLineCorrection(inputForNInitiation):
    global itIsTheFirstLine
    global T
    itIsTheFirstLine = False
    T = inputForNInitiation
    

for N in sys.stdin:
    print("itIsTheFirstLine now is " + str(itIsTheFirstLine))
    if itIsTheFirstLine == True:
        firstLineCorrection(N)
    else:
        result = mainCalculativFunction(N)
        print("the T which represent the number of lines with input data, now is " + str(T))        
        if N < T:
            print ("the N now which is the value of the last input now is " + str(N))
        else:
            print("the result of the main calculative fuction know as mainCalculativFunction() now is " + result)
 
        





