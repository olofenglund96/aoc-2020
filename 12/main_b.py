import numpy as np

lines = []
with open('13/test', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

busses = []

i = 0
for bus_id in lines[1].split(','):
  if bus_id != 'x':
    busses.append((int(bus_id), i))
    i = 0

  i += 1


first_matches = []

def find_first_match(n1, n2, diff):
  for i in range(n1*n2):
    for j in range(n1*n2):
      if j*n2 - i*n1 == 1:
        return i, j


for i in range(len(busses)-1):
  n1, n2 = busses[i], busses[i+1]

  x, y = find_first_match(n1[0], n2[0], n2[1])

  first_matches.append((x, y))

print(first_matches)


i = 0
prod = 1
j = 0
while True:
  p1, p2 = first_matches[i]
  n1, n2 = busses[i][0], busses[i+1][0]

  print(p1, p2, n1, n2, (p2+n1*j)*n2 - (p1+n2*j)*n1)

  j += 1

  if j == 3:
    break
