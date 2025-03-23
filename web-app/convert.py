import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

file_path = "../Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2\Map01_PALEOMAP_1deg_Holocene_0Ma.nc"
ds = xr.open_dataset(file_path)
z = ds['z']
lon = ds['lon']
lat = ds['lat']

# custom colormap
terrain_cmap = plt.get_cmap("terrain")
colors = terrain_cmap(np.linspace(0, 1, 256))
colors[:128, :] = plt.get_cmap("Blues")(np.linspace(0, 1, 128))  # Set the lower half to blue
new_cmap = mcolors.ListedColormap(colors)


plt.figure(figsize=(12, 6))
plt.contourf(lon, lat, z, levels=100, cmap=new_cmap)
plt.axis("off")
plt.savefig("paleomap_0Ma_texture.png", bbox_inches="tight", pad_inches=0, dpi=300)
plt.close()