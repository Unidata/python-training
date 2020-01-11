# Our import for numpy and metpy
import numpy as np
import matplotlib.pyplot as plt
from metpy.units import units

# Here's the "data"
np.random.seed(19990503)  # Make sure we all have the same data
temp = (20 * np.cos(np.linspace(0, 2 * np.pi, 100)) +
        80 + 2 * np.random.randn(100)) * units.degF
rh = (np.abs(20 * np.cos(np.linspace(0, 4 * np.pi, 100)) +
              50 + 5 * np.random.randn(100))) * units('percent')

# Create a mask for the two conditions described above
good_heat_index = (temp >= 80 * units.degF) & (rh >= 40 * units.percent)

# Use this mask to grab the temperature and relative humidity values that together
# will give good heat index values
hi_temps = temp[good_heat_index]
hi_rh = rh[good_heat_index]

# BONUS POINTS: Plot only the data where heat index is defined by
# inverting the mask (using `~mask`) and setting invalid values to np.nan
temp[~good_heat_index] = np.nan
rh[~good_heat_index] = np.nan

plt.plot(temp.m, color='tab:red')
plt.plot(rh.m, color='tab:green')
