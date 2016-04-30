input_var = input()
arr = input_var.split(" ")
amount_to_withdraw = int(arr[0])
balance=  float(arr[1])
 
if((amount_to_withdraw+0.50)<balance and amount_to_withdraw%5==0):
    balance -= (amount_to_withdraw + 0.50)
 
 
 
print("%.2f"%balance)
