import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm, TwoSlopeNorm

# Load NetCDF file
file_path = "Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2\\Map05_PALEOMAP_1deg_middle_Late_Miocene_10Ma.nc"

ds = xr.open_dataset(file_path)

# Extract data
z = ds['z']
lon = ds['lon']
lat = ds['lat']

# Create custom colormap
z_min = float(z.min())
z_max = float(z.max())

# Create separate colormaps
land_cmap = ListedColormap(plt.get_cmap('terrain', 128)(np.linspace(0.5, 0.9, 128)))
sea_cmap = ListedColormap(plt.get_cmap('Blues_r', 128)(np.linspace(0, 0.5, 128)))

# Combine them into one
combined_colors = np.vstack((
    sea_cmap(np.linspace(0, 1, 128)),
    land_cmap(np.linspace(0, 1, 128))
))
custom_cmap = ListedColormap(combined_colors)

# Create a normalization that centers at zero
divnorm = TwoSlopeNorm(vmin=z_min, vcenter=0, vmax=z_max)

# Display map
plt.figure(figsize=(16, 9))
contour = plt.contourf(lon, lat, z, levels=100, cmap=custom_cmap, norm=divnorm)
plt.colorbar(contour, label='Altitude (m)')
plt.title('Paleogeographic Map - Miocene (15 Ma)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(False)
plt.tight_layout()
plt.show()
