import numpy as np

lines = []
with open('16/test', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

field_ranges = np.array(int)
my_ticket = []
nearby_tickets = []

i = 0
while True:
  line = lines[i]
  i += 1
  print(line)
  if line == '':
    break

  cidx = line.index(":") + 1
  ranges = line[cidx:].strip()

  rangei = [list(np.arange(int(rng.split('-')[0]), int(rng.split('-')[1]))) for rng in ranges.split(" or ")]
  range_flat = []
  for arr in rangei:
    print(arr)
    range_flat += rangei

  print(rangei, range_flat)
  field_ranges = np.append(field_ranges, np.array(rangei).flatten())


print(field_ranges.flatten())
