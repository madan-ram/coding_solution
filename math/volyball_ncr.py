import math
M=10**9+7
fact=[1,1]

def init():
    N=10**7
    global fact,xInvFact
    for x in xrange(2,N+1):
        fact.append(fact[len(fact)-1]*x%M)

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
    denominator=findMMI_fermat((fact[r]*fact[n-r])%M,M)
    return (neuminator*denominator)%M

init()

S1=input()
S2=input()
if(S1>=24 and S2>=24):
    if math.fabs(S1-S2)<=2:
        l=S1+S2-1
        if(S1>S2):
            S=(S1-1)
            print nCr(l,S,M)
        else:
            S=(S2-1)
            print nCr(l,S,M)
    else:
        print 0
elif((S1==25 and S2<=23) or (S2==25 and S1<=23)):
    l=S1+S2-1
    if(S1==25 and S2<=23):
        S=S1-1
        print nCr(l,S,M)
    else:
        S=S2-1
        print nCr(l,S,M)
else:
    print 0