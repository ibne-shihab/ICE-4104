bw = 30000  # Bandwidth in Hz
schannel_bw = 25  # Single channel bandwidth in Hz
bw = 30000  # Bandwidth in Hz
schannel_bw = 25  # Single channel bandwidth in Hz
print("Channel Bandwidth...")
dup_ch_bw = 2 * schannel_bw  # Duplex channel bandwidth (both directions)
t_ch = bw / dup_ch_bw  # Total number of available channels
print(dup_ch_bw)
print("Total available channels:", t_ch)
# Control channel bandwidth
cc_bw = 1000  # Control channel bandwidth in Hz
t_cc = cc_bw / dup_ch_bw  # Number of control channels
print("Total control channels:", t_cc)
# N represents different cluster sizes
N = [4, 7, 12]  # Cluster sizes

# Loop through each cluster size in N
for i in range(3):
    # Calculate channels per cell for each cluster size
    ch = t_ch / N[i]
    ch_per_cell = round(ch)  # Rounded channels per cell
    print("Cluster size:", N[i])
    print("Channels per cell:", ch_per_cell)
    # Calculate control channels per cell
    c = t_cc / N[i]
    cc = round(c)
    # Calculate voice channels per cell
    v = (t_ch - t_cc) / N[i]
    vc = round(v)
    # Display the results for control and voice channels
    print("Control channels:", cc)
    print("Voice channels:", vc)

print("Channel Bandwidth...")
dup_ch_bw = 2 * schannel_bw  # Duplex channel bandwidth (both directions)
t_ch = bw / dup_ch_bw  # Total number of available channels
print(dup_ch_bw)
print("Total available channels:", t_ch)
# Control channel bandwidth
cc_bw = 1000  # Control channel bandwidth in Hz
t_cc = cc_bw / dup_ch_bw  # Number of control channels
print("Total control channels:", t_cc)
# N represents different cluster sizes
N = [4, 7, 12]  # Cluster sizes

# Loop through each cluster size in N
for i in range(3):
    # Calculate channels per cell for each cluster size
    ch = t_ch / N[i]
    ch_per_cell = round(ch)  # Rounded channels per cell
    print("Cluster size:", N[i])
    print("Channels per cell:", ch_per_cell)
    # Calculate control channels per cell
    c = t_cc / N[i]
    cc = round(c)
    # Calculate voice channels per cell
    v = (t_ch - t_cc) / N[i]
    vc = round(v)
    # Display the results for control and voice channels
    print("Control channels:", cc)
    print("Voice channels:", vc)
