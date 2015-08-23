class D(object):
	a = None
	def __init__(self,a):
		self.a = a

	def __add__(self,b):

		return self.a+b.a


a1=D(1)
a2=D(2)
print a1+a2