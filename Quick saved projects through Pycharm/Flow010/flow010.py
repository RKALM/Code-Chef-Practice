T = int(input())
for x in range(T):
    N = input()
    if N.lower() == "b":
        print("BattleShip")
    elif N.lower() == "c":
        print("Cruiser")
    elif N.lower() == "d":
        print("Destroyer")
    else:
        print("Frigate")
