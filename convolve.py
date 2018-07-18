import netCDF4
import matplotlib.pyplot as plt
import matplotlib.colors as col
import os
import astropy
import numpy as np
from netCDF4 import Dataset
from astropy.convolution import convolve as ap_convolve
from astropy.convolution import Box2DKernel

# Change to directory o
os.chdir('/Volumes/Samsung_T5/plot-data-1')

# Create "handle" to access netCDF file
tFile = netCDF4.Dataset('20130109090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc')
sst=tFile['analysed_sst']

# Choose subregion (Hawaii)
sstReg=sst[0,10800:15000,1000:3500]-273.
sstReg=sst[0,11300:14000,1750:2750]-273. # area north of Hawaii


box_2D_kernel = Box2DKernel(9)
# nan=float('nan')
# sstReg=np.where(sstReg==0,nan,sstReg)
sstReg[ :, 0]=nan
sstReg[ 0, :]=nan
sstReg[ :,-1]=nan
sstReg[-1, :]=nan
sstReg2=ap_convolve(sstReg, box_2D_kernel)

dd=sstReg-sstReg2
dd=dd[9:-9,9:-9]
dd=np.ma.masked_invalid(dd)
ddmean=np.mean(dd)
ddstd=np.std(dd)
dd=dd-ddmean
phi=dd.flatten()
plt.hist(phi, bins = 50)
plt.savefig('0 values for nan all data')
plt.show()
plt.clf()