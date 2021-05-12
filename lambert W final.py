import numpy as np
import matplotlib
# ~ import matplotlib.patches as patches
import matplotlib.pyplot as plt
# ~ plt.style.use('fivethirtyeight')
plt.rcParams['axes.linewidth'] = 1.2
# ~ matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 13,
        }

n_rows = 2
n_cols = 2
n_plots = n_rows * n_cols
fig, ax = plt.subplots(n_rows, n_cols,figsize=(8,9), sharex = False, sharey = False)
fig.tight_layout()
f10=open("c10.txt","w")
f11=open("c11.txt","w")

f21=open("c21.txt","w")

f31=open("c31.txt","w")

f41=open("c41.txt","w")



c1 = -1
c2 = -1/np.e
c3 = -0.2
c4 = 0.2

xmin= -3*np.pi
xmax= 3*np.pi
xvalues = np.arange(xmin, xmax, 0.001)

for x in xvalues:
	y0 = -x * np.cos(x)/np.sin(x)
	y1 = np.log(-c1*(np.sin(x))/x)
	y2 = np.log(-c2*(np.sin(x))/x)
	y3 = np.log(-c3*(np.sin(x))/x)
	y4 = np.log(-c4*(np.sin(x))/x)
	f10.write('{} {}'.format(x,y0))
	f10.write('\n')
	f11.write('{} {}'.format(x,y1))
	f11.write('\n')
	f21.write('{} {}'.format(x,y2))
	f21.write('\n')
	f31.write('{} {}'.format(x,y3))
	f31.write('\n')
	f41.write('{} {}'.format(x,y4))
	f41.write('\n')
	
f10.close()	
f11.close()
f21.close()
f31.close()
f41.close()

data10=np.loadtxt('c10.txt')
data11=np.loadtxt('c11.txt')
data21=np.loadtxt('c21.txt')
data31=np.loadtxt('c31.txt')
data41=np.loadtxt('c41.txt')


s10=data10[:,0]
t10=data10[:,1]
s11=data11[:,0]
t11=data11[:,1]
s21=data21[:,0]
t21=data21[:,1]
s31=data31[:,0]
t31=data31[:,1]
s41=data41[:,0]
t41=data41[:,1]
########################################################################
ax[0,0].axis([-3*np.pi,3*np.pi,-3*np.pi,3*np.pi])
ax[0,0].plot(t10,s10,'r')
ax[0,0].plot(t11,s11,'b')
# ~ ax[0,0].axhline(y = 0., color = 'k', linestyle = '--', lw=0.7)
# ~ ax[0,0].axvline(x=0, color = 'k', linestyle = '--', lw=0.7)
ax[0,0].set_title(r'c < -1/e', fontdict=font)

ax[0,0].spines['left'].set_position('zero')
# ~ ax[0,0].spines['right'].set_color('none')
ax[0,0].spines['bottom'].set_position('zero')
# ~ ax[0,0].spines['top'].set_color('none')
twin1 = ax[0,0].twinx()
twin1.tick_params(axis='y',left=False, right=False,labelleft=False, labelright=False)


ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax[0,0].xaxis.set_major_formatter(plt.FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))

ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax[0,0].yaxis.set_major_formatter(plt.FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))
ax[0,0] = fig.add_axes((1,1,1,1))
# ~ my_ticks_x=[0.5,0.6,0.7,0.8,7/8.,1]
# ~ my_ticks_y=[0.,1/4.,0.5,0.75,1]
# ~ my_tickslabel_x=[r'$0.5$',r'$0.6$',r'$0.7$',r'$0.8$',r'$\frac{7}{8}$',r'$1.0$']
# ~ my_tickslabel_y=[r'$0$',r'$\frac{1}{4}$',r'$0.5$',r'$0.75$',r'$1.0$']
# ~ ax[0,1].set_xticks(my_ticks_x)
# ~ ax[0,1].set_xticklabels(my_tickslabel_x, fontsize=13)
########################################################################
ax[0,1].axis([-3*np.pi,3*np.pi,-3*np.pi,3*np.pi])
ax[0,1].plot(t10,s10,'r')
ax[0,1].plot(t21,s21,'b')
ax[0,1].set_title(r'c = -1/e', fontdict=font)

ax[0,1].spines['left'].set_position('zero')
ax[0,1].spines['right'].set_color('none')
ax[0,1].spines['bottom'].set_position('zero')
ax[0,1].spines['top'].set_color('none')


ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax[0,1].xaxis.set_major_formatter(plt.FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))

ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax[0,1].yaxis.set_major_formatter(plt.FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))
twin1 = ax[0,1].twinx()
twin1.tick_params(axis='y',left=False, right=False,labelleft=False, labelright=False)
########################################################################
ax[1,0].axis([-3*np.pi,3*np.pi,-3*np.pi,3*np.pi])
ax[1,0].plot(t10,s10,'r')
ax[1,0].plot(t31,s31,'b')
ax[1,0].set_title(r'-1/e < c <0', fontdict=font)

ax[1,0].spines['left'].set_position('zero')
ax[1,0].spines['right'].set_color('none')
ax[1,0].spines['bottom'].set_position('zero')
ax[1,0].spines['top'].set_color('none')


ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax[1,0].xaxis.set_major_formatter(plt.FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))

ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax[1,0].yaxis.set_major_formatter(plt.FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))

twin1 = ax[1,0].twinx()
twin1.tick_params(axis='y',left=False, right=False,labelleft=False, labelright=False)
########################################################################
ax[1,1].axis([-3*np.pi,3*np.pi,-3*np.pi,3*np.pi])
ax[1,1].plot(t10,s10,'r')
ax[1,1].plot(t41,s41,'b')
ax[1,1].set_title(r'c > 0', fontdict=font)

ax[1,1].spines['left'].set_position('zero')
ax[1,1].spines['right'].set_color('none')
ax[1,1].spines['bottom'].set_position('zero')
ax[1,1].spines['top'].set_color('none')


ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax[1,1].xaxis.set_major_formatter(plt.FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))

ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(np.pi))
ax[1,1].yaxis.set_major_formatter(plt.FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))

twin1 = ax[1,1].twinx()
twin1.tick_params(axis='y',left=False, right=False,labelleft=False, labelright=False)
fig.tight_layout()	
plt.savefig("lambertw.pdf")
plt.show()
