import numpy as np
# Define constants
R = 1.387              # Cell Radius
n = 4                  # Number of cells
N = 60                 # Total number of channels
area = round(2.5981 * R**2)  # Area covered per cell
C = N / n              # Number of channels per cell
A = 9                  # Traffic intensity at c=15, GOS=0.05, Au=0.029 from Erlang C chart

# Question (a)
Au = 0.029             # Traffic per user
U = np.floor(A / Au)   # Number of users
U_per = round(U / area)  # Number of users per square km
print(f'(a) Number of users per square km: {U_per} users/sq km\n')

# Question (b)
lemda = 1              # lambda = 1 hour
H = (Au / lemda) * 3600  # Holding time in seconds
t = 10                 # Delay time in seconds
Prb = np.exp(-((C - A) * t) / H)  # Probability that a delayed call will have to wait
print(f'(b) The probability that a delayed call will have to wait: {Prb * 100:.2f}%\n')

# Question (c)
Prc = 0.05 * Prb * 100  # 5% probability of delayed call
print(f'(c) The probability that a call will be delayed: {Prc:.2f}%\n')
