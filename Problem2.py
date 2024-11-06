import math
# Initialize variables
R_SI = 15  # Reference Signal to Interference ratio
io = 6  # Interference
n = [4, 3,5]  # Power values

# Loop through each element of n
for a in range(3):
    N = 7  # Initial reuse pattern size
    Q = math.sqrt(3 * N)  # Frequency reuse factor
    print('n:', n[a])
    print('Frequency reuse factor:', Q)
    
    # Calculate Signal to Interference Ratio (SI)
    SI = 10 * math.log10((1 / io) * (Q ** n[a]))
    print('Signal to interference ratio:', SI)
    
    # Check if SI is less than the reference value R_SI
    if SI < R_SI:
        i, j = 2, 2  # Parameters for new N
        N = (i ** 2) + (i * j) + (j ** 2)  # New reuse pattern size
        Q = math.sqrt(3 * N)  # Recalculate frequency reuse factor
        print('n:', n[a])
        print('New frequency reuse factor:', Q)
        
        # Calculate new Signal to Interference Ratio (SI1)
        SI1 = 10 * math.log10((1 / io) * (Q ** n[a]))
        print('New Signal to interference ratio:', SI1)
