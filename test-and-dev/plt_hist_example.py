
### CELL
# Load needed Python modules
import numpy as np
import os
import netCDF4
import matplotlib.pyplot as plt


# Switch to directory containing file(s)
os.chdir('/nfs/cnhlab003/cnh/mur-sst')


# Create "handle" to access netCDF file
# the variable "tFile" is not a simple variable but is an instance of 
# a the netcdf4.Dataset class ( see - http://unidata.github.io/netcdf4-python/#netCDF4.Dataset)
tFile = netCDF4.Dataset('20110913090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc')

# To see something about the class instance variable tFile we can apply the print function to the tFile instance.
print(tFile)


# Reading the output of print() we can see that tFile contains a netCDF variable called 'analysed_sst'
# This holds the sea-surface temperature that we want to plot, so we extract it.
# Extract sst from file
sst=tFile['analysed_sst']

# Check dimensions
# The variable sst turns out to have 3 dimensions time,lat,lon
print(sst.shape)


# Extract a subregion
# Take time level 0 (thats all there is for this example)
# Subtract 273. to convert from Kelvin to Celcius. 
sstReg=sst[0,10800:15000,1000:3500]-273.


# Make a very basic plot
plt.imshow(sstReg,origin='lower',cmap='prism');plt.colorbar();plt.show()


### CELL
# Make a histogram
phi=sstReg.flatten()
print(np.shape(phi))
print(np.max(phi))
print(np.min(phi))


### CELL
plt.hist(phi, bins=50);
