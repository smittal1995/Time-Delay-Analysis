import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.special import lambertw

xmin=-5
xmax=5
xvalues = np.arange(xmin, xmax, 0.001)

f0=open("x.txt","w")
f1=open("w0.txt","w")
f2=open("w1.txt","w")
f3=open("xex.txt","w")


for x in xvalues:
	y0 = x
	if x > -1/np.e:
		y1 = lambertw(x,k=0)
		f1.write('{} {}'.format(x,y1.real))
		f1.write('\n')
		if x < 0:
			y2 = lambertw(x,k=-1)
			f2.write('{} {}'.format(x,y2.real))
			f2.write('\n')


	y3 = x*np.e**x
	f0.write('{} {}'.format(x,y0))
	f0.write('\n')
	f3.write('{} {}'.format(x,y3))
	f3.write('\n')

f0.close()	
f1.close()
f2.close()
f3.close()

data0=np.loadtxt('x.txt')
data1=np.loadtxt('w0.txt')
data2=np.loadtxt('w1.txt')
data3=np.loadtxt('xex.txt')

s0=data0[:,0]
t0=data0[:,1]
s1=data1[:,0]
t1=data1[:,1]
s2=data2[:,0]
t2=data2[:,1]
s3=data3[:,0]
t3=data3[:,1]


plt.plot(s0,t0,'k--', label = 'x')
plt.plot(s1,t1,'r', label = r'$W_0(x)$')
plt.plot(s2,t2,'g', label = r'$W_{-1}(x)$')
plt.plot(s3,t3,'b', label = 'xe^x')
plt.axis([-5,5.0,-5.0,5.0])
plt.legend(loc=0)
plt.savefig("W-xex.pdf")
plt.tight_layout()
plt.show()
