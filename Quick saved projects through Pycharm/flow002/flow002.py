T = int(input())
AB = []
for x in range(T):
    AB = input().split(" ")
    print(int(AB[0]) % int(AB[1]))