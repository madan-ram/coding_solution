import sys, os

sys.stdin = open('haybales.in', 'r')
sys.stdout = open('haybales.out', 'w')

# 4 6
# 3 2 7 5
# 2 3
# 2 4
# 2 5
# 2 7
# 4 6
# 8 10

def binary_search(data_list, key):
	low = 0
	heigh = len(data_list)-1
	while(low<=heigh):
		mid = (low+heigh)/2
		if data_list[mid] == key:
			return True, mid
		else:
			if data_list[mid] > key:
				heigh = mid-1
			elif data_list[mid] < key:
				low = mid+1

	return False, mid

N, Q = map(int, raw_input().split(' '))
haybales_found_index = map(int, raw_input().split(' '))
# sort by index
haybales_found_index.sort()

queries = []
for q in xrange(Q):
	queries.append(map(int, raw_input().split(' ')))

# perform binary search to find and return index for every queries
for q in xrange(Q):
	l, h = queries[q]
	status1, p1 = binary_search(haybales_found_index, l)
	status2, p2 = binary_search(haybales_found_index, h)

	if status1 is False:
		while(haybales_found_index[p1] < l):
			p1 = p1+1
			if p1 == len(haybales_found_index):
				p1 = p1 - 1
				break

	if status2 is False:
		while(haybales_found_index[p2] > h):
			p2 = p2-1
			if p2 == -1:
				p2 = p2 + 1
				break

	# if haybales_found_index[p1]
	if (haybales_found_index[-1] < l and haybales_found_index[-1] < h) or (haybales_found_index[0] > l and haybales_found_index[0] > h):
		print 0
	else:
		print p2 - p1 + 1

	# print status1, p1, haybales_found_index[p1]
	# print status2, p2, haybales_found_index[p2]
	# print '---------------------------------------------'