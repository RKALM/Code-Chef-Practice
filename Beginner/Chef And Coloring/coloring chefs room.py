import fileinput
firstlineiszero = 0
roomsorcolor = 0

f = open('output.txt','w')




for line in fileinput.input("happyinput.in"):
    if firstlineiszero == 0:
        firstlineiszero +=1
        print("there will be ", line, " cases!")
    else:
        firstlineiszero+=1
        print("the line ", firstlineiszero-1 ," is reffering to the ", line, " statement", sep="")
        if roomsorcolor == 0:
            print("there will be ", line, " rooms to renovate", sep="")
            roomsorcolor = 1
        else:
            print("color configuration will be ", line, sep="")
            roomsorcolor = 0


#print("Case #", str(unregisteredcase), ": ", number_string2, sep="")
#print("Case #", str(unregisteredcase), ": ", number_string2, " ",sep="", end='\n', file=f)




f.close()
print("That's all filks!")

