import sys

itIsTheFirstLine = True
arrayNList = list()
setN=0
N1=0
N2=0
result = "Not any result right now"

#there is always something to check
def mainCheckFunction(checkFunctionsProperty1, checkFunctionsProperty2):
        if checkFunctionsProperty1 / 5 >= 1.0:
                return True
            
def functionZ(N1):
    reminder = 1.1
    i = 1
    ZN1 = 1
    ZN2 = 0
    while float(reminder) > 1.0:
#    while mainCheckFunction(float(N1),float(i)):
        print("Now I will divine " + str(N1) + " with " + str(5**i))
        ZN1 = float(N1) / float(5**i)
        print("the Z1 now is " + str(ZN1))
        reminder = float(N1) - float(ZN1 * (5.0**float(i))) #the problem is still here.
        #reminder = float(N1) % float(5**i) #the problem is about that I am using the reminder the wrong way.
        print("the reminder now is " + str(reminder))
        i+=1
        ZN2 = ZN2 + int(ZN1)
        print("I am thinking to print " + str(ZN2))
    print("I made my mind and I will print " + str(ZN2))
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
        





