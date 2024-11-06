# Initialize variables
blocking_p = 2 / 100  # Blocking probability
lamda = 2  # Arrival rate (calls per hour)
H = 3 / 60  # Average call duration in hours (3 minutes)
Au = lamda * H  # Traffic intensity per user (Erlangs)

# System A
print('For system A')
channel_a = 19
cell_A = 394
A = 12  # Total traffic intensity in system A

# Number of users in System A
Ua = A / Au
print('Number of users in System A:', Ua)

# Total number of subscribers in system A
subscriber_A = Ua * cell_A
print('Total number of subscribers in system A:', subscriber_A)

# Market penetration for system A
percentage_market_penetration_for_A = (subscriber_A / 2000000) * 100
print('Percentage market penetration for A:', percentage_market_penetration_for_A)

# System B
print('For system B')
channel_b = 57
cell_B = 98
Ab = 45  # Total traffic intensity in system B

# Number of users in System B
Ub = Ab / Au
print('Number of users in System B:', Ub)

# Total number of subscribers in system B
subscriber_B = Ub * cell_B
print('Total number of subscribers in system B:', subscriber_B)

# Market penetration for system B
percentage_market_penetration_for_B = (subscriber_B / 2000000) * 100
print('Percentage market penetration for B:', percentage_market_penetration_for_B)

# System C
print('For system C')
channel_c = 100
cell_C = 49
Ac = 88  # Total traffic intensity in system C

# Number of users in System C
Uc = Ac / Au
print('Number of users in System C:', Uc)

# Total number of subscribers in system C
subscriber_C = Uc * cell_C
print('Total number of subscribers in system C:', subscriber_C)

# Market penetration for system C
percentage_market_penetration_for_C = (subscriber_C / 2000000) * 100
print('Percentage market penetration for C:', percentage_market_penetration_for_C)

# Total number of subscribers across all systems
Total_number_of_subscriber = subscriber_A + subscriber_B + subscriber_C
print('Total number of subscribers across all systems:', Total_number_of_subscriber)
# Total market penetration across all systems
Market_penetration_for_three_systems = (Total_number_of_subscriber / 2000000) * 100
print('Market penetration for all three systems:', Market_penetration_for_three_systems)
