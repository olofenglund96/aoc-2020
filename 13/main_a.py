import numpy as np

lines = []
with open('13/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

tstamp = int(lines[0])
busses = []

for bus_id in lines[1].split(','):
  if bus_id != 'x':
    busses.append(int(bus_id))


#print(busses)

busmod = []
for bus in busses:
  busmod.append(bus - (tstamp % bus))

minbus_idx = np.argmin(busmod)
minbus_id = busses[minbus_idx]
minbus_delay = busmod[minbus_idx]

print(minbus_delay*minbus_id)
