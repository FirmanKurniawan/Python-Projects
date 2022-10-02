from math import log

log2 = lambda x: log(x, 2)

def Unary(x):
	return (x-1)*'0'+'1'

def Binary(x, l = 1):
	s = '{0:0%db}' % l
	return s.format(x)
	
def Elias_Gamma(x):
	if(x == 0): return '0'
	n = 1 + int(log2(x))
	b = x - 2**(int(log2(x)))
	l = int(log2(x))
	return Unary(n) + Binary(b, l)
	
print(Elias_Gamma(10))