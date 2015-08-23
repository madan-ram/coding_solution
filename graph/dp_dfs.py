def adjList(i,j,N,M):
	l=[]
	if((i+1)<N and A[i+1][j]>A[i][j]):
		l.append((i+1,j))
	if((j+1)<M and A[i][j+1]>A[i][j]):
		l.append((i,j+1))
	return l


def dfs(li,curlen):
	global length,A,visit,N,M
	if length<curlen:
		length=curlen
	l=adjList(li[0],li[1],N,M)
	for i in xrange(len(l)):
		if(visit[l[i][0]][l[i][1]]!=1):
			visit[l[i][0]][l[i][1]]=1
			dfs(l[i],curlen+1)


for _ in xrange(input()):
	temp=map(int,raw_input().split())
	N,M=temp
	A=[]
	visit=[]
	for _ in xrange(N):
		temp=map(int,raw_input().split())
		visit.append([0]*M)
		A.append(temp)
	visit[0][0]=1
	for i in xrange(1,N):
		if(A[i-1][0]<A[i][0]):
			visit[i][0]=visit[i-1][0]+1
	for j in xrange(1,M):
		if(A[0][j-1]<A[0][j]):
			visit[0][j]=visit[0][j-1]+1
	for i in xrange(1,N):
		for j in xrange(1,M):
			if A[i][j]>A[i-1][j] and visit[i][j]<visit[i-1][j]+1:
				visit[i][j]=visit[i-1][j]+1

			if A[i][j]>A[i][j-1] and visit[i][j]<visit[i][j-1]+1:
				visit[i][j]=visit[i][j-1]+1
	r=0
	for i in xrange(0,N):
		for j in xrange(0,M):
			if(visit[i][j]==i+j+1):
				r=max(visit[i][j],r)
	if r==0:
		r=r+1
	print r
	#visit[0][0]=1
	#dfs(li,curlen)
	#print length