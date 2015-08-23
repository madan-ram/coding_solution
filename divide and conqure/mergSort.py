def merge(A,low,mid,high):
	i=0
	j=0
	D=[]
	B=A[low:mid+1]
	C=A[mid+1:high+1]
	inveration=0
	inverationList=[]
	while(i<len(B) and j<len(C)):
		if(B[i]<=C[j]):
			D.append(B[i])
			i+=1
		else:
			D.append(C[j])
			inveration+=len(B[i:])
			for x in B[i:]:
				inverationList.append((x,C[j]))
			j+=1
	if i==len(B):
		for x in C[j:]:
			D.append(x)
	else:
		for x in B[i:]:
			D.append(x)
	for i in xrange(len(C)):
		A[i]=D[i]
	return C,inveration,inverationList

def mergeSort(A,low,high):
	if high>low:
		mid=(low+high)/2
		mergeSort(A,low,mid)
		mergeSort(A,mid+1,high)
		merge(A,low,high,mid)
	else:
		return 0

A=[1,5,2,6,3]
B=[0]*100
for i in xrange(len(A)):
	B[i]=A[i]
mergeSort(B,0,len(A)-1)
print B
A=[1,3,5,2,4,6]
B=[0]*100
for i in xrange(len(A)):
	B[i]=A[i]
mergeSort(B,0,len(A)-1)
print B