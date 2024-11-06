import numpy as np

# Define constants
fc = 1.8  # Frequency in GHz
hb = 20   # Effective transmitter (base station) antenna height in meters

# Calculate T-R separation distance in kilometers
d = (np.sqrt(20**2 + 30**2)) / 1000  # Convert meters to kilometers

# Calculate Path Loss in high-rise urban areas
Lp = 135.41 + (12.49 * np.log10(fc)) - (4.99 * np.log10(hb)) + \
     ((46.84 - 2.34 * np.log10(hb)) * np.log10(d))

print(f'The path loss in high-rise urban areas, Lp = {Lp:.2f} dB')
