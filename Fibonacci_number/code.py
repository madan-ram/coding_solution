import math

FI = 1.61803
def fib_num(pos):
    global FI
    return int(round(FI**pos/math.sqrt(5) + 1/2.0))

for i in xrange(0, 10):
    print fib_num(i)