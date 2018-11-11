t = input()
A = input().split()
count  = 0
for i in A:
    if int(i)%2 == 0:
        count += 1
if count > int(len(A)/2):
    print('READY FOR BATTLE')
else:
    print('NOT READY')