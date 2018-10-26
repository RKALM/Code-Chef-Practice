t = int(input())
data =[]
for i in range(t):
    n = int(input())
    data = input().split()
    for j in range(len(data)):
        d = int(data[j])
        data.remove(data[j])
        data.insert(j,d)
    data.sort()
    print(data[1]+data[0])
