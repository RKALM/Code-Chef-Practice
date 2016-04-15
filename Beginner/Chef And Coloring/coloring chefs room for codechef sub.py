import sys
firstlineiszero = 0
roomsorcolor = 0



def most_common(lst):
    return max(set(lst), key=lst.count)


def configuratesomeshit(somelist):
    keyshit = most_common(somelist)
    nothing = 0
    nothing2 = 0
    paintjob = 0
    for shit in somelist:
        if shit == "R" or shit == "G" or shit=="B":
            if shit == keyshit:
                nothing +=1
            else:
                paintjob+=1
        else:
            nothing2 +=1
    print(paintjob)




for line in sys.stdin:
    if firstlineiszero == 0:
        firstlineiszero +=1
    else:
        firstlineiszero+=1
        if roomsorcolor == 0:
            roomsorcolor = 1
        else:
            roomsorcolor = 0
            roomconfiguration = str(line)
            list(roomconfiguration)
            configuratesomeshit(roomconfiguration)
