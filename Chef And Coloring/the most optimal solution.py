T = int(input())
for x in range(T):
	r = int(input())
	S = input()
	R = S.count('R')
	G = S.count('G')
	B = S.count('B')
	n = len(S) - max(R, G, B)
	print(n)
