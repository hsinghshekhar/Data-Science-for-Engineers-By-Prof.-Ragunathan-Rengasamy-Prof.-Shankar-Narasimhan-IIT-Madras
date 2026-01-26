import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Our original matrix A
data = np.array([
    [6.4, 21.8, 720],
    [6.7, 22.5, 745],
    [6.6, 23.1, 760],
    [6.8, 22.9, 780],
    [6.5, 21.5, 735]
])

pH = data[:, 0]
temp = data[:, 1]
ec = data[:, 2]

# 2. mAKE GRID for plane
ph_range = np.linspace(6, 7.5, 10)
temp_range = np.linspace(20, 25, 10)
PH, TEMP = np.meshgrid(ph_range, temp_range)

# 3 Null Space: EC = 134.14*pH - 6.13*Temp
EC_plane = 134.14 * PH - 6.13 * TEMP

# 4. Ploting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(pH, temp, ec, color='red', s=100, label='Actual Sensor Data')

surf = ax.plot_surface(PH, TEMP, EC_plane, alpha=0.5, cmap='viridis')

# Lavels and tiles
ax.set_xlabel('pH')
ax.set_ylabel('Temperature (°C)')
ax.set_zlabel('EC (µS/cm)')
ax.set_title('Visualizing the Row Space & Null Space Relationship')
plt.legend()
plt.show()