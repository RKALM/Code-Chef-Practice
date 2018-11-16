import sys


def is_rainbow(n, A):
  if A[0] != 1:
    return 'no'
  mid = n // 2
  j = n - 1
  i = 0
  while i < j:
    if A[i] != A[j] or A[i + 1] - A[i] > 1 or A[i + 1] - A[i] < 0 or A[i] < 0 or A[i] > 7:
      break
    j -= 1
    i += 1
  if i < j or A[i] != 7:
    return 'no'
  return 'yes'

def main():
  line = sys.stdin.read()
  data = list(map(int, line.split()))
  num_cases = data[0]
  data = data[1:]
  for _ in range(num_cases):
    n = data[0]
    A = data[1: n + 1]
    print(is_rainbow(n, A))
    data = data[n + 1:]

if __name__ == "__main__":
  main()