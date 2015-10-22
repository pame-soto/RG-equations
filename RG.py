# Equation (a) : K'=(1/2)*ln[cosh(2K)], f(K)=2*cosh^{1/2}(2K)
# Equation (b) : g(K')=2*g(K)-ln[2*sqrt(cosh(2K))]
# Equation (c) : K=(1/2)*cosh^{-1}(e^{2K'})
# Equation (d) : g(K)=(1/2)*g(K')+(1/2)*ln[2]+K'/2  [since f(K)=2*exp(K')]

import math

print(' K        g')

# Starting values
K=10    
g=10

count=0
for count in xrange(10,-1,-1):                          # I tried using while
	Kn=(1/2)*(math.log(math.cosh(2*K)))
	gn=(2*g)-(math.log(2*math.sqrt(math.cosh(2*K))))

	K=Kn
	g=gn

	print K, '\t', g

print ''	
print 'Ready!'
