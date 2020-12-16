import numpy as np

lines = []
with open('16/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

field_ranges = {}
field_set = []
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
  field_ranges[line[:cidx-1]] = range_flat
  field_set += range_flat


#print(field_ranges)

valid_nums = set(field_set)

#print(valid_nums)

i += 1
my_ticket = [int(n) for n in lines[i].split(',')]
valid_lines = []

def find_invalid_nums_in_line(line):
  for num in line.split(','):
    num = int(num)
    if num not in valid_nums:
      return True
  
  return False

find_invalid_nums_in_line(lines[i])
  
i += 3
nt = np.zeros((len(lines[i:]), len(lines[i].split(','))))
for j, line in enumerate(lines[i:]):
  if not find_invalid_nums_in_line(line):
    lsplit = [int(l) for l in line.split(',')]
    nt[j,:] = np.array(lsplit)


print(nt.shape)
nt = nt[~np.all(nt == 0, axis=1), :]
print(nt.shape)
#print(nt, field_ranges)

from collections import defaultdict

col_to_key = defaultdict(list)
for i in range(nt.shape[1]):
  for k, v in field_ranges.items():
    print(k, nt[:,i])
    if np.isin(nt[:,i] , v).all():
      col_to_key[i].append(k)

ctk = dict(col_to_key)
final_map = {}
while len(ctk.keys()) > 0:
  ld = {k:len(v) for k, v in ctk.items()}
  print(ld)
  k = min(ld, key=ld.get)
  print(ctk[k], k)
  col = ctk[k][0]
  final_map[col] = k
  del ctk[k]

  for k, v in ctk.items():
    if col in v:
      v.remove(col)


num = 1

for k, v in final_map.items():
  if 'departure' in k:
    print(k, v)
    num *= my_ticket[v]

print(num)