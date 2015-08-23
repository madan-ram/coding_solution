import sys
import time

def rowBinSearch(A,row,low,high,key):
	while(low<=high):
		mid=(low+high)/2
		if(A[row][mid]==key):
			return (True,row,mid)
		elif(A[row][mid]>key):
			high=mid-1
		else:
			low=mid+1
	return False,0,0

def colBinSearch(A,col,low,high,key):
	while(low<=high):
		mid=(low+high)/2
		if(A[mid][col]==key):
			return (True,mid,col)
		elif(A[mid][col]>key):
			high=mid-1
		else:
			low=mid+1
	return False,0,0

temp=map(int,raw_input().split())
N=temp[0]
M=temp[1]

for _ in xrange(N):
	A.append(map(int,raw_input().split()))
t=raw_input()
t=input()
start=time.time()
for key in map(int,raw_input().split()):
	found=False
	row=0
	col=M-1
	while(col>=0 and row<=N-1):
		if A[row][col]==key:
			found=True
			print row,col
			break
		elif A[row][col]>key:
			found,rowPos,colPos=rowBinSearch(A,row,0,col-1,key)
			if found:
				print rowPos,colPos
				break

		elif A[row][col]<key:
			found,rowPos,colPos=colBinSearch(A,col,row+1,N-1,key)
			if found:
				print rowPos,colPos
				break

		row=row+1
		col=col-1

	if found!=True:
		print "-1 -1"
end=time.time()
print "diagonal bineary search:"+str(end-start)