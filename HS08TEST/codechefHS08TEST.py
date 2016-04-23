#import sys

amount = 0

def isdivby5(num):
        if int(num)%5==0:
                return True
        else:
                return False

def withdraw(amount, account):
        if float(amount) > float(account):
                return account
        else:
                if float(account) > 0.5:
                        account = float(account) - 0.5
                        while float(amount) > 0:
                                if isdivby5(float(amount)):
                                        account = float(account) - float(amount)
                                        return account
                                        amount = 0
                                else:
                                        amount = float(amount) - 0.5
                

#for line in sys.stdin:
#        amount = float(line)
#        if amount % 5 == 0:
#            print("the amount is divided by 5")
#            print(amount)
#        else:
#            amount = amount - 0,5
#            print("not divided by 5")
        
