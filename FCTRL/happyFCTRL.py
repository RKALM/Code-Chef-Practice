import sys

itIsTheFirstLine = True
arrayNList = list()
setN=0
N1=0
N2=0
result = "Not any result right now"
            
def functionZ(N1):
    reminder = 1.1
    i = 1
    ZN1 = 1
    ZN2 = 0
    while float(reminder) > 1.0:
        ZN1 = float(N1) / float(5^i)
        reminder = float(N1) - float(ZN1)
        i+=1
        ZN2 = ZN2 + int(ZN1)
    return ZN2
        
    

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
            result = functionZ(int(N))
            print("the setN now is " + str(setN))
            print ("the N now is " + str(N))
            print("The result is " + str(result))
        else:
            result = functionZ(int(N))
            print("The result is " + str(result))
            print("That's all folks!")
            #here i need to kill the function
        





