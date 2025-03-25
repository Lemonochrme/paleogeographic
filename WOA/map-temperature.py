import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'woa23_decav_t00_01.nc'

data = xr.open_dataset(file_path, decode_times=False)

print(data)

salinity = data['t_an']  # t_an variable represent mean temperature

depth_index = 20  # (0, 5, 10, ..., 5000m)

salinity_filtered = salinity.where(salinity >= 0)

plt.figure(figsize=(16, 9))
contourf = plt.contourf(salinity_filtered.lon, salinity_filtered.lat, salinity_filtered[0, depth_index, :, :], levels=20, cmap='RdYlBu_r')
plt.colorbar(contourf, label='Temperature')
plt.title('2023 Mean Water Temperature at 0 m Depth')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
