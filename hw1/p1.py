
import math
import numpy as np
import numpy.random as rand 
import matplotlib.pyplot as plt

def lambfunc(n):
	return 1.0/(((n+.5)**2)*math.pi**2)
def basisfunc(x,n,lambn):
	return math.sqrt(2)*math.sin(x/math.sqrt(lambn))
def meanl(x):
	return (1.0/8.0)*(x+1)**2

def eval(x):
	l1 = lambfunc(1)
	l1 = math.sqrt(l1)
	l2 = lambfunc(2)
	l2=math.sqrt(l2)
	l3 = lambfunc(3)
	l3=math.sqrt(l3)
	return meanl(x) + l1*basisfunc(x,1,l1)*rand.normal(0.0,1.0) +l2*basisfunc(x,2,l2)*rand.normal(0.0,1.0) + l3*basisfunc(x,1,l3)*rand.normal(0.0,1.0)

def func(n,lambn):
	return lambda x : basisfunc(x,n,lambn)

interval =np.linspace(0,1,1000)
vfunc = np.vectorize(eval)


def variance(x):
	l1 = lambfunc(1)
	l1 = math.sqrt(l1)
	l2 = lambfunc(2)
	l2=math.sqrt(l2)
	l3 = lambfunc(3)
	l3=math.sqrt(l3)
	return  (l1*basisfunc(x,1,l1))**2+(l2*basisfunc(x,2,l2))**2 + (l3*basisfunc(x,1,l3))**2

for i in range(0,1000):
	output = vfunc(interval)
	plt.plot(interval,output)

vfunc = np.vectorize(meanl)
output = vfunc(interval)
plt.plot(interval,output,'o')
plt.show()


one = np.vectorize(func(1,lambfunc(1)))
two = np.vectorize(func(2,lambfunc(2)))
three = np.vectorize(func(3,lambfunc(3)))
plt.plot(interval,one(interval),'o')
plt.plot(interval,two(interval),'-')
plt.plot(interval,three(interval))
plt.legend(["ph1","phi2","phi3"])
plt.show()

lastfunc = np.vectorize(variance)
plt.plot(interval,lastfunc(interval))
plt.show()
