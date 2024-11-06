import numpy as np
# Define constants
pt = 50          # Transmitted power in watts
fc = 900         # Carrier frequency in MHz
gt = 1           # Transmitter antenna gain
gr = 1           # Receiver antenna gain
d = 100          # Free space distance in meters
L = 1            # System loss factor
c = 3 * 10**8    # Speed of light in m/s

# Calculate wavelength (lambda)
lambda_ = c / (fc * 10**6)  # Converting fc from MHz to Hz
# Question (a): Transmitter power in dBm
tr_dBm = np.ceil(10 * np.log10(pt * 1000))
print(f"(a) Transmitter power, Pt in dBm: {tr_dBm:.0f} dBm")
# Question (b): Transmitter power in dBW
tr_dBW = np.ceil(10 * np.log10(pt))
print(f"(b) Transmitter power, Pt in dBW: {tr_dBW:.0f} dBW")
# Question (c): Received power at 100 meters in dBm
c_value = (pt * gt * gr * (lambda_ ** 2)) / ((4 * np.pi) ** 2 * d ** 2 * L) * 1000
Pr = 10 * np.log10(c_value)
print(f"(c) Received power, Pr in dBm: {Pr:.2f} dBm")
# Question (d): Received power at 10 km in dBm
d_km = 10000  # Distance of 10 km in meters
Pr_10km = Pr + (20 * np.log10(d / d_km))
print(f"(d) Received power, Pr at 10km in dBm: {Pr_10km:.2f} dBm")