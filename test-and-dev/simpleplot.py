# Load needed Python modules
import netCDF4
import matplotlib.pyplot as plt


# Switch to directory containing file(s)
cd '/nfs/cnhlab003/cnh/mur-sst'


# Create "handle" to access netCDF file
tFile = netCDF4.Dataset('20110913090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc')


# Extract sst from file
sst=tFile['analysed_sst']

# Check dimensions
print(sst.shape)


# Extract a subregion
sstReg=sst[0,10800:15000,1000:3500]-273.


# Make a very basic plot
plt.imshow(sstReg,origin='lower',cmap='prism');plt.colorbar();plt.show()
