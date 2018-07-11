# Import modules
import matplotlib.pyplot as plt
import astropy
import numpy as np
from astropy.convolution import convolve as ap_convolve
from astropy.convolution import Box2DKernel

# Create and show histogram array a
a = np.random.normal(loc=0.0, scale=0.5, size = (5000,5000))
aphi = a.flatten()
plt.hist(aphi, bins=50)
plt.title('A')
plt.savefig('/Users/allisonculbert/Desktop/summer_2018_MIT/plot-code/hist-debug-figs/a-hist.png')
plt.show()
plt.clf()

# Create and show histogram of array b (shifted 3 over from a with a third of data points)
b = np.random.normal(loc=0.0, scale=0.5, size = (5000,5000))
b += 3 #shift
b = b[:1667, :5000] #third
bphi = b.flatten()
plt.hist(bphi, bins=50)
plt.title('B')
plt.savefig('/Users/allisonculbert/Desktop/summer_2018_MIT/plot-code/hist-debug-figs/b-hist.png')
plt.show()
plt.clf()

# Create and show histogram of array c (a combination of a and b)
c = np.concatenate((a, b))
phi = c.flatten()
plt.hist(phi, bins=50)
plt.title('C')
plt.savefig('/Users/allisonculbert/Desktop/summer_2018_MIT/plot-code/hist-debug-figs/c-hist.png')
plt.show()
plt.clf()

# Convolve
box_2D_kernel = Box2DKernel(10)
nan=float('nan')
c=np.where(c==0,nan,c)
c[ :, 0]=nan
c[ 0, :]=nan
c[ :,-1]=nan
c[-1, :]=nan
c2=ap_convolve(c, box_2D_kernel, normalize_kernel=True)

dd=c-c2
dd=dd[10:-10,10:-10]
dd=np.ma.masked_invalid(dd)
ddmean=np.mean(dd)
ddstd=np.std(dd)
dd=dd-ddmean
phi=dd.flatten()
plt.hist(phi, bins = 50)
plt.title('Convolved C')
plt.savefig('/Users/allisonculbert/Desktop/summer_2018_MIT/plot-code/hist-debug-figs/c-convolved-hist.png')
plt.show()
plt.clf()
