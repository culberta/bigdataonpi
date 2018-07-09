import netCDF4
import matplotlib.pyplot as plt
import matplotlib.colors as col
import os
import astropy
import numpy as np
import pprint
from netCDF4 import Dataset
from netCDF4 import num2date
from astropy.convolution import convolve as ap_convolve
from astropy.convolution import Box2DKernel

# Change to SSD with files
os.chdir('/Volumes/Samsung_T5/')

for filename in os.listdir('plot-data-all'):
    if filename != 'engaging-key' and filename[:6] == '201110':
        #Create "handle" to access netCDF file
        tFile = Dataset('plot-data-all/' + filename)
        print(filename)
        
        # Extract date
        date_num = tFile['time'][:]
        units = tFile.variables['time'].units
        date = num2date(date_num, units)[0]

        # Extract data
        sst=tFile['analysed_sst']

        # Choose subregion (Hawaii)
        sstReg=sst[0,10800:15000,1000:3500]-273.
        #sstReg=sst[0,11300:14000,1750:2750]-273. # area north of Hawaii

        # phi=sstReg.flatten()
        # plt.hist(phi, bins = 50)
        # plt.title(str(date))
        # plt.savefig('oct-2011/' + str(date) + '.png')
        # plt.clf()

        box_2D_kernel = Box2DKernel(10)
        nan=float('nan')
        sstReg=np.where(sstReg==0,nan,sstReg)
        sstReg[ :, 0]=nan
        sstReg[ 0, :]=nan
        sstReg[ :,-1]=nan
        sstReg[-1, :]=nan
        sstReg2=ap_convolve(sstReg, box_2D_kernel, normalize_kernel=True)

        dd=sstReg-sstReg2
        dd=dd[10:-10,10:-10]
        dd=np.ma.masked_invalid(dd)
        ddmean=np.mean(dd)
        ddstd=np.std(dd)
        dd=dd-ddmean
        phi=dd.flatten()
        plt.hist(phi, bins = 50, range = (-5, 5))
        plt.title(str(date))
        plt.savefig('conv-oct-2011/' + str(date) + '.png')
        plt.clf()