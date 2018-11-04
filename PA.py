errList = []
import math
import numpy as np
import matplotlib.pyplot as plt

x0=int(input('x0 = '))
X = int(input('X = '))
y0 = int(input('y0 = '))
n= int(input('n = '))
h= input('(optional)h= ')
print(len(h))
def f(x,y):
	return 2*(math.sqrt(y) + y)
def Euler(f,x0,y0,n,X,h=-1):
	x = [x0]
	y = [y0]
	try:
		global errList
		if (n<1):
			errList.append('n must be greater than 0')
			return 'error'
		if (h==-1):
			h = (X - x0)/n
		u = 0
		for i in range(n):
			x.append(x[i]+h)
			di = h*f(x[i],y[i])
			y.append(y[i]+di)
	except BaseException as e:
			errList.append('Euler: '+ e)
	return x,y

def ImproveEuler(f,x0,y0,n,X,h=-1):
	x = [x0]
	y = [y0]
	try:
		global errList
		if (n<1):
			errList.append('n must be greater than 0')
			return 'error'
		if (h==-1):
			h = (X - x0)/n
		u = 0
		for i in range(n):
			x.append(x[i]+h)
			di = h*f(x[i],y[i])
			dy = h/2 * (f(x[i],y[i])+f(x[i]+h,y[i]+di))
			y.append(y[i]+dy)
	except BaseException as e:
			errList.append('ImproveEuler: '+ e)
	return x,y

def RungeKutta(f,x0,y0,n,X,h=-1):
	x = [x0]
	y = [y0]
	try:
		global errList
		if (n<1):
			errList.append('n must be greater than 0')
			return 'error'
		if (h==-1):
			h = (X - x0)/n
		u = 0
		for i in range(n):
			x.append(x[i]+h)
			k1 = f(x[i],y[i])
			k2 = f(x[i] + h/2,y[i] + k1 * h/2)
			k3 = f(x[i] + h/2,y[i] + k2 * h/2)
			k4 = f(x[i] + h,  y[i] + k3 * h  )
			dy = h * (k1 + 2*k2 + 2*k3 + k4)/6
			y.append(y[i]+dy)
	except BaseException as e:
			errList.append('ImproveEuler: '+ e)
	return x,y

def InitValue(x0,y0):
	sol = []
	print('x0 = {0},y0 = {1}'.format(x0,y0))
	if (y0 < 0):
		return BaseException
	if (1-math.sqrt(y0)>0 and math.sqrt(y0) !=1):
		c1 = math.log1p(1-math.sqrt(y0)) - x0
		sol.append(c1)
	
	if (1+math.sqrt(y0)>0):
		c2 = math.log1p(1+math.sqrt(y0)) - y0
		sol.append(c2)

	if (len(sol)==2):
		print('First solution: c1=',sol[0])
		print('Second solution: c2=',sol[1])
	elif (len(sol)==1):
		print('Solution: c=',sol[0])
	else:
		print('Has no solution')
		
	
ni = 222
mainplot = 	plt.subplot(221)
def printPlot(x,y,title='none'):
	global ni,mainplot
	x = np.array(x)
	y = np.array(y)
	p = plt.subplot(ni)
	ni+=1
	p.plot(x,y,label=title)
	p.legend()
	leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=False, fancybox=True)
	leg.get_frame().set_alpha(0.5)
	plt.grid(True)
	mainplot.plot(x,y)

def printOnePlote(x,y,title='none'):
	plt.plot(x,y)
	plt.title(title)
	plt.legend()
	plt.grid(True)
	plt.show()

InitValue(x0,y0)
x,y = Euler(f,x0,y0,n,X)
printPlot(x,y,'Euler')
#printOnePlote(x,y,'Euler')
x,y = ImproveEuler(f,x0,y0,n,X)
printPlot(x,y,'ImproveEuler')
#printOnePlote(x,y,'ImproveEuler')
x,y = RungeKutta(f,x0,y0,n,X)
printPlot(x,y,'Runge-Kutta')
#printOnePlote(x,y,'Runge-Kutta')

#mainplot.title = 'Three methods'
mainplot.grid(True)
leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.show()
print(','.join(errList))
