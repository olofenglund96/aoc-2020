lines = []
with open('12/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

actions = []
for line in lines:
  t, v = line[0], line[1:]

  actions.append((t, int(v)))

#print(actions)
direction = 1
direction_dict = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
num_to_dir = ['N', 'E', 'S', 'W']
locations = [(0, 0)]

def add_vecs(v1, v2):
  v3 = []
  for i in range(len(v1)):
    v3.append(v1[i] + v2[i])

  return tuple(v3)

def mul_scal(v, s):
  v3 = []
  for i in range(len(v)):
    v3.append(v[i] * s)

  return tuple(v3)

for action in actions:
  t, v = action
  loc = locations[-1]
  #print(direction)
  curr_direction = num_to_dir[direction]

  if t == 'F':
    loc = add_vecs(loc, mul_scal(direction_dict[curr_direction], v))
  elif t == 'L':
    direction = int((direction - (v / 90)) % 4)
    print(t, direction)
  elif t == 'R':
    direction = int((direction + (v / 90)) % 4)
    print(t, v, direction)
  else:
    loc = add_vecs(loc, mul_scal(direction_dict[t], v))

  locations.append(loc)

  #if direction

x, y = locations[-1]

print(abs(x) + abs(y))
