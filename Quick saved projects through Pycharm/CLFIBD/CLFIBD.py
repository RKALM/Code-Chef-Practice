cases = int(input())
for k in range(cases):
    str1 = input()
    set1 = set(str1)
    if len(set1) < 3:
        print("Dynamic")
    else:
        lst1 = []
        for k in set1:
            lst1.append(str1.count(k))
        lst1 = sorted(lst1)
        o = 0
        while o != len(set1) - 2:
            if lst1[o+2] != lst1[o] + lst1[o+1]:
                ans = "Not"
                break
            else:
                o += 1
        if o == len(set1) - 2:
            ans = "Dynamic"
            print("Dynamic")

        if ans != "Dynamic":
            lst2 = [lst1[1]] + [lst1[0]] + lst1[2:]
            o = 0
            while o != len(set1) - 2:
                if lst2[o+2] != lst2[o] + lst2[o+1]:
                    print("Not")
                    break
                else:
                    o += 1
            if o == len(set1) - 2:
                print("Dynamic")