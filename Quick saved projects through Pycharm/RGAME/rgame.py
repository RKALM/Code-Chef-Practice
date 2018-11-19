mod = 10**9 + 7
for k in range(int(input())):
    ans = 0
    num = int(input())
    lst = input().split(" ")
    lst1 = [lst[0]]
    lst2 = list(map(int, lst))
    dynamic_sum = 0
    lst3 = []
    for i in range(1,len(lst2)):
        b = lst2[i] * (2 ** (num - i))
        lst3.append(b)
        dynamic_sum += b
    ans1 = 2 * lst2[0] * dynamic_sum
    for k in range(0,len(lst3)):
        dynamic_sum -= lst3[k]
        ans1 += int((lst2[k+1] * dynamic_sum) * (2 ** (k+1)))
        ans1 = ans1 % mod
    print(ans1)