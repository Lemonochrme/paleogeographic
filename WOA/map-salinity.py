import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# file_path = 'woa23_decav_s00_01.nc'
file_path = 'woa23_decav_t00_01.nc'

data = xr.open_dataset(file_path, decode_times=False)

print(data)

salinity = data['s_an']  # s_an variable represent climatological mean salinity

depth_index = 0  # (0, 5, 10, ..., 5000m)

salinity_filtered = salinity.where(salinity >= 32)

plt.figure(figsize=(16, 9))
ax = plt.axes(projection=ccrs.PlateCarree())
contourf = plt.contourf(salinity_filtered.lon, salinity_filtered.lat, salinity_filtered[0, depth_index, :, :], levels=20, cmap='RdYlBu_r', transform=ccrs.PlateCarree())
plt.colorbar(contourf, label='Salinity')
ax.coastlines(edgecolor='grey')
# ax.add_feature(cfeature.LAND, edgecolor='black')
plt.title('2023 Mean Water Salinity at 0 m Depth')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
