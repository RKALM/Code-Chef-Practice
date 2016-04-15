import fileinput
firstlineiszero = 0
roomsorcolor = 0

f = open('output.txt','w')

def most_common(lst):
    return max(set(lst), key=lst.count)


def configuratesomeshit(somelist):
    keyshit = most_common(somelist)
    paintjob = 0
    print("we will paint with", keyshit)
    for shit in somelist:
        if shit == "R" or shit == "G" or shit=="B":
            if shit == keyshit:
                print("the color in the room is alrwady ", shit, " No action is necessary", sep="")
            else:
                print("the room is ", shit, " .We have to paint it ", keyshit, sep="")
                paintjob+=1
        else:
            print("i found a piece of junk, it is my lucky one")
    print("it took ", paintjob, " to paint all the rooms")
    print(paintjob,sep="", end='\n', file=f)




for line in fileinput.input("happyinput.in"):
    if firstlineiszero == 0:
        firstlineiszero +=1
        print("there will be ", line, " cases!", sep="", end='\n')
    else:
        firstlineiszero+=1
        print("the line ", firstlineiszero-1 ," is reffering to the ", line, " statement", sep="")
        if roomsorcolor == 0:
            print("there will be ", line, " rooms to renovate", sep="")
            roomsorcolor = 1
        else:
            roomsorcolor = 0
            roomconfiguration = str(line)
            list(roomconfiguration)
            print("color configuration will be ", roomconfiguration, sep="")
            configuratesomeshit(roomconfiguration)


#print("Case #", str(unregisteredcase), ": ", number_string2, sep="")
#print("Case #", str(unregisteredcase), ": ", number_string2, " ",sep="", end='\n', file=f)




f.close()
print("That's all folks!")

