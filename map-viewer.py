import xarray as xr
import matplotlib.pyplot as plt

#  Load NetCDF file
# 540 Ma Map87.5_PALEOMAP_1deg_Early_Cambrian_535Ma.nc
# file_path = "Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2\Map87.5_PALEOMAP_1deg_Early_Cambrian_535Ma.nc"

file_path = "Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2\Map66_PALEOMAP_1deg_Late_Devonian_370Ma.nc"


# file_path = "Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2\Map01_PALEOMAP_1deg_Holocene_0Ma.nc"


ds = xr.open_dataset(file_path)

# extract data 
z = ds['z']
lon = ds['lon']
lat = ds['lat']

# display map
plt.figure(figsize=(12, 6))
plt.contourf(lon, lat, z, levels=100, cmap='terrain')
plt.colorbar(label='Altitude (m)')
plt.title('Paleogeographic Map - Early Cambrian (535 Ma)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.tight_layout()
plt.show()
