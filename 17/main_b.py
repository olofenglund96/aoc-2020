import numpy as np

lines = []
with open('17/test', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

no_lines = len(lines)
line_len = len(lines[0])

no_lines_even = no_lines + no_lines % 2
line_len_even = line_len + line_len % 2

xdim = no_lines + 15
xdim = xdim + (xdim + 1) % 2
ydim = line_len + 15
ydim =  ydim + (ydim + 1) % 2

space_size = np.array([xdim, ydim, 15, 15])
space = np.zeros(space_size)

mid_indices = (space_size - 1) // 2
for i, line in enumerate(lines):
  for j, char in enumerate(line):
    idx_x = mid_indices[0] - no_lines_even // 2 + i + 1
    idx_y = mid_indices[1] - line_len_even // 2 + j + 1
    idx_z = mid_indices[2]
    idx_w = mid_indices[3]

    print(idx_x, idx_y, idx_z, idx_w)
    if char == '#':
      space[idx_x,idx_y,idx_z,idx_w] = 1

print(f"Space has dimensions: {space.shape}")

def get_next_point(field, index, iter):
  active = field[index] == 1
  x, y, z, w = index
  #print(index, field[index])
  #print(x, y, z)
  subspace_idx = np.ogrid[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2]
  #print(subspace_idx)
  #input()
  num_active = int(np.sum(field[tuple(subspace_idx)]) - field[tuple(index)])

  if num_active < 0:
    print("Num active > 0")
    tmp_field_save = field[tuple(index)]
    field[tuple(index)] = 9
    print(x, y, z, num_active)
    print(field[:,:,z])
    field[tuple(index)] = tmp_field_save
    input()
  if active and num_active in [2,3]:
    return 1

  if not active and num_active == 3:
    return 1

  return 0

def get_next_field(old_field, iter):
  x, y, z, w = old_field.shape
  new_field = np.zeros(old_field.shape)

  for i in range(1, x-1):
    for j in range(1, y-1):
      for k in range(1, z-1):
        for l in range(1, w-1):
          new_field[i, j, k, l] = get_next_point(old_field, (i,j,k,l), iter)


  return new_field

def print_field(field, iter):
  print(int((field.shape[2]-1) // 2 - iter), int((field.shape[2]-1) // 2 + iter))
  for i in range(int((field.shape[2]-1) // 2 - iter), int((field.shape[2]-1) // 2 + iter) + 1):
    print(f"z={i}")
    print(field[:,:,i])

for i in range(6):
  #print_field(space, i)
  #input()
  space = get_next_field(space, i)



print(np.sum(space))
