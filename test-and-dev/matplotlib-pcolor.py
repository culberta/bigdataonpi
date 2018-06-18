import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import math as m

nx=100;ny=50
xc=np.arange(0,nx,1)+0.5
yc=np.arange(0,ny,1)+0.5
f=lambda i,j:m.sin(xc[i]*m.pi/nx)*m.sin(yc[j]*m.pi/ny)
arr=np.fromfunction(np.vectorize(f),(nx-1,ny-1),dtype=int)

plt.pcolormesh(arr,cmap='jet')
plt.colorbar()
plt.show()

plt.pcolormesh(arr,cmap='jet',vmin=0.2,vmax=0.8)
plt.colorbar()
plt.show()
