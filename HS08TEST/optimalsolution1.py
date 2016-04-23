x = input()
lst = x.split()
amou = int(lst[0])
bal = float(lst[1])
cond = amou + 0.5 < bal
cond = cond and amou % 5 == 0
 
if cond:
	bal -= amou + 0.5
	
print(bal) 
