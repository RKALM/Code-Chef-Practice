T = int(input())
for k in range(T):
  lines = int(input())
  l = []
  for j in range(lines):
    x = list(map(int, input().split()))
    l.append(x)

  for i in range(len(l)-1, 0, -1):
    for j in range(i):
      if l[i][j] > l[i][j+1]:
        l[i-1][j] += l[i][j]
      else:
        l[i-1][j] += l[i][j+1]
  print(l[0][0])  