import sys

happylist = list()

def isdivby5(num):
        if int(num)%5==0:
                return True
        else:
                return False

def withdraw(amount, account):
        if float(amount) >= float(account):
                return float(account)
        else:
                if float(account) > 0.5:
                        while float(amount) > 0:
                                if isdivby5(float(amount)):
                                        account = float(account) - float(amount)
                                        account = float(account) - 0.5
                                        return account
                                        amount = 0
                                else:
                                        return account
                

for line in sys.stdin:
        happylist = line.split()
        print("%.2f" %  withdraw(happylist[0],happylist[1]))
        
