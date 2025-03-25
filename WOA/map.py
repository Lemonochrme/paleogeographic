import xarray as xr
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'woa23_decav_s00_01.nc'

data = xr.open_dataset(file_path, decode_times=False)

print(data)

salinity = data['s_an'] # s_an variable represent climatological mean salinity 

depth_index = 0  # (0, 5, 10, ..., 5000m)

salinity_filtered = salinity.where(salinity >= 20)

plt.figure(figsize=(16, 9))
sns.heatmap(salinity_filtered[0, depth_index, ::-1, :], cmap='inferno_r', cbar_kws={'label': 'Salinity'}, 
            xticklabels=10, yticklabels=10)
plt.title('Mean Water Salinity at 0 m Depth')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()