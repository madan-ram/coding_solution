import sys, os

sys.stdin = open('cowsignal.in', 'r')
sys.stdout = open('cowsignal.out', 'w')

r1 = map(int, raw_input().split(' '))
r2 = []
for y in xrange(r1[0]):
	r2.append(raw_input())

res = []
t = r1[2]
for y in xrange(r1[0]):
	temp = ''
	for x in xrange(r1[1]):
		for _ in xrange(t):
			temp += r2[y][x]

	for _ in xrange(t):
		res += [temp]

print '\n'.join(res)