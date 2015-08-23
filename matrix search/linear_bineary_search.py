import sys
temp=map(int,raw_input().split())
N=temp[0]
M=temp[1]
A=[]
for _ in xrange(N):
	A.append(map(int,raw_input().split()))

for _ in xrange(input()):
	found=False
	X=input()
	row=0
	col=M-1
	while(col>=0 and row<=N-1):
		if X<A[row][col]:
			col=col-1
		elif X>A[row][col]:
			row=row+1
		else:
			print row,col
			found=True
			break
	if found==False:
		print "-1 -1"