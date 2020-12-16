lines = []
with open('11/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

grid = [[]]*(len(lines) + 2)
grid[0] = ['.']*(len(lines[0]) + 2)

for i in range(1, len(lines)+1):
  grid[i] = ['.'] + list(lines[i-1]) + ['.']


grid[-1] = ['.']*(len(lines[0]) + 2)

def count_types(grid, row, col, axis):
  oc = 0

  directions = [(-1, -1),
                (-1, 0),
                (-1, 1), 
                (0, 1), 
                (1, 1), 
                (1, 0), 
                (1, -1), 
                (0,-1)]
  
  for yincr, xincr in directions:
    yix, xix = row, col
    
    while True:
      yix, xix = yix + yincr, xix + xincr
      if yix >= 0 and yix < len(grid) and xix >= 0 and xix < len(grid[0]) :
        if grid[yix][xix] == '#':
          #print(f"row: {yix}, col: {xix}, start: ({row}, {col})")
          oc += 1
          break
        elif  grid[yix][xix] == 'L':
          break
      else:
        break

      

  return 0, oc

def decide_seat(grid, row, col):
  empty_count, occupied_count = count_types(grid, row, col, 'asd')

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
      elif oc >= 5:
        new_grid[i][j] = 'L'

      tot_occ += oc
  
  #pprint_grid(new_grid)
  #input()
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