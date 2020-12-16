lines = []
with open('11/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

grid = [[]]*(len(lines) + 2)
grid[0] = ['.']*(len(lines[0]) + 2)

for i in range(1, len(lines)+1):
  grid[i] = ['.'] + list(lines[i-1]) + ['.']


grid[-1] = ['.']*(len(lines[0]) + 2)

def count_types(grid, row, col, axis):
  ec = 0
  oc = 0

  srow, scol = row - 1, col - 1
  #print(axis, srow, scol)
  for i in range(scol, scol + 3):
    if grid[srow][i] == '#':
        oc += 1
  
  for i in range(srow + 1, srow + 3):
    if grid[i][scol + 2] == '#':
        oc += 1

  for i in range(srow + 1, srow + 3):
    if grid[i][scol] == '#':
        oc += 1

  if grid[row + 1][col] == '#':
    oc += 1

  return 0, oc

  
  #input()

  if axis == 'row' and (row < len(grid) and row >= 0):
    for i in range(col, col + 3):
      if i >= len(grid[0]) or i < 0:
        continue

      #print(axis, row, i)

      if grid[row][i] == '#':
        oc += 1
      else:
        ec += 1

  elif axis == 'col' and (col < len(grid[0]) and col >= 0):
    for i in range(row, row + 3):
      if i >= len(grid) or i < 0:
        continue
      
      #print(axis, i, col)
      if grid[i][col] == '#':
        oc += 1
      else:
        ec += 1
        

  #print(ec, oc)
  #input()
  return ec, oc

def decide_seat(grid, row, col):
  offsets = [(row - 1, col - 1, 'row'),
             (row - 1, col - 1, 'col'),
             (row - 1, col + 1, 'col'),
             (row + 1, col - 1, 'row')]

  empty_count, occupied_count = 0, 0

  #print(f'--- count seat at ({row}, {col}) ---')
  empty_count, occupied_count = count_types(grid, row, col, 'asd')

  
  #print(f"final count: (empty: {empty_count}, occupied: {occupied_count})")
  return empty_count, occupied_count

def pprint_grid(grid):
  gridstring = ''

  for row in grid:
    gridstring += ''.join(row) + '\n'

  print(gridstring)

pprint_grid(grid)

grid_stable = False
prev_tot_occ = 0
done_count = 0
while not grid_stable:
  tot_occ = 0
  new_grid = [row.copy() for row in grid]
  for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
      if grid[i][j] == '.':
        continue

      ec, oc = decide_seat(grid, i, j)

      if oc == 0:
        new_grid[i][j] = '#'
      elif oc >= 4:
        new_grid[i][j] = 'L'

      tot_occ += oc
  
  pprint_grid(new_grid)
  
  if prev_tot_occ == tot_occ:
    done_count += 1

    if done_count > 5:
      grid_stable = True
  
  prev_tot_occ = tot_occ
  grid = new_grid

tot_occ = 0
for row in grid:
  tot_occ += row.count('#')

print(tot_occ)