import sys, os
import math

sys.stdin = open('moocast.in', 'r')
sys.stdout = open('moocast.out', 'w')

# 4
# 1 3 5
# 5 4 3
# 7 2 1
# 6 1 1


N = input()
# create graph with no connection represented by 25001
G = [[False]*N for _ in xrange(N)]
r1 = []
for _ in xrange(N):
	r1.append(map(int, raw_input().split(' ')))

for i in xrange(N):
	x, y, p = r1[i]
	for j in xrange(N):
		x_, y_, _ = r1[j]
		if i == j:
			continue
		if math.sqrt((x-x_)**2 + (y-y_)**2) < p:
			G[i][j] = True


top_connection_count = []
# apply dfs on each cow
for c_id in xrange(N):
	visited = [False]*N
	visited[c_id] = True
	can_send_cow = [c_id]
	for _id in can_send_cow:
		for i in xrange(N):
			if G[_id][i] == True and visited[i] != True:
				visited[i] = True
				can_send_cow.append(i)

	counter = 0
	for x in visited:
		if x:
			counter += 1
	top_connection_count.append(counter)

print max(top_connection_count)


