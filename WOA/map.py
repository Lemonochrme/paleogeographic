import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'woa23_decav_s00_01.nc'

data = xr.open_dataset(file_path, decode_times=False)

print(data)

salinity = data['s_an'] # s_an variable represent climatological mean salinity 

depth_index = 0  # (0, 5, 10, ..., 5000m)

salinity_filtered = salinity.where(salinity >= 32)

# plt.figure(figsize=(16, 9))
# sns.heatmap(salinity_filtered[0, depth_index, ::-1, :], cmap='inferno_r', cbar_kws={'label': 'Salinity'}, 
#             xticklabels=10, yticklabels=10)
# plt.title('Mean Water Salinity at 0 m Depth')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.show()

plt.figure(figsize=(16, 9))
# contour = plt.contour(salinity_filtered[0, depth_index, :, :], levels=42, colors='grey', linewidths=0.5)
# plt.clabel(contour, inline=True, fontsize=8, fmt='%1.1f')
contourf = plt.contourf(salinity_filtered[0, depth_index, :, :], levels=20, cmap='RdYlBu')
plt.colorbar(contourf, label='Salinity')
plt.title('2023 Mean Water Salinity at 0 m Depth')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()