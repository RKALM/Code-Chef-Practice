import sys

amount = 0

for line in sys.stdin:
        amount = float(line)
        if amount % 5 == 0:
            print("the amount is divided by 5")
            print(amount)
        else:
            amount = amount - 0,5
            print("not divided by 5")
        
