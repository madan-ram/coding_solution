#
# The algorithm uses Barycentric coordinate system techniqe to detect wither point p is inside or outside triangle
#
import sys
class point:
	def __init__(self,x,y):
		self.x=float(x)
		self.y=float(y)

def test_inside(a,b,c,p):
	if (((b.y-c.y)*(a.x-c.x))+((c.x-b.x)*(a.y-c.y)))==0.0:
		return None
		sys.exit(0)
	alpha=(((b.y-c.y)*(p.x-c.x))+((c.x-b.x)*(p.y-c.y)))/(((b.y-c.y)*(a.x-c.x))+((c.x-b.x)*(a.y-c.y)))
	beta=(((c.y-a.y)*(p.x-c.x))+((a.x-c.x)*(p.y-c.y)))/(((b.y-c.y)*(a.x-c.x))+((c.x-b.x)*(a.y-c.y)))
	gama=1.0-alpha-beta
	if alpha<=1.0 and alpha>=0.0 and beta<=1.0 and beta>=0.0 and gama<=1.0 and gama>=0.0:
		return True
	else:
		return False


for test in xrange(input()):
	temp=map(float,raw_input().split())
	a=point(temp[0],temp[1])
	b=point(temp[2],temp[3])
	c=point(temp[4],temp[5])
	p=point(temp[6],temp[7])
	print test_inside(a,b,c,p)