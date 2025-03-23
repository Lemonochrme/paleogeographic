import xarray as xr
import matplotlib.pyplot as plt
import imageio
import os
import re
from glob import glob

data_dir = "Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2"
output_dir = "frames"
gif_path = "paleomap_evolution.gif"
cmap = "terrain" 
duration = 0.5

os.makedirs(output_dir, exist_ok=True)

def extract_age(filename):
    match = re.search(r"(\d+\.?\d*)Ma", filename)
    return float(match.group(1)) if match else float('inf')

files = sorted(glob(os.path.join(data_dir, "*.nc")), key=extract_age)
files.reverse()  # Reverse the order of the files

image_files = []

for i, filepath in enumerate(files):
    try:
        ds = xr.open_dataset(filepath)
        z = ds['z']
        lon = ds['lon']
        lat = ds['lat']
        age = extract_age(os.path.basename(filepath))

        plt.figure(figsize=(12, 6))
        plt.contourf(lon, lat, z, levels=100, cmap=cmap)
        plt.axis("off")
        plt.gca().set_position([0, 0, 1, 1])  # Remove white border
        plt.text(0.5, 0.95, f'{age:.1f} Ma', ha='center', va='top', transform=plt.gca().transAxes, fontsize=12, color='white', bbox=dict(facecolor='black', alpha=0.5))
        # plt.colorbar(label='Altitude (m)')
        # plt.title(f'Paleographic map – {age:.1f} Ma')
        # plt.xlabel('Longitude')
        # plt.ylabel('Latitude')
        # plt.grid(True)
        # plt.tight_layout()

        frame_path = os.path.join(output_dir, f"frame_{i:03d}.png")
        plt.savefig(frame_path)
        image_files.append(frame_path)
        plt.close()
    except Exception as e:
        print(f"Error {filepath}: {e}")

# GIF creation
with imageio.get_writer(gif_path, mode='I', duration=duration, loop=0) as writer:
    for file in image_files:
        image = imageio.imread(file)
        writer.append_data(image)

print(f"Gif created : {gif_path} ({len(image_files)} images)")
