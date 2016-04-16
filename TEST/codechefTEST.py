import sys

for line in sys.stdin:
    if int(line) == 42:
        sys.exit()
    else:
        print(line)

