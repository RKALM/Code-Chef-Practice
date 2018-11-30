import math


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


for i in range(int(input())):
    R = int(input())
    count = 0;
    CX, CY = map(int, input().split(" "))
    HX, HY = map(int, input().split(" "))
    SX, SY = map(int, input().split(" "))
    if dist(HX, HY, SX, SY) <= R:
        count += 1
    if dist(CX, CY, SX, SY) <= R:
        count += 1
    if dist(CX, CY, HX, HY) <= R:
        count += 1
    if count >= 2:
        print('yes')
    else:
        print('no')