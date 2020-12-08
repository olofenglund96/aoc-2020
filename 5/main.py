import math

lines = []
with open('5/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

passports = [(line[:-3], line[-3:]) for line in lines]

#passports = [('FBFBBFF', 'RLR')]

def find_row(pass_str, low, high):
  print(pass_str, low, high)
  if abs(low-high) == 1:
    if pass_str == 'F':
      return low
    else:
      return high

  if pass_str[0] == 'F':
    high -= math.ceil((high - low) / 2)

    return find_row(pass_str[1:], low, high)
  else:
    low += math.floor((high - low) / 2)

    return find_row(pass_str[1:], low, high)

def find_col(pass_str, low, high):
  print(pass_str, low, high)
  if abs(low-high) == 1:
    if pass_str == 'L':
      return low
    else:
      return high

  if pass_str[0] == 'L':
    high -= math.ceil((high - low) / 2)

    return find_col(pass_str[1:], low, high)
  else:
    low += math.floor((high - low) / 2)

    return find_col(pass_str[1:], low, high)

saved_ids = []
for pass_row, pass_col in passports:
  print('---- Find row ----')
  row = find_row(pass_row, 0, 127)
  print('---- Find col ----')
  col = find_col(pass_col, 0, 7)

  saved_ids.append(row*8 + col)
  #input()
print('---')
for i in range(0, 965):
  if i not in saved_ids and i-1 in saved_ids and i+1 in saved_ids:
    print(i)
