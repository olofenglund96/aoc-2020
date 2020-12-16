import numpy as np
import time

t0 = time.time()
lines = []
with open('13/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

busses = []

i = 0
for bus_id in lines[1].split(','):
  if bus_id != 'x':
    busses.append((int(bus_id), i))
    i = 0
  i += 1

print(busses)

def find_first_match(n1, n2, diff, i1, n_offset):
  i = n_offset
  matches = 0
  i0, j0 = 0, 0
  while True:
    jnum = diff + i*n1

    if jnum % n2 == 0:
      #print(f"i: {i}, j:{int(jnum / n2)}, j0:{j0}")
      if matches == 1:
        return i0, j0, int(jnum / n2) - j0
      elif matches == 0:
        i0 = i
        j0 = int(jnum / n2)
      
      matches += 1
    
    i += i1
        

# n1, n2, n3, n4 = busses[0], busses[1], busses[2], busses[3]
# x, y = find_first_match(n1[0], n2[0], n2[1], 1, 1)

# print(x, y, n1[0]*x, n2[0]*y)

# x1, y1 = find_first_match(n2[0], n3[0], n3[1], y, 1)
# print(x1, y1, n2[0]*x1, n3[0]*y1)

# x2, y2 = find_first_match(n3[0], n4[0], n4[1], y1, 1)
# print(x2, y2, n3[0]*x2, n4[0]*y2)

i = 0
n_incr = 1
n_offset = 0
for i in range(len(busses)-1):
  n1_ix, n1_offset = busses[i]
  n2_ix, n2_offset = busses[i+1]

  x, y, diff = find_first_match(n1_ix, n2_ix, n2_offset, n_incr, n_offset)

  n_incr = diff
  n_offset = y
  #print(x, y, n1_ix*x, n2_ix*y)

offset_sum = sum([a[1] for a in busses])
print(n2_ix*y - offset_sum)

t1 = time.time()

print(t1 - t0)