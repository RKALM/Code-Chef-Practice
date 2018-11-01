a,b = list(map(int,input().split()))
difference = str(a - b)
if difference[0] is '9':
    print('8' + difference[1:])
else:
    print('9' + difference[1:])