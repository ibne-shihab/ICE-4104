import numpy as np

# Initialize variables
Gos = 0.5 / 100  # Grade of service (blocking probability)
Au = 0.1  # Traffic intensity per user
A = np.array([0.005, 1.13, 3.96, 11.1, 80.9])  # Traffic intensity
c = np.array([1, 5, 10, 20, 100])  # Number of channels

# Displaying the given values
print('Blocking probability:', Gos)
print('Traffic intensity per user:', Au)
print('Traffic intensity:', A)
print('Number of channels:', c)

# Calculate the number of users for each value of A
U = A / Au  # Total traffic divided by traffic per user gives number of users
u = np.round(U)  # Round to nearest whole number
print('Number of users:', u)