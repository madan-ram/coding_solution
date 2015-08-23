def merge(A,B):
	i=0
	j=0
	C=[]
	inveration=0
	inverationList=[]
	while(i<len(A) and j<len(B)):
		if(A[i]<=B[j]):
			C.append(A[i])
			i+=1
		else:
			C.append(B[j])
			inveration+=len(A[i:])
			for x in A[i:]:
				inverationList.append((x,B[j]))
			j+=1
	if i==len(A):
		for x in B[j:]:
			C.append(x)
	else:
		for x in A[i:]:
			C.append(x)
	return C,inveration,inverationList

A=[1]
B=[2]
print merge(A,B)
A=[1]
B=[3]
print merge(A,B)
A=[1,2]
B=[4]
print merge(A,B)
A=[1,3]
B=[5]
print merge(A,B)
A=[1,2,4]
B=[1,3,5]
print merge(A,B)
print "---------------------"
A=[1]
B=[2]
print merge(A,B)
A=[1,2]
B=[4]
print merge(A,B)
A=[3]
B=[5]
print merge(A,B)
A=[1,2,4]
B=[3,5]
print merge(A,B)
print "--------------------"
A=[1,3,5]
B=[2,4,6]
print merge(A,B)