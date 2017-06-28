import sys, os

sys.stdin = open('blocks.in', 'r')
sys.stdout = open('blocks.out', 'w')

# 3
# fox box
# dog cat
# car bus

res = [0]*26
N = input()
r = []
for _ in xrange(N):
	r.append(raw_input().split(' '))

for i in xrange(N):
	w1 = r[i][0]
	w2 = r[i][1]
	a1 = [0]*26
	a2 = [0]*26
	for w in w1:
		a1[ord(w) - ord('a')] += 1

	for w in w2:
		a2[ord(w) - ord('a')] += 1

	for i in xrange(len(res)):
		res[i] += max(a1[i], a2[i])

for i in xrange(len(res)):
	print res[i]