import numpy as np

lines = []
with open('16/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

field_ranges = []
my_ticket = []
nearby_tickets = []

i = 0
while True:
  line = lines[i]
  i += 1
  #print(line)
  if line == '':
    break

  cidx = line.index(":") + 1
  ranges = line[cidx:].strip()

  rangei = [list(np.arange(int(rng.split('-')[0]), int(rng.split('-')[1])+1)) for rng in ranges.split(" or ")]
  range_flat = []
  for arr in rangei:
    #print(arr)
    range_flat += arr

  #print(rangei, range_flat)
  field_ranges += range_flat


#print(field_ranges)

valid_nums = set(field_ranges)

#print(valid_nums)

i += 1
invalid_nums = []

def find_invalid_nums_in_line(line):
  for num in line.split(','):
    num = int(num)
    if num not in valid_nums:
      invalid_nums.append(num)

find_invalid_nums_in_line(lines[i])
  
i += 3

for line in lines[i:]:
  find_invalid_nums_in_line(line)

#print(invalid_nums)
print(sum(invalid_nums))