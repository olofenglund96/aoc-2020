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
loc = (0, 0)
wp_loc = [-1, 10]

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

def rotate_waypoint(loc, wp_loc, rot):
  wpy, wpx = wp_loc

  if rot == 90:
    new_wp_loc = [wpx, -wpy]
  elif rot == 180:
    new_wp_loc = [-wpy, -wpx]
  else:
    new_wp_loc = [-wpx, wpy]

  return new_wp_loc




for action in actions:
  t, v = action

  if t == 'F':
    loc = add_vecs(loc, mul_scal(wp_loc, v))
  elif t == 'L':
    wp_loc = rotate_waypoint(loc, wp_loc, 360-v)
  elif t == 'R':
    wp_loc = rotate_waypoint(loc, wp_loc, v)
  else:
    wp_loc = add_vecs(wp_loc, mul_scal(direction_dict[t], v))

  #if direction

x, y = loc

print(abs(x) + abs(y))
