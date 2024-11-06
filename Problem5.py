import math
area = 1300
radius = 4
each_cell_covers = math.floor(2.5981 * radius ** 2)
print(f'Each Cell covers:{each_cell_covers}')
print('(a)')
number_of_cells = math.floor(area / each_cell_covers)
print(f'Number of cells: {number_of_cells}')
allocated_spectrum = 40000
channel_width = 60
frequency_reuse_factor = 7
print('(b)')
number_of_channel_per_cell = math.floor(allocated_spectrum / (channel_width * frequency_reuse_factor))
print(f'Number of channels per cell: {number_of_channel_per_cell}')
print('(c)')
traffic_intensity_per_cell = 84
print(f'Traffic intensity per cell: {traffic_intensity_per_cell}')
print('(d)')
maximum_carried_traffic = number_of_cells * traffic_intensity_per_cell
print(f'Maximum carried traffic: {maximum_carried_traffic}')
traffic_per_user = 0.03
print('(e)')
total_number_of_users = maximum_carried_traffic / traffic_per_user
print(f'Total number of users: {total_number_of_users}')
number_of_channels = number_of_channel_per_cell * frequency_reuse_factor
print('(f)')
number_of_mobile_per_channel = math.floor(total_number_of_users / number_of_channels)
print(f'Number of mobiles per channel: {number_of_mobile_per_channel}')
print('(g)')
theoretical_maximum_users = number_of_cells * number_of_channel_per_cell
print(f'Theoretical maximum number of users: {theoretical_maximum_users}')