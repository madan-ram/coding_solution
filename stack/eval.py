from collections import deque

def getTokenList(s):
	t=""
	l=[]
	for i in xrange(len(s)):
		x=s[i]
		if x.isdigit() and i!=len(s)-1:
			t=t+x
		elif  x.isdigit() and i==len(s)-1:
			t=t+x
			l.append(t)
			t=""
		else:
			l.append(t)
			l.append(x)
			t=""
	return l

def getPrec(c):
	if c in ("+","-"):
		return 1
	if c in ("/","*","%"):
		return 2


def postfix(l):
	p=[]
	st=deque()
	for x in l:
		if x.isdigit():
			p.append(x)
		else:
			while len(st)!=0 and getPrec(st[len(st)-1])>=getPrec(x):
				p.append(st.pop())
			st.append(x)
	while(len(st)!=0):
		p.append(st.pop())
	return p
def evaluate(postfix):
	for x in postfix:
		if x.isdigit():
print postfix(getTokenList("11+10*123-1"))