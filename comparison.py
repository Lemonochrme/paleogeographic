import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, TwoSlopeNorm

# Define file paths for three time periods
file_paths = [
    "Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2/Map06_PALEOMAP_1deg_Middle_Miocene_15Ma.nc",
    "Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2/Map03_PALEOMAP_1deg_Pliocene_5Ma.nc",
    "Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2/Map01_PALEOMAP_1deg_Holocene_0Ma.nc"
]

# Create custom land-sea colormap
def create_custom_colormap():
    land_cmap = plt.get_cmap('terrain', 128)
    sea_cmap = plt.get_cmap('Blues_r', 128)
    combined_colors = np.vstack((
        sea_cmap(np.linspace(0, 1, 128)),
        land_cmap(np.linspace(0, 1, 128))
    ))
    return ListedColormap(combined_colors)

custom_cmap = create_custom_colormap()

# Set up subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)
titles = ['Miocene (15 Ma)', 'Late Miocene (10 Ma)', 'Pliocene (5 Ma)']

for i, file_path in enumerate(file_paths):
    ds = xr.open_dataset(file_path)
    z = ds['z']
    lon = ds['lon']
    lat = ds['lat']

    # Normalization centered at 0
    z_min = float(z.min())
    z_max = float(z.max())
    divnorm = TwoSlopeNorm(vmin=z_min, vcenter=0, vmax=z_max)

    # Plot full global map
    ax = axes[i]
    contour = ax.contourf(lon, lat, z, levels=100,
                          cmap=custom_cmap, norm=divnorm)
    ax.set_title(titles[i])
    ax.set_xlabel("Longitude")
    if i == 0:
        ax.set_ylabel("Latitude")

# Add one shared colorbar
cbar = fig.colorbar(contour, ax=axes.ravel().tolist(), shrink=0.8, label='Altitude (m)')
plt.suptitle("Global Paleogeographic Maps", fontsize=16)
plt.show()
