
M=10**9+7
fact=[1,1]
xInvFact=[]
def init():
	global fact,xInvFact
	for x in xrange(2,100001):
		fact.append(fact[len(fact)-1]*x%M)

	for i in xrange(0,100001):
		xInvFact.append(findMMI_fermat(fact[i],M)%M)

def fast_pow(d,n,M):
	if n==0:
		return 1
	if n==1:
		return d
	half=fast_pow(d,n/2,M)
	if n%2==0:
		return (half*half)%M
	else:
		return ((half*half)%M*d)%M

def findMMI_fermat(d,M):
	return fast_pow(d,M-2,M)

def nCr(n,r,M):
    neuminator=fact[n]
    denominator=(xInvFact[r]*xInvFact[n-r])%M
    return (neuminator*denominator)%M

init()
for _ in xrange(input()):
	temp=map(int,raw_input().split())
	N,K=temp
	temp=map(int,raw_input().split())
	s=0
	temp.sort()
	c=N-1
	for x in temp[0:N-K+1]:
		s+=x*nCr(c,K-1,M)%M
		c=c-1
	print (s%M)