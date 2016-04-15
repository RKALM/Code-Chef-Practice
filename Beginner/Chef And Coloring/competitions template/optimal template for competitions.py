import fileinput

f = open('output.txt','w')




for line in fileinput.input("happyinput.in"):


#print("Case #", str(unregisteredcase), ": ", number_string2, sep="")
#print("Case #", str(unregisteredcase), ": ", number_string2, " ",sep="", end='\n', file=f)




f.close()
print("That's all filks!")

