import sys

itIsTheFirstLine = True     #This variable is about the input line. If the line is the first the variable itIsTheFirstLine is True.
T=0     #The number of lines with usefull Data.
result = "Not any result right now" #this is used for the result wich is printed in the end of the code with the default value.
mainlist = []
countForT = 0

#the mainCheckFunction() function is doing the necessary checking before the mainCalculativFunction().
#there is always something to check
def mainCheckFunction(checkFunctionsProperty):
        if checkFunctionsProperty == True:
                return True

#The function mainCalculativFunction() solves the logical problem of the exercise.         
def mainCalculativFunction(inputProperty):
    #if mainCheckFunction(True):
    global mainlist
    #print("Now i will add the " + str(inputProperty) + "to the mainlist")
    mainlist.append(int(inputProperty))
    #print("the mainlist now is" + str(mainlist))


#The function firstLineCorrection() changes the itIsTheFirstLine to False and stores the N to the variable T
def firstLineCorrection(inputForNInitiation):
    global itIsTheFirstLine
    global T
    itIsTheFirstLine = False
    T = inputForNInitiation
    

for N in sys.stdin:
    #print("itIsTheFirstLine now is " + str(itIsTheFirstLine))
    if itIsTheFirstLine == True:
        firstLineCorrection(N)
    else:
        mainCalculativFunction(N)
        countForT += 1
        #print("the T which represent the number of lines with input data, now is " + str(T))        
        if countForT >= int(T):
            #print ("the N now which is the value of the last input now is " + str(N))
            mainlist.sort()
            result = str(mainlist)
            #print("the result of the main calculative fuction know as mainCalculativFunction() now is " + result)
            for i in range(int(T)):
                print(str(mainlist[i]))
        





