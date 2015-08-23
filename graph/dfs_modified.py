import sys

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
	length=0
	curlen=1
	li=(0,0)
	for _ in xrange(N):
		temp=map(int,raw_input().split())
		visit.append([0]*M)
		A.append(temp)
	visit[0][0]=1
	dfs(li,curlen)
	print length